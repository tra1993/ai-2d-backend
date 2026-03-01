import sys
import json
import random
import hashlib
import numpy as np
from datetime import datetime
from inference.predict_daily import run_ai_prediction
from inference.probabilistic_output import get_confidence_metrics

def extract_2d(set_val, val_val):
    """SET Index decimal last + Value integer last logic"""
    try:
        set_str = "{:.2f}".format(float(set_val))
        first_digit = set_str[-1]
        val_int_str = str(int(float(val_val)))
        last_digit = val_int_str[-1]
        return first_digit + last_digit
    except:
        return "--"

def set_fixed_seed(session):
    """တစ်နေ့တာ၏ session အလိုက် အဖြေကို lock ချခြင်း"""
    today_str = datetime.now().strftime("%Y-%m-%d")
    seed_str = f"{today_str}-{session}-MASTER-V3.5"
    seed_val = int(hashlib.sha256(seed_str.encode()).hexdigest(), 16) % (2**32)
    np.random.seed(seed_val)
    random.seed(seed_val)

def main():
    try:
        # PHP သို့မဟုတ် Python Arguments လက်ခံခြင်း
        modern = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
        internet = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
        session = sys.argv[3] if len(sys.argv) > 3 else "morning"

        set_fixed_seed(session)

        # AI Prediction ရယူခြင်း
        ai_raw = run_ai_prediction(modern, internet, session)
        
        # Logic အသုံးပြု၍ 2D ထုတ်ယူခြင်း
        final_2d = extract_2d(ai_raw['pred_set'], ai_raw['pred_val'])
        
        # ဖြစ်နိုင်ခြေ metrics များရယူခြင်း
        metrics = get_confidence_metrics(final_2d)

        result = {
            "status": "success",
            "prediction": final_2d,
            "set_index": "{:.2f}".format(ai_raw['pred_set']),
            "value": "{:.2f}".format(ai_raw['pred_val']),
            "confidence": metrics['confidence'],
            "architecture": "Kronos+TimesFM Hybrid",
            "analysis": f"Market state: {metrics['state']}. Sentiment analysis complete."
        }
        print(json.dumps(result))

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))

if __name__ == "__main__":
    main()
