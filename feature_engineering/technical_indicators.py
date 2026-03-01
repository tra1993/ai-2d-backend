import pandas as pd
import numpy as np

def add_technical_indicators(df):
    """ဈေးကွက်၏ အရှိန်အဟုန်ကို တိုင်းတာသည့် indicators များထည့်သွင်းခြင်း"""
    # ၁။ Simple Moving Average (SMA) - ၅ ရက်စာ ပျှမ်းမျှ
    df['sma_5'] = df['set'].rolling(window=5).mean()
    
    # ၂။ Relative Strength Index (RSI) - အဝယ်လွန်/အရောင်းလွန် တိုင်းတာခြင်း
    delta = df['set'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / (loss + 1e-9)
    df['rsi'] = 100 - (100 / (1 + rs))
    
    # ၃။ Volatility - ဈေးနှုန်းအတက်အကျ ကြမ်းမှုနှုန်း
    df['volatility'] = df['set'].rolling(window=5).std()
    
    return df.fillna(0)

if __name__ == "__main__":
    print("Technical indicators module is ready.")
