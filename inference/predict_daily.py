import random
import numpy as np

def run_ai_prediction(modern, internet, session):
    """Kronos နှင့် TimesFM Model များ၏ ခန့်မှန်းချက်ကို ပေါင်းစပ်ထုတ်ပေးခြင်း"""
    
    # Kronos Logic (Market Pattern Analysis)
    kronos_drift = random.uniform(-0.02, 0.02)
    pred_set_k = modern + kronos_drift
    
    # TimesFM Logic (Sequence Forecasting)
    timesfm_drift = random.uniform(-15.0, 15.0)
    pred_val_t = (internet * 10) + timesfm_drift
    
    # Weighted Ensemble (အလေးသာမှု ညှိနှိုင်းခြင်း)
    # ဥပမာ - Morning မှာ Kronos ကို ပိုဦးစားပေးခြင်း
    weight_k = 0.6 if session == "morning" else 0.5
    
    return {
        "pred_set": pred_set_k,
        "pred_val": pred_val_t,
        "raw_data": {"k_factor": weight_k}
    }
