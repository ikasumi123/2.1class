from flask import Flask, request
import requests

app = Flask(__name__)

# Line Notifyのアクセストークン
LINE_NOTIFY_TOKEN = 'YOUR_LINE_NOTIFY_TOKEN'

def send_line_notify(message):
    """
    Line Notifyを使用して通知を送信する関数
    """
    headers = {
        'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}',
    }
    payload = {
        'message': message,
    }
    response = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=payload)
    return response

@app.route('/')
def index():
    """
    ユーザーがサイトにアクセスしたときにIPアドレスを取得し、Lineに通知するエンドポイント
    """
    # ユーザーのIPアドレスを取得
    user_ip = request.remote_addr
    # メッセージを作成
    message = f"サイトにアクセスしたIPアドレス: {user_ip}"
    # Line Notifyで送信
    send_line_notify(message)
    return 'IPアドレスが通知されました。'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
