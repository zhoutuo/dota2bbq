$(document).ready(function(){
	$("#Faction_Select").val($("#Faction_Select").data('select'));
	$("#PrimaryAttr_Select").val($("#PrimaryAttr_Select").data('select'));

	var hero_name = $('#hero_name').val();
	$('.update_skill').click(function(){
		var $container = $(this).parent();
		var skill_num = $container.find('.skill_number').val();
		var skill_type = $container.find('.skill_type').is(':checked')? 1 : 0;

		$.ajax({
			url: '/ajax/' + hero_name + '/' + skill_num,
			data: {
				"skill_name": $container.find('.skill_name').val(),
				"skill_desc": $container.find('.skill_desc').html(),
				"skill_type": skill_type,
				"skill_manacost": $container.find('.skill_manacost').val(),
				"skill_cooldown": $container.find('.skill_cooldown').val()
			},
			type: 'PUT',
			dataType: 'json',
			success: function(data){
				alert(data.Content);
			},
			error: function(){
				alert('fails to connect to the server');
			}
		});
	});


	$('.delete_skill').click(function(){
		var $container = $(this).parent();
		var skill_num = $container.find('.skill_number').val();
		$.ajax({
			url: '/ajax/' + hero_name + '/' + skill_num,
			type: 'DELETE',
			dataType: 'json',
			success: function(data){
				alert(data.Content);
				$container.remove();
			},
			error: function(){
				alert('fails to connect to the server');
			}
		});
	});


	$('#create_skill').click(function(){
		var $container = $(this).parent();
		var skill_num = $container.find('.skill_number').val();

		if(!$.isNumeric(skill_num))
		{
			alert('skill number should be an unsigned integer');
			return;
		}

		var skill_type = $container.find('.skill_type').is(':checked')? 1 : 0;

		$.ajax({
			url: '/ajax/' + hero_name + '/' + skill_num,
			data: {
				"skill_name": $container.find('.skill_name').val(),
				"skill_desc": $container.find('.skill_desc').html(),
				"skill_type": skill_type,
				"skill_manacost": $container.find('.skill_manacost').val(),
				"skill_cooldown": $container.find('.skill_cooldown').val()
			},
			type: 'POST',
			dataType: 'json',
			success: function(data){
				alert(data.Content);
				if(data.Result == 'OK')
				{
					location.reload();
				}
				
			},
			error: function(){
				alert('fails to connect to the server');
			}
		});
	});

	$('#close_btn').click(function(){
		window.location = "/hero/" + hero_name;
	});


});