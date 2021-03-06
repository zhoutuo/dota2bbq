import sqlite3
import json
import hashlib
import hmac
import os
from flask import Flask, render_template, request, g, redirect, session, url_for, abort
from functools import wraps

SALT = "DOTA2"
app = Flask(__name__)
app.config.from_pyfile(os.path.join(
	os.path.dirname(__file__), "./setting.py"))


@app.before_request
def before_request():
	g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
	g.db.close()


def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if 'username' not in session:
			return 'you have no right to edit this page'
		else:
			return f(*args, **kwargs)
	return decorated_function


@app.route('/')
def index():
	return render_template("index.html", **generate_base_arg())


@app.route('/heroes')
def heroes():
	heroes = query_db("SELECT Name, Faction, Class FROM Heroes", [], one=False)
	entry = {'heroes': heroes}
	entry.update(generate_base_arg());
	return render_template("heroes.html", **entry)


@app.route('/items')
def items():
	return render_template("items.html", **generate_base_arg())


@app.route('/ajax/combined')
def combined_feed():
	query = g.db.execute("""SELECT Heroes.[Name]
		FROM Heroes""").fetchall()
	heroes = [{'Name': row[0], 'Class': "Hero"} for row in query]
	query = g.db.execute("""SELECT IID, Name
		FROM Items""").fetchall()
	items = [{'ID': row[0],'Name': row[1], 'Class': "Item"} for row in query]
	return json.dumps(heroes + items)


@app.route('/ajax/<hero_name>/<int:skill_index>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def skill_feed(hero_name, skill_index):
	skill = dict()
	if request.method == 'GET':
		entry = query_db("""SELECT Type, Manacost, Cooldown FROM Skills
			WHERE Skills.[HeroName] = ? AND Skills.[Number] = ?
			LIMIT 1
		""", [hero_name, skill_index], one=True)
		if entry:
			skill = {"Result": "OK", "Content": entry}
		else:
			skill = {"Result": "None"}
	elif request.method == 'POST':
		try:
			g.db.execute("""INSERT INTO Skills VALUES(?, ?, ?, ?, ?, ?, ?)
				""", (
					hero_name,
					skill_index,
					request.form['skill_name'],
					request.form['skill_desc'],
					request.form['skill_type'],
					request.form['skill_manacost'],
					request.form['skill_cooldown']))
			g.db.commit()
			skill = {"Result": "OK", "Content": "This skill is successfully created"}
		except sqlite3.IntegrityError as e:
			skill = {"Result": "Failure", "Content": e.args[0]}
	elif request.method == 'PUT':
		c = g.db.cursor()
		c.execute("""UPDATE Skills SET SkillName = ?, Description = ?, Type = ?, ManaCost = ?, Cooldown = ?
			WHERE HeroName = ? AND Number = ?
			""", (
				request.form['skill_name'],
				request.form['skill_desc'],
				request.form['skill_type'],
				request.form['skill_manacost'],
				request.form['skill_cooldown'],
				hero_name,
				skill_index))
		g.db.commit()
		if c.rowcount == 1:
			skill = {"Result": "OK", "Content": "This skill gets updated successfully"}
		else:
			skill = {"Result": "Failure", "Content": "There is no such skill"}
	else:
		c = g.db.cursor()
		c.execute("""DELETE FROM Skills
			WHERE HeroName = ? AND Number = ?
			""", (hero_name, skill_index))
		g.db.commit()
		if c.rowcount == 1:
			skill = {"Result": "OK", "Content": "This skill is successfully deleted"}
		else:
			skill = {"Result": "Failure", "Content": "there is no such skill to be deleted"}
	return json.dumps(skill)


@app.route("/ajax/items")
def item_feed():
	item = query_db(
		"""SELECT * FROM Items
		""", one=False)
	if len(item) == 0:
		item = {"Result": "None"}
	else:
		item = {"Result": "OK", "Content": item}
	return json.dumps(item)


@app.route('/hero/<hero_name>')
def hero(hero_name):
	entry = query_db(
		"""SELECT Heroes.[Name], Factions.[Name] AS Faction, Classes.[Name] AS Class,
		Lore, BasicStr, BasicAgi, BasicInt, StrInc, AgiInc, IntInc,
		Movement, Armor, MinDamage, MaxDamage
		FROM Heroes, Classes, Factions
		WHERE Heroes.[Name] = ? AND Classes.[Index] = Heroes.[Class]
		AND Factions.[Index] = Heroes.[Faction]
		LIMIT 1""",
		[hero_name], one=True)

	if entry == None:
		return redirect('/hero/' + hero_name + "/_edit")
	else:
		skills = query_db(
			"""	SELECT * FROM Skills
				WHERE HeroName = ?
				ORDER BY Number ASC
			""", [hero_name], one=False)
		entry["skills"] = skills;
		entry.update(generate_base_arg())
		return render_template("hero.html", **entry)


@app.route('/signin', methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	entry = query_db("SELECT Password FROM Users WHERE Username = ?", (username, ), one=True)
	if entry:
		hashed = hmac.new(SALT, password, hashlib.sha1)
		if hashed.hexdigest() == entry['Password']:
			session['username'] = username
		else:
			session['login_error'] = 'wrong password'
	else:
		session['login_error'] = 'no such user'

	return redirect(request.referrer) if request.referrer else redirect(url_for('index'))


@app.route('/signoff', methods=['POST'])
def signoff():
	session.pop('username', None)
	return redirect(request.referrer) if request.referrer else redirect(url_for('index'))


@app.route('/hero/<hero_name>/_edit', methods=['GET', 'POST'])
@login_required
def hero_edit(hero_name):
	#retrive info editable info to client
	if request.method == 'GET':
		entry = query_db("SELECT * FROM Heroes WHERE Name = ? LIMIT 1",
			[hero_name], one=True)
		if entry == None:
			entry = dict()
			entry["Name"] = hero_name
			entry["Faction"] = ""
			entry["Class"] = ""
			entry["Lore"] = ""
			entry["BasicStr"] = ""
			entry["BasicAgi"] = ""
			entry["BasicInt"] = ""
			entry["StrInc"] = ""
			entry["AgiInc"] = ""
			entry["IntInc"] = ""
			entry["Movement"] = ""
			entry["Armor"] = ""
			entry["MinDamage"] = ""
			entry["MaxDamage"] = ""
			entry["IsNew"] = "True"
			entry['Skills'] = [];
			return render_template("hero_edit.html", **entry)
		else:
			entry["IsNew"] = "False"
			skills = query_db("SELECT * FROM Skills WHERE HeroName = ? ORDER BY Number ASC", (hero_name, ), one=False)
			entry['Skills'] = skills;
			return render_template("hero_edit.html", **entry)
	#get edited info from client
	else:
		if request.form["IsNew"] == "False":
			g.db.execute(
					"""UPDATE Heroes
					SET Faction = ?, Class = ?,
					Lore = ?, BasicStr = ?, BasicAgi = ?, BasicInt = ?,
					StrInc = ?, AgiInc = ?, IntInc = ?, Movement = ?,
					Armor = ?, MinDamage = ?, MaxDamage = ?
					WHERE Name = ?
					""",
					(request.form["Faction"],
					request.form["Class"],
					request.form["Lore"],
					request.form["BasicStr"],
					request.form["BasicAgi"],
					request.form["BasicInt"],
					request.form["StrInc"],
					request.form["AgiInc"],
					request.form["IntInc"],
					request.form["Movement"],
					request.form["Armor"],
					request.form["MinDamage"],
					request.form["MaxDamage"],
					request.form["Name"]))
			g.db.commit()
		else:
			g.db.execute("""INSERT INTO Heroes(Name, Faction, Class, Lore, BasicStr,
					BasicAgi, BasicInt, StrInc, AgiInc, IntInc,
					Movement, Armor, MinDamage, MaxDamage)
				VALUES(?, ?, ?, ?, ?,
					?, ?, ?, ?, ?,
					?, ?, ?, ?)
				""", (request.form["Name"],
					request.form["Faction"],
					request.form["Class"],
					request.form["Lore"],
					request.form["BasicStr"],
					request.form["BasicAgi"],
					request.form["BasicInt"],
					request.form["StrInc"],
					request.form["AgiInc"],
					request.form["IntInc"],
					request.form["Movement"],
					request.form["Armor"],
					request.form["MinDamage"],
					request.form["MaxDamage"],
					))
			g.db.commit()
	return redirect("/hero/" + hero_name)


@app.route('/items/<int:item_id>/_edit', methods=['GET', 'POST'])
@login_required
def item_edit(item_id):
	if request.method == 'GET':
		entry = query_db("""SELECT * FROM Items WHERE IID = ?""", (item_id, ), one=True)
		if entry:
			return render_template('item_edit.html', **entry);
		else:
			abort(404)
	else:
		c = g.db.cursor()
		c.execute("""UPDATE Items set Description = ?, Cost = ?, Usage = ?, Attributes = ?, Recipe = ?
			WHERE IID = ?""", (
				request.form['Description'],
				request.form['Cost'],
				request.form['Usage'],
				request.form['Attributes'],
				request.form['Recipe'],
				request.form['IID']
				))
		g.db.commit()
		return redirect(url_for('items'));





def connect_db():
	return sqlite3.connect(os.path.join(
		os.path.dirname(__file__), app.config['DATABASE']))


def query_db(query, args=(), one=False):
	cur = g.db.execute(query, args)
	rv = [dict((cur.description[idx][0], value)
		for idx, value in enumerate(row)) for row in cur.fetchall()]
	return (rv[0] if rv else None) if one else rv


def generate_base_arg():
	username = None
	error = None
	if 'username' in session:
		username = session['username']
	elif 'login_error' in session:
		error = session['login_error']
		session.pop('login_error', None)
	return dict(username = username, error = error)

if __name__ == '__main__':
	app.run()
