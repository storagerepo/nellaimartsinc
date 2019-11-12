$(document).ready(function () {
    $("html").niceScroll({
        cursorcolor: "#424242", // change cursor color in hex
        cursoropacitymin: 0, // change opacity when cursor is inactive (scrollabar "hidden" state), range from 1 to 0
        cursoropacitymax: 1, // change opacity when cursor is active (scrollabar "visible" state), range from 1 to 0
        cursorwidth: "5px", // cursor width in pixel (you can also write "5px")
        cursorborder: "1px solid #fff", // css definition for cursor border
        cursorborderradius: "5px", // border radius in pixel for cursor
        zindex: "5000",
    });
    $('#back-top, #cart-button-top').hide();
});
$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#back-top, #cart-button-top').fadeIn();
        } else {
            $('#back-top, #cart-button-top').fadeOut();
        }
    });
    $('#back-top a').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
});
