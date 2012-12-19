
$(document).ready(function(){
	$(document).tooltip({position: {my: "center top", at: "center bottom"}});


	$(".faction a")
	.each(function(){
		$(this).attr("title", $(this).attr("href").split("/")[2]);
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
});