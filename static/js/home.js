$(document).ready(function() {
    $.getJSON("/ajax/combined", function(data) {
        $("#search_input").autocomplete({
            minLength: 2,
            delay: 500,
            source: function(request, response) {
                var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(request.term), "i");
                var results = $.grep(data, function(item) {
                    return matcher.test(item.Name);
                });
                response(results);
            },
            open: function(event, ui) {
                $(".ui-autocomplete").css({
                    'width': '300px'
                });
            },
            select: function(event, ui) {
                if(ui.item.Class == 'Hero') {
                    $(location).attr("href", "/hero/" + ui.item.Name);
                } else {
                    $(location).attr("href", "/items#" + ui.item.ID);
                }

            }
        }).data("autocomplete")._renderItem = function(ul, item) {
            return $("<li>").data("item.autocomplete", item).append("<a><span style='display: inline-block;width: 220px;'>" + item.Name + "</span>" + item.Class + "</a>").appendTo(ul);
        };

    });

});