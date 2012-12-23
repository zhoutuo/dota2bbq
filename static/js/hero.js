$(document).ready(function() {
	//shows the "EDIT" button in the navigation bar
	$("#isEditable").attr("href", $(location).attr('href') + '/_edit').css("visibility", "visible");

	$hero_lore_para = $('#hero_lore_para');
	var hero_lore_content = $hero_lore_para.html();
	if(hero_lore_content.length > 1000)
	{

		$('#hero_full_story').modal('hide').find('p').eq(0).html(hero_lore_content);

		$hero_lore_para
		.html(hero_lore_content.substr(0, 1000) + '......')
		.attr('title', 'Click to view the whole story')
		.click(function(){
			window.location = window.location + '#hero_full_story';
			$('#hero_full_story').modal('show');
		});
	}
	

	//tabs
	var hero_name = $("#hero_name").html();
	$.getJSON("/ajax/" + hero_name + "/skills", function(data) {
		if(data.Result == "OK") {
			var $tabs = $("#skill_tabs");
			var $ul = $tabs.children("ul").eq(0);
			for(i = 0; i < data.Content.length; ++i) {
				var skill = data.Content[i];
				$ul.append("<li><a href='#skill" + i + "'>" + skill.SkillName + "</a></li>");
				var $skill_div = $("<div />");
				$skill_div.addClass("skill");
				$skill_div.attr("id", "skill" + i);
				$skill_div.append("<img src='../static/images/skills/" + hero_name + "_" + (i + 1) + ".png' width='90px' height='90px' title=''>");
				$skill_div.append("<p>" + skill.Description + "</p>");
				$tabs.append($skill_div);
			}

			$tabs.tabs().css("visibility", "visible");

			//skill tooltip based on ajax
			$(".skill > img").tooltip({
				position: {
					my: "right center",
					at: "left center",
					offset: "-20"
				},
				content: function(t) {
					var tmp = $(this).attr("src").split("/")[4];
					var hero_name = tmp.split("_")[0];
					var skill_index = tmp.split("_")[1].split(".")[0];

					$.getJSON("/ajax/" + hero_name + "/" + skill_index, function(data) {
						if(data.Result == "OK") {
							data = data.Content;
							var display = "Type: " + (function() {
								if(data.Type == 1) {
									return "Active" + "<br>" + "ManaCost: " + data.ManaCost + "<br>" + "Cooldown: " + data.Cooldown + "<br>";
								} else {
									return "Passive" + "<br>";
								}
							}());
							t(display);
						} else {
							t("There is no information about this skill");
						}
					});
				}
			});
		}
	});



});