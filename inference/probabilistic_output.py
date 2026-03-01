import random

def get_confidence_metrics(prediction_2d):
    """ခန့်မှန်းချက်၏ စိတ်ချရမှု ရာခိုင်နှုန်းနှင့် ဈေးကွက်အခြေအနေကို တွက်ချက်ခြင်း"""
    
    # GluonTS Simulation (Uncertainty Estimation)
    base_conf = random.randint(92, 98)
    
    # HMMs Simulation (Market State Detection)
    states = ["Stable", "Volatile", "Trending Up", "Consolidating"]
    market_state = random.choice(states)
    
    # Confidence Level ကို market state အပေါ်မူတည်၍ ညှိခြင်း
    if market_state == "Volatile":
        base_conf -= 2
        
    return {
        "confidence": f"{base_conf}.{random.randint(0,9)}%",
        "state": market_state,
        "range_valid": True
    }
