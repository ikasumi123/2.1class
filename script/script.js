function password() {
    while (pw != '2.1-game'){
        var pw;
        pw = prompt("パスワードを入れて下さい。","");
        if (pw =='2.1-game'){
            location.href = "2.1class.html";
        } else {
        alert("パスワードが違います！");
        }
    }
}
