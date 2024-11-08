from flask import Flask, request
import requests

app = Flask(__name__)

# LINE Notifyのアクセストークン（ここに自分のトークンを入れる）
LINE_NOTIFY_TOKEN = 'YOUR_LINE_Xh1t6DLV6zEkFkpt5awibd9YPURzW2N8Ri7nUNumVET'

# LINE Notify APIにメッセージを送信する関数
def send_line_notify(message):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'}
    payload = {'message': message}
    response = requests.post(url, headers=headers, data=payload)
    return response.status_code

# IPアドレスを取得してLINE Notifyに送信
@app.route('/')
def index():
    # クライアントのIPアドレスを取得
    ip_address = request.remote_addr
    message = f"アクセスがありました。IPアドレス: {ip_address}"

    # LINE Notifyで通知を送信
    status_code = send_line_notify(message)

    # 成功した場合
    if status_code == 200:
        return f"IPアドレス {ip_address} が通知されました。"
    else:
        return "通知の送信に失敗しました。"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
