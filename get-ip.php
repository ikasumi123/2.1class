<?php
// ユーザーのIPアドレスを取得
$ip = $_SERVER['REMOTE_ADDR'];

// 結果をJSON形式で返す
header('Content-Type: application/json');
echo json_encode(['ip' => $ip]);
?>
