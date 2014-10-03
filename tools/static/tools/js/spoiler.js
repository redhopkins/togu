$( document ).ready(function(){
    $('.n-item').click(function(){
        $(this).parent().children('div.spoiler').toggle('normal');
        return false;
    });
})
