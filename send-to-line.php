<?php
// LINE Notifyのアクセストークンを設定
$access_token = 'YOUR_LINE_NOTIFY_ACCESS_TOKEN';  // 自分のアクセストークンに置き換えてください

// POSTデータを受け取る
$data = json_decode(file_get_contents('php://input'), true);
$ip = $data['ip'];

// LINE NotifyのAPIエンドポイント
$api_url = 'https://notify-api.line.me/api/notify';

// メッセージの内容
$message = "新しいIPアドレスがアクセスしました: " . $ip;

// cURLでPOSTリクエストを送信
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $api_url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query(['message' => $message]));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $access_token
]);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

// 結果を返す
echo json_encode(['status' => 'success']);
?>
