<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");

// OPTIONS request အတွက် (CORS pre-flight)
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit;
}

$input = json_decode(file_get_contents('php://input'), TRUE);
if (!$input) {
    exit(json_encode([
        "status" => "error",
        "message" => "Invalid JSON input"
    ]));
}

// Arguments များကို စနစ်တကျယူခြင်း
$m = escapeshellarg($input['modern'] ?? 0);
$i = escapeshellarg($input['internet'] ?? 0);
$s = escapeshellarg($input['session'] ?? 'morning');
$p = escapeshellarg($input['prev_2d'] ?? 0);

// Python3 executable path နှင့် script path ကို သေချာစေရန်
$command = "python3 " . __DIR__ . "/inference/orchestration.py $m $i $s $p 2>&1";
$output = shell_exec($command);

// Output ထဲက JSON part ကိုပဲ ရှာဖွေဖတ်ယူခြင်း
if (preg_match('/\{.*\}/s', $output, $matches)) {
    echo $matches[0];
} else {
    // Python error ဖြစ်ခဲ့လျှင် debug message ပြန်ပေးရန်
    echo json_encode([
        "status" => "error",
        "message" => "Python Execution Failed",
        "debug" => trim($output)
    ]);
}
?>
