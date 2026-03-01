import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import pickle
import os

def scale_features(df, save_scaler=True):
    """Data များကို normalize လုပ်ပြီး scaler ဖိုင်ကို သိမ်းဆည်းခြင်း"""
    scaler = MinMaxScaler(feature_range=(0, 1))
    
    # Feature scaling လုပ်မည့် column များ (ဥပမာ SET, VALUE, MODERN)
    cols_to_scale = [col for col in df.columns if df[col].dtype in ['float64', 'int64']]
    
    df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
    
    if save_scaler:
        # kronos_scaler.pkl အဖြစ် သိမ်းဆည်းသည်
        scaler_path = os.path.join(os.path.dirname(__file__), 'kronos_scaler.pkl')
        with open(scaler_path, 'wb') as f:
            pickle.dump(scaler, f)
            
    return df, scaler

if __name__ == "__main__":
    print("Feature scaling and normalization script ready.")
