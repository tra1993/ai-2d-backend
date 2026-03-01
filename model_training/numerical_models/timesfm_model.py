import numpy as np

class TimesFM:
    """Google TimesFM Simulation for sequence forecasting"""
    def predict(self, sequence):
        # Sequence data ကို အခြေခံပြီး next value ကို forecast လုပ်ခြင်း
        drift = np.random.normal(0, 0.5)
        return sequence[-1] + drift
