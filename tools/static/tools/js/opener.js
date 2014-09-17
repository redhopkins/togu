$( document ).ready(function() {
    $('.open_popup').click(function() {
        $("#popup1").find("td")[1].innerText = $(this).children("span")[0].innerText;
        $("#popup1").find("td")[3].innerText = $(this).children("span")[1].innerText;
        $("#popup1").find("td")[5].innerText = $(this).children("span")[2].innerText;
        $("#popup1").find("td")[7].innerText = $(this).children("span")[3].innerText;

        $("#popup1").find("p")[0].innerText = $(this).find("h3")[0].innerText;
        $($("#popup1").find("img")[1]).attr("src", $(this).children("img").attr('src'));
        
        var popup_id = $('#' + $(this).attr("rel"));

        $(popup_id).show();
        $('.overlay').show();
    })
    $('.close, .overlay').click(function() {
        $('.overlay, .popup').hide();
    })
})
