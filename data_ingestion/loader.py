import pandas as pd
import os

def load_csv_data(file_path="data.csv"):
    """CSV ဖိုင်မှ ဒေတာများကို DataFrame အဖြစ် ဖတ်ယူခြင်း"""
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return None
    
    df = pd.read_csv(file_path)
    # နေ့စွဲကို datetime format ပြောင်းခြင်း
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])
    
    return df

if __name__ == "__main__":
    print("Data loader module is ready.")
