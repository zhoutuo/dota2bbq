$(document).ready(function(){
	var href = window.location.pathname;
	$(".nav").children('li').removeClass('active')
		.find('a[href="' + href.toLowerCase() + '"]').parent().addClass('active');
	$('#edit_btn').click(validate);
});


function validate(){
	var href = window.location.pathname;
	var target = href.split('/')[1];
	var $notification = $('#result_window');
	if(target == 'hero')
	{
		window.location += '/_edit';
	}
	else if(target == 'items')
	{
		if(window.location.hash !== "")
		{
			var item_id = window.location.hash.substring(1);
			window.location = '/items/' + item_id + '/_edit';
		}
		else
		{
			$notification.find('p').html('Please click an item to edit');
			$notification.modal('show');
		}
	}
	else
	{
		$notification.find('p').html('This Page is not editable');
		$notification.modal('show');
	}
	return false;
}

