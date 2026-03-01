import os
import pandas as pd
import shutil

def setup_environment():
    print("🛠️ Setting up project environment...")
    
    # ၁။ လိုအပ်သော Folder များဆောက်ခြင်း
    folders = ['data', 'preprocessing', 'model_training/weights', 'inference', 'utils', 'logs']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

    # ၂။ ဒေတာဖိုင်ကို Sync လုပ်ခြင်း
    source = 'converted_output.csv'
    target = 'data/data.csv'
    
    if os.path.exists(source):
        print(f"📊 Processing {source}...")
        df = pd.read_csv(source)
        
        # SET နှင့် Value ကော်လံများကို သန့်ရှင်းရေးလုပ်ခြင်း
        for col in ['SET', 'Value']:
            if col in df.columns:
                # Comma များဖြုတ်ပြီး Numeric ပြောင်းခြင်း
                df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')
        
        # NaN တန်ဖိုးများရှိလျှင် ဖယ်ထုတ်ခြင်း
        df = df.dropna(subset=['SET'])
        
        df.to_csv(target, index=False)
        print(f"✅ Successfully synced and cleaned data to {target}")
        print(f"📈 Total records: {len(df)}")
    else:
        print(f"⚠️ Warning: {source} not found in current directory.")

if __name__ == "__main__":
    setup_environment()
