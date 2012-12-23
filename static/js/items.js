$(document).ready(function() {

	$(".nav").eq(0).children('li').removeClass('active').eq(4).addClass('active');

	var hash = null;
	if(window.location.hash)
	{
		hash = window.location.hash.substring(1);
	}

	$.getJSON("/ajax/items", function(data) {
		if(data.Result == "OK")
		{
			for(var index in data.Content) {
				var item = data.Content[index];
				
				var tip = $(".item > img[src$='" + item.Name + ".png']").tooltip({
					position: {my: "left center", at: "right center"},
					content: setTooltip(item)
				});

				if(hash == item.Name)
				{
					tip.css("border-color", "red").tooltip('open');
				}
			}

		}
	});



});


function setTooltip(data) {
	var $display_div = $("<div/>")
	.addClass("item_tooltip")
	.append("<span>" + data.Name + "</span>");

	var $cost_span = $("<span/>")
	.append("<img src='../static/images/items/gold.png'>")
	.append(" " + data.Cost)
	.addClass("item_cost");
	$display_div.append($cost_span);

	if(data.Usage !== null)
	{
		$("<div/>").html(data.Usage)
		.addClass("item_usage")
		.appendTo($display_div);
	}

	if(data.Attributes !== null)
	{
		var attrs = data.Attributes.split("/");
		var $attrs_div = $("<div />").addClass("item_attr");
		for(var i = 0; i < attrs.length; ++i)
		{
			$attrs_div.append(attrs[i]);
			if(i != attrs.length - 1)
			{
				$attrs_div.append("<br>");
			}

		}
		$display_div.append($attrs_div);
	}

	if(data.Recipe !== null)
	{
		var items = data.Recipe.split("/");
		var $recipe_div = $("<div>Recipe:<br></div>");
		for(var index in items)
		{
			$recipe_div.append("<img src=\"../static/images/items/" + items[index] + ".png\" width='85px' height='64px'>");
		}
		$display_div.append($recipe_div);
	}

	$("<div/>").html(data.Description)
	.addClass("item_description")
	.appendTo($display_div);


	var $container = $("<div />");
	return $container.append($display_div).html();
}