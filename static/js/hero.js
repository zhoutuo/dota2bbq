$(document).ready(function() {

	$hero_lore_para = $('#hero_lore_para');
	var hero_lore_content = $hero_lore_para.html();
	if(hero_lore_content.length > 1000) {

		$('#hero_full_story').find('p').html(hero_lore_content);
		$hero_lore_para.html(hero_lore_content.substr(0, 1000) + '......').attr('title', 'Click to view the whole story').click(function() {
			window.location = window.location + '#hero_full_story';
			$('#hero_full_story').modal('show');
		});
	}


	//tabs
	var hero_name = $("#hero_name").html();

	$("#skill_tabs").tabs();

	//skill tooltip based on ajax
	$(".skill")
	.each(function(){
		$('<img>')
		.attr('src', "/static/images/skills/" +
			($(this).data("hero") + '_' + $(this).data('skill'))
			.toLowerCase().replace(/ /g, '_').replace(/'/g, '').replace(/\?/g, '') +
			'.png')
		.width('128px')
		.height('128px')
		.attr('title', '')
		.prependTo($(this));
	});
	$(".skill").tooltip({
		position: {
			my: "right center",
			at: "left center",
			offset: "-20"
		},
		content: function(t) {
			var hero_name = $(this).parent().data('hero');
			var skill_index = $(this).parent().data('index');

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
});