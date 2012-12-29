$(document).ready(function() {
	var hash = null;
	if(window.location.hash) {
		hash = window.location.hash.substring(1);
	}

	$.getJSON("/ajax/items", function(data) {
		if(data.Result == "OK") {
			for(var index in data.Content) {
				var item = data.Content[index];

				var tip = $(".item > img[src$='" + item.Name + ".png']")
				.data('id', item.IID)
				.click(setClick).tooltip({
					position: {
						my: "left center",
						at: "right center"
					},
					content: setTooltip(item)
				});

				if(hash == item.IID) {
					tip
					.css("border-color", "red")
					.tooltip('open');
				}
			}

		}
	});



});

function setClick(e) {
	if($(e.currentTarget).css('border-color') == 'rgb(255, 0, 0)') {
		$(e.currentTarget).css("border-color", "transparent");
		window.location.hash = '';
	} else {
		$(".item > img").css("border-color", "transparent");
		$(e.currentTarget).css("border-color", "rgb(255, 0, 0)");
		window.location.hash = '#' + $(e.currentTarget).data('id');
	}

}


function setTooltip(data) {
	var $display_div = $("<div/>")
	.addClass("item_tooltip")
	.append("<span>" + data.Name + "</span>");

	var $cost_span = $("<span/>")
	.append("<img src='/static/images/items/gold.png'>")
	.append(" " + data.Cost)
	.addClass("item_cost");
	$display_div.append($cost_span);

	if(data.Usage !== null) {
		$("<div/>")
		.html(data.Usage.replace(/\n/g, '<br>'))
		.addClass("item_usage")
		.appendTo($display_div);
	}

	if(data.Attributes !== null) {
		var $attrs_div = $("<div />")
		.html(data.Attributes.replace(/\n/g, '<br>'))
		.addClass("item_attr");
		$display_div.append($attrs_div);
	}

	if(data.Recipe !== "") {
		var items = data.Recipe.split("/");
		var $recipe_div = $("<div>Recipe:<br></div>");
		for(var index in items) {
			$recipe_div.append("<img src=\"/static/images/items/" + items[index] + ".png\" width='85px' height='64px'>");
		}
		$display_div.append($recipe_div);
	}

	$("<div/>")
	.html(data.Description)
	.addClass("item_description")
	.appendTo($display_div);


	var $container = $("<div />");
	return $container
	.append($display_div)
	.html();
}