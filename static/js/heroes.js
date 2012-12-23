
$(document).ready(function(){

	$(".nav").eq(0).children('li').removeClass('active').eq(2).addClass('active');

	$(".faction a")
	.each(function(){
		$(this).children("img").eq(0).attr("title", $(this).attr("href").split("/")[2]);
	})
	.hover(
		function(e){
			var $hero_portrait = $(e.currentTarget).children("img").eq(0);
			$hero_portrait.css("border-color", "white");
		},
		function(e){
			$(e.currentTarget).children("img").eq(0).css("border-color", "black");
		}
		);

	$(document).tooltip({position: {my: "center top", at: "center bottom"}});

});