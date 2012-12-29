var timeroutID = 0;
$(document).ready(function() {
	$(".hero a").hover(

	function(e) {
		var $hero_portrait = $(e.currentTarget).children("img");
		$hero_portrait.css("border-color", "white");
	}, function(e) {
		$(e.currentTarget).children("img").css("border-color", "black");
	});

	$('#filter_by_class').change(filter);
	$('#filter_by_faction').change(filter);
	$('#filter_by_name').keyup(delayNameFiltering);
	$('#sort_by_name').change(sort);
	$('.hero_browse')
	.sortable(
		{
			revert: true,
			connectWith: '#dustbin'
		});

	$('#dustbin')
	.sortable({
			receive: function(event, ui){
				$(ui.item).remove();
				$('#dustbin > h1').show();
			},
			over: function(event, ui){
				$('#dustbin > h1').hide();
			}
});

});

function delayNameFiltering() {
	window.clearTimeout(timeroutID);
	timeroutID = window.setTimeout(filter, 500);
}

function filter() {
	var cur_class = $('#filter_by_class').val();
	var cur_faction = $('#filter_by_faction').val();
	var cur_name_prefix = $('#filter_by_name').val();
	if(cur_name_prefix === '') {
		cur_name_prefix = 'all';
	}
	$('div.hero')
	.hide()
	.filter('[data-class*=' + cur_class + ']')
	.filter('[data-faction*=' + cur_faction + ']')
	.filter('[data-name*=' + cur_name_prefix + ']')
	.show('slow');

}

function sort() {
	var cur_val = parseInt($('#sort_by_name').val(), 10);
	if(cur_val !== 0) {
		$('div.hero:visible')
		.hide()
		.sort(function(a, b) {
			return cur_val * cmp($(a).data('name'), $(b).data('name'));
		})
		.appendTo($('.hero_browse'))
		.show('fast');
	}
}

function cmp(a, b)
{
	if(a > b)
	{
		return -1;
	}
	else if(a == b)
	{
		return 0;
	}
	else
	{
		return 1;
	}
}