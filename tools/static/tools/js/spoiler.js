$( document ).ready(function(){
    $('.n-item').click(function(){
        $(this).parent().children('p.spoiler').toggle('normal');
        return false;
    });
})
