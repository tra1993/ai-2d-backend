import pandas as pd
import numpy as np

def clean_data(df):
    """Missing values များကို သန့်စင်ပေးခြင်း"""
    # Numerical column များရှိ NaN တန်ဖိုးများကို ရှေ့ဂဏန်းဖြင့် ဖြည့်ခြင်း (Forward Fill)
    df = df.ffill()
    
    # ကျန်ရှိနေသေးသော NaN များကို mean တန်ဖိုးဖြင့် အစားထိုးခြင်း
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].mean())
        
    return df

if __name__ == "__main__":
    print("Data cleaning module initialized.")
