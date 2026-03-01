#!/bin/bash

echo "🚀 Starting Full AI Professional Backend Reconstruction..."

# 1. Backup Data
if [ -f "data.csv" ]; then
    cp data.csv data.csv.bak
    echo "✅ Data backed up."
fi

# 2. Complete Clean Slate (သိမ်းထားချင်တဲ့ ဖိုင်တွေကလွဲရင် အကုန်ဖျက်မယ်)
find . -maxdepth 1 ! -name '.git' ! -name '.' ! -name '..' ! -name 'data.csv.bak' ! -name 'master_setup.sh' -exec rm -rf {} +
echo "🧹 Old scripts and folders cleaned."

# 3. Create Professional Directory Structure
mkdir -p config data_ingestion preprocessing feature_engineering model_training/numerical_models inference utils
echo "📂 New directory structure created."

# 4. Restore Data
if [ -f "data.csv.bak" ]; then
    mv data.csv.bak data.csv
    echo "✅ Data restored."
fi

# ==========================================
# 5. GENERATE COMPONENT FILES
# ==========================================

# A. Configuration
cat > config/settings.yaml <<EOF
model:
  transformer_weight: 0.6
  xgboost_weight: 0.4
  seed: 42
paths:
  data: "data.csv"
EOF

# B. Data Ingestion Logic
cat > data_ingestion/loader.py <<EOF
import pandas as pd
import os
import requests

def load_history():
    if not os.path.exists('data.csv'): return None
    df = pd.read_csv('data.csv')
    for col in ['SET', 'Value']:
        df[col] = df[col].astype(str).str.replace(',', '').astype(float)
    if 'Modern' not in df.columns: df['Modern'] = 0.0
    if 'Internet' not in df.columns: df['Internet'] = 0.0
    return df

def get_live_data():
    try:
        r = requests.get("https://api.thaistock2d.com/live", timeout=2)
        d = r.json()
        if 'live' in d:
            s = str(d['live'].get('set','0')).replace(',','')
            v = str(d['live'].get('value','0')).replace(',','')
            return float(s if s!='--' else 0), float(v if v!='--' else 0)
    except: pass
    return 0.0, 0.0
EOF

# C. Feature Engineering Logic
cat > feature_engineering/processor.py <<EOF
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def process_features(df):
    delta = df['SET'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    df['SMA_5'] = df['SET'].rolling(window=5).mean()
    df['Volatility'] = df['SET'].rolling(window=5).std()
    df['Time_Encoded'] = df['Time'].apply(lambda x: 0 if "12:01" in str(x) else 1)
    if '2D' not in df.columns:
        df['2D'] = df.apply(lambda x: float(str(x['SET'])[-1] + str(x['Value']).split('.')[0][-1]), axis=1)
    df['Prev_2D'] = df['2D'].shift(1).fillna(0)
    df.fillna(0, inplace=True)
    return df

def get_scaler():
    return MinMaxScaler()
EOF

# D. AI Models
cat > model_training/numerical_models/transformer.py <<EOF
import tensorflow as tf
from tensorflow.keras import layers, models, Input

def create_transformer(input_shape):
    inputs = Input(shape=input_shape)
    x = layers.MultiHeadAttention(num_heads=4, key_dim=4)(inputs, inputs)
    x = layers.LayerNormalization(epsilon=1e-6)(x + inputs)
    x = layers.GlobalAveragePooling1D()(x)
    x = layers.Dense(64, activation="relu")(x)
    outputs = layers.Dense(1)(x)
    model = models.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mse")
    return model
EOF

cat > model_training/numerical_models/xgboost_logic.py <<EOF
from xgboost import XGBRegressor
def create_xgboost(seed=42):
    return XGBRegressor(n_estimators=100, max_depth=5, random_state=seed)
EOF

# E. The Inference Engine (Main Brain)
cat > inference/run_prediction.py <<EOF
import sys
import json
import numpy as np
import os
import random
import warnings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')

import tensorflow as tf
from data_ingestion.loader import load_history, get_live_data
from feature_engineering.processor import process_features, get_scaler
from model_training.numerical_models.transformer import create_transformer
from model_training.numerical_models.xgboost_logic import create_xgboost

SEED = 42
random.seed(SEED); np.random.seed(SEED); tf.random.set_seed(SEED)

try:
    modern = float(sys.argv[1]) if len(sys.argv)>1 else 0
    internet = float(sys.argv[2]) if len(sys.argv)>2 else 0
    session = sys.argv[3] if len(sys.argv)>3 else 'morning'
    prev_2d = float(sys.argv[4]) if len(sys.argv)>4 else 0
    
    time_in = 0 if session == 'morning' else 1
    
    live_set, _ = get_live_data()
    df = load_history()
    df = process_features(df)
    
    cols = ['Modern', 'Internet', 'Time_Encoded', 'Prev_2D', 'SMA_5', 'Volatility']
    X = df[cols].values
    y_set = df['SET'].values
    y_val = df['Value'].values
    
    scaler = get_scaler()
    X_scaled = scaler.fit_transform(X)
    
    last_row = df.iloc[-1]
    context_val = live_set if live_set > 0 else last_row['SMA_5']
    input_vec = np.array([[modern, internet, time_in, prev_2d, context_val, last_row['Volatility']]])
    input_scaled = scaler.transform(input_vec)
    
    X_dl = X_scaled.reshape((X_scaled.shape[0], 1, 6))
    input_dl = input_scaled.reshape((1, 1, 6))

    # Prediction Ensemble
    trans = create_transformer((1, 6))
    trans.fit(X_dl, y_set, epochs=20, verbose=0)
    p_set = trans.predict(input_dl, verbose=0)[0][0]
    
    trans.fit(X_dl, y_val, epochs=20, verbose=0)
    p_val = trans.predict(input_dl, verbose=0)[0][0]
    
    set_fmt = "{:.2f}".format(p_set)
    val_fmt = "{:.2f}".format(p_val)
    prediction = set_fmt[-1] + val_fmt.split('.')[0][-1]
    
    print(json.dumps({
        "status": "success",
        "predicted_set": set_fmt,
        "predicted_value": val_fmt,
        "prediction": prediction,
        "architecture": "Master-Pro-v1"
    }))
except Exception as e:
    print(json.dumps({"status": "error", "message": str(e)}))
EOF

# F. API Gateway (PHP)
cat > index.php <<EOF
<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Allow-Headers: Content-Type");

$input = json_decode(file_get_contents('php://input'), TRUE);
if (!$input) { echo json_encode(["status" => "error", "message" => "No input"]); exit(); }

$m = escapeshellarg(\$input['modern'] ?? 0);
$i = escapeshellarg(\$input['internet'] ?? 0);
$s = escapeshellarg(\$input['session'] ?? 'morning');
$p = escapeshellarg(\$input['prev_2d'] ?? 0);

\$command = "python3 inference/run_prediction.py \$m \$i \$s \$p 2>&1";
\$output = shell_exec(\$command);

if (preg_match('/\{.*\}/s', \$output, \$matches)) echo \$matches[0];
else echo json_encode(["status" => "error", "message" => trim(\$output)]);
?>
EOF

# G. Deployment Files
cat > requirements.txt <<EOF
numpy
pandas
scikit-learn
tensorflow-cpu
xgboost
requests
EOF

cat > Dockerfile <<EOF
FROM php:8.2-apache
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*
WORKDIR /var/www/html
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt --break-system-packages
RUN chown -R www-data:www-data /var/www/html && chmod -R 777 /var/www/html
RUN sed -i 's/80/7860/g' /etc/apache2/ports.conf /etc/apache2/sites-available/000-default.conf
EXPOSE 7860
CMD ["apache2-foreground"]
EOF

echo "✅ ALL-IN-ONE Professional Setup Finished!"
