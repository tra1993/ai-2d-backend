import numpy as np
import pandas as pd

def check_data_drift(new_data, historical_mean, threshold=0.15):
    """ဈေးကွက်ဒေတာများ ပုံမှန်မဟုတ်ဘဲ လွဲချော်သွားခြင်း ရှိမရှိ စစ်ဆေးခြင်း"""
    current_mean = np.mean(new_data)
    drift_score = abs(current_mean - historical_mean) / (historical_mean + 1e-9)
    
    if drift_score > threshold:
        return True, drift_score
    return False, drift_score

def monitor_market_shift(df_new):
    """လက်ရှိ SET Index ပုံစံများကို စောင့်ကြည့်ခြင်း"""
    # ဥပမာ - SET index ၏ ပျှမ်းမျှတန်ဖိုးကို နှိုင်းယှဉ်ခြင်း
    # drift_detected, score = check_data_drift(df_new['set'].values, 1200.0)
    # return drift_detected
    pass

if __name__ == "__main__":
    print("Data Drift Detection module initialized.")
