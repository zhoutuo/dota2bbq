import sqlite3
import json
import os
from flask import Flask, render_template, request, g, redirect

app = Flask(__name__)
app.config.from_pyfile(os.path.join(
	os.path.dirname(__file__), "./setting.py"))


@app.before_request
def before_request():
	g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
	g.db.close()


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/heroes')
def heroes():
	return render_template("heroes.html")


@app.route('/items')
def items():
	return render_template("items.html")


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
		return render_template("hero.html", **entry)


@app.route('/ajax/combined')
def combined_feed():
	query = g.db.execute("""SELECT Heroes.[Name]
		FROM Heroes""").fetchall()
	heroes = [{'Name': row[0], 'Class': "Hero"} for row in query]
	query = g.db.execute("""SELECT Items.[Name]
		FROM Items""").fetchall()
	items = [{'Name': row[0], 'Class': "Item"} for row in query]
	return json.dumps(heroes + items)


@app.route('/ajax/<hero_name>/<skill_index>')
def skill_feed(hero_name, skill_index):
	entry = query_db("""SELECT Type, Manacost, Cooldown FROM Skills
			WHERE Skills.[HeroName] = ? AND Skills.[Number] = ?
			LIMIT 1
		""", [hero_name, skill_index])
	if len(entry) == 1:
		skill = {"Result": "OK", "Content": entry[0]}
	else:
		skill = {"Result": "None"}
	return json.dumps(skill)


@app.route("/ajax/<hero_name>/skills")
def skills_feed(hero_name):
	skills = query_db(
		"""	SELECT SkillName, Description FROM Skills
			WHERE Skills.[HeroName] = ?
			ORDER BY Number ASC
		""", [hero_name], one=False)
	if len(skills) == 0:
		skills = {"Result": "None"}
	else:
		skills = {"Result": "OK", "Content": skills}
	return json.dumps(skills)


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


@app.route('/hero/<hero_name>/_edit', methods=['GET', 'POST'])
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
			return render_template("hero_edit.html", **entry)
		else:
			entry["IsNew"] = "False"
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


@app.route('/hero/<hero_name>/skills_edit', methods=['GET', 'POST'])
def skills_edit(hero_name):
	if request.method == "GET":
		entry = query_db("SELECT * FROM Heroes WHERE Name = ? LIMIT 1",
			[hero_name], one=True)
		if entry == None:
			return "There is no such hero so that you cannot edit this hero's skills"
		else:
			skills = query_db("SELECT * FROM Skills WHERE HeroName = ?",
				[hero_name], one=False)
			if skills == None:
				pass
			else:
				pass


def connect_db():
	return sqlite3.connect(os.path.join(
		os.path.dirname(__file__), app.config['DATABASE']))


def query_db(query, args=(), one=False):
	cur = g.db.execute(query, args)
	rv = [dict((cur.description[idx][0], value)
		for idx, value in enumerate(row)) for row in cur.fetchall()]
	return (rv[0] if rv else None) if one else rv

if __name__ == '__main__':
	app.run()
