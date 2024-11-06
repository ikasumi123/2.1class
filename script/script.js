function password() {
    var pw1;
    var pw2;
    
    // ユーザー名の入力を繰り返し求める
    do {
        pw1 = prompt("ユーザー名を入力してください", "");
        if (pw1 != 'ikasumi') {
            alert('登録されていないユーザーです');
        }
    } while (pw1 != 'ikasumi');
    
    // ユーザー名が正しければ、パスワードの入力を繰り返し求める
    do {
        pw2 = prompt("パスワードを入れて下さい。", "");
        if (pw2 != '2.1-game') {
            alert("パスワードが違います！");
        }
    } while (pw2 != '2.1-game');
    
    // 正しいユーザー名とパスワードが入力された場合、ページ遷移
    location.href = "2.1class.html";
}
