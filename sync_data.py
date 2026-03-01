import os
import pandas as pd

def clean_and_sync():
    source = 'converted_output.csv'
    target_dir = 'data'
    target_file = os.path.join(target_dir, 'data.csv')

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    if os.path.exists(source):
        df = pd.read_csv(source)
        # SET နှင့် Value ကော်လံများမှ comma များဖြုတ်ပြီး float ပြောင်းခြင်း
        for col in ['SET', 'Value']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace(',', '').astype(float)
        
        df.to_csv(target_file, index=False)
        print(f"✅ Data processed and saved to {target_file}")
    else:
        print(f"❌ {source} not found!")

if __name__ == "__main__":
    clean_and_sync()
