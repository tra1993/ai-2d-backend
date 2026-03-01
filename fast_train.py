import torch
import torch.nn as nn
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import MinMaxScaler

# 1. Directory တည်ဆောက်ခြင်း
weights_dir = "model_training/weights"
if not os.path.exists(weights_dir):
    os.makedirs(weights_dir)

# Neural Network Architecture
class KronosLite(nn.Module):
    def __init__(self, input_size):
        super(KronosLite, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 2) 
        )
    
    def forward(self, x):
        return self.network(x)

def clean_numeric(value):
    """ကော်မာပါသော စာသားများကို ကိန်းဂဏန်းအဖြစ် ပြောင်းလဲခြင်း"""
    if isinstance(value, str):
        return float(value.replace(',', ''))
    return float(value)

def run_fast_training():
    print("📂 Loading and Preprocessing CSV data...")
    try:
        df = pd.read_csv("data.csv")
        
        # Column names များကို သန့်စင်ခြင်း
        df.columns = df.columns.str.strip()
        
        print(f"✅ Columns found: {list(df.columns)}")

        # SET နှင့် Value column များမှ ကော်မာများကို ဖယ်ထုတ်ပြီး Float ပြောင်းခြင်း
        df['SET'] = df['SET'].apply(clean_numeric)
        df['Value'] = df['Value'].apply(clean_numeric)
        
        # အခြားလိုအပ်သော column များ (2D, Modern စသည်)
        df['2D'] = pd.to_numeric(df['2D'], errors='coerce').fillna(0)
        df['Modern'] = pd.to_numeric(df['Modern'], errors='coerce').fillna(0)

        # Feature Selection
        # SET, Value, Modern တို့ကို Input အဖြစ် သုံးပါမည်
        feature_cols = ['SET', 'Value', 'Modern']
        print(f"🛠️ Using features: {feature_cols}")

        features = df[feature_cols].values
        # Target သည် နောက်တစ်ကြိမ်ထွက်မည့် SET နှင့် Value ဖြစ်သည်
        target = df[['SET', 'Value']].shift(-1).ffill().values 

        # Scaling
        scaler = MinMaxScaler()
        features_scaled = scaler.fit_transform(features)
        
        X = torch.tensor(features_scaled, dtype=torch.float32)
        y = torch.tensor(target, dtype=torch.float32)

        # 3. Training စတင်ခြင်း
        model = KronosLite(input_size=len(feature_cols))
        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.005)

        print("🚀 Training in progress (Fast Mode)...")
        epochs = 200
        for epoch in range(epochs):
            model.train()
            optimizer.zero_grad()
            outputs = model(X)
            loss = criterion(outputs, y)
            loss.backward()
            optimizer.step()
            
            if (epoch+1) % 40 == 0:
                print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.6f}")

        # 4. Weights သိမ်းဆည်းခြင်း
        torch.save(model.state_dict(), os.path.join(weights_dir, "kronos_v1.pth"))
        torch.save(model.state_dict(), os.path.join(weights_dir, "timesfm_base.pth"))
        
        print("\n✅ Training Complete!")
        print(f"💾 Weights saved to: {weights_dir}/kronos_v1.pth")

    except Exception as e:
        print(f"❌ Error during training: {str(e)}")

if __name__ == "__main__":
    run_fast_training()
