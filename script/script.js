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
fetch('https://api.ipify.org?format=json')
.then(response => response.json()) // APIのレスポンスをJSONとして解析
.then(data => { // 解析されたデータを受け取る
  console.log("Your IP address is: " + data.ip); // IPアドレスをコンソールに表示
});
