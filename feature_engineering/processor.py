from feature_engineering.technical_indicators import add_technical_indicators
from feature_engineering.session_features import add_session_context
from feature_engineering.macro_features import add_macro_indicators

def run_feature_pipeline(df):
    """Raw data မှ Final Features အထိ အဆင့်ဆင့် ပြောင်းလဲခြင်း"""
    print("🛠️ Running Feature Engineering Pipeline...")
    
    df = add_technical_indicators(df)
    df = add_session_context(df)
    df = add_macro_indicators(df)
    
    # AI Model အတွက် မလိုအပ်သော columns များဖြုတ်ခြင်း
    features_only = df.drop(columns=['date', 'session'], errors='ignore')
    
    return features_only

if __name__ == "__main__":
    print("Feature Processor Master is ready.")
