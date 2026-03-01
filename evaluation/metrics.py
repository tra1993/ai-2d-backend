import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def calculate_performance_metrics(y_true, y_pred):
    """ခန့်မှန်းချက်များ၏ တိကျမှုကို တိုင်းတာသည့် metrics များတွက်ချက်ခြင်း"""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    
    # Hit Rate (ဂဏန်းအကွက် တည့်တည့်မှန်ကန်မှု ရာခိုင်နှုန်း)
    hits = np.sum(np.round(y_true) == np.round(y_pred))
    hit_rate = (hits / len(y_true)) * 100
    
    return {
        "MAE": mae,
        "RMSE": rmse,
        "HitRate": f"{hit_rate:.2f}%"
    }

if __name__ == "__main__":
    print("Metrics evaluation module ready.")
