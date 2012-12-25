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
			var item_name = window.location.hash.substring(1);
			var item = $(".item > img[src$='" + item_name + ".png']");
			if(item === null)
			{
				$notification.find('p').html('There is no such item');
				$notification.modal('show');
			}
			else
			{

			}
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
}

