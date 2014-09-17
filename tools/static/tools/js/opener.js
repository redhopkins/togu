$( document ).ready(function() {
    $('.open_popup').click(function() {
        var popup_id = $('#' + $(this).attr("rel"));
        $(popup_id).show();
        $('.overlay').show();
    })
    $('.close, .overlay').click(function() {
        $('.overlay, .popup').hide();
    })
})
