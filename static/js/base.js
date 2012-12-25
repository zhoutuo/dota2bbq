$(document).ready(function(){
	var href = window.location.pathname;
	$(".nav").children('li').removeClass('active')
		.find('a[href="' + href.toLowerCase() + '"]').parent().addClass('active');
});


function validate(object){
	var username = object.elements['username'].value;
	var password = object.elements['password'].value;
}