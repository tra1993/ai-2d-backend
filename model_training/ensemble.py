import numpy as np

class AIEnsemble:
    """မတူညီသော AI Model များ၏ ရလဒ်များကို ပေါင်းစပ်ပေးသည့် Layer"""
    def __init__(self, model_weights=None):
        # Default weights: Kronos (0.6), TimesFM (0.4)
        self.weights = model_weights if model_weights else {'kronos': 0.6, 'timesfm': 0.4}

    def combine_predictions(self, kronos_pred, timesfm_pred):
        """Weighted Average အသုံးပြု၍ အကောင်းဆုံးရလဒ်ကို တွက်ချက်ခြင်း"""
        # Pred format: [SET, VALUE]
        final_set = (kronos_pred[0] * self.weights['kronos']) + (timesfm_pred[0] * self.weights['timesfm'])
        final_val = (kronos_pred[1] * self.weights['kronos']) + (timesfm_pred[1] * self.weights['timesfm'])
        
        return np.array([final_set, final_val])

    def adjust_weights_by_market(self, market_state):
        """ဈေးကွက်အခြေအနေအလိုက် Model များ၏ အလေးသာမှုကို ပြောင်းလဲခြင်း"""
        if market_state == "Volatile":
            self.weights = {'kronos': 0.4, 'timesfm': 0.6} # TimesFM က ရေတိုမှာ ပိုကောင်းသည်
        else:
            self.weights = {'kronos': 0.7, 'timesfm': 0.3}

if __name__ == "__main__":
    ensemble = AIEnsemble()
    print("AI Ensemble System is ready to merge predictions.")
