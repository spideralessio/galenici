(function($){
$(function(){
    $(".button-collapse").sideNav();
    $.ajax({
        method: "GET",
        url: "",
        dataType: "json",
        data: {  }
        success: function (res) {
            $('input.autocomplete').autocomplete({
                data: res,
                limit: 20,
                minLength: 2
            });
        } 
    });
}); // end of document ready
})(jQuery); // end of jQuery name space