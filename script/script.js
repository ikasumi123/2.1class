function password() {
    var pw;
    pw = prompt("パスワードを入れて下さい。","");
    if (pw =='2.1-game'){
        location.href = "2.1class.html";
    } else {
    alert("パスワードが違います！");
    }
}
$(function(){
    var pagetop = $('#page-top');
    pagetop.hide();
    $(window).scroll(function () {
       if ($(this).scrollTop() > 100) {
            pagetop.fadeIn();
       } else {
            pagetop.fadeOut();
       }
    });
    pagetop.click(function () {
       $('body, html').animate({ scrollTop: 0 }, 500);
       return false;
    });
  });
