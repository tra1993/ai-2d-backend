import json
import os
from datetime import datetime

LOG_FILE = "logs/performance_metrics.json"

def log_prediction_accuracy(session, predicted_2d, actual_2d):
    """ခန့်မှန်းချက်နှင့် အမှန်တကယ်ထွက်ဂဏန်းကို နှိုင်းယှဉ်မှတ်တမ်းတင်ခြင်း"""
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "session": session,
        "predicted": predicted_2d,
        "actual": actual_2d,
        "is_correct": predicted_2d == actual_2d
    }
    
    # Logs directory မရှိလျှင် ဆောက်ပါ
    if not os.path.exists("logs"):
        os.makedirs("logs")
        
    # ရှိပြီးသား logs များကိုဖတ်ပြီး အသစ်ထည့်ပါ
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                logs = json.load(f)
            except:
                logs = []
                
    logs.append(log_entry)
    
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
    
    print(f"📊 Performance logged for {session} session.")

if __name__ == "__main__":
    print("Performance Logging system ready.")
