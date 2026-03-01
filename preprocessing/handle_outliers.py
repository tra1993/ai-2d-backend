import numpy as np

def handle_outliers(df, columns):
    """Z-score အသုံးပြု၍ Outliers များကို ကန့်သတ်ခြင်း"""
    for col in columns:
        mean = df[col].mean()
        std = df[col].std()
        
        # 3 Standard Deviations ထက်ကျော်သော တန်ဖိုးများကို ကန့်သတ်သည်
        lower_limit = mean - 3 * std
        upper_limit = mean + 3 * std
        
        df[col] = np.clip(df[col], lower_limit, upper_limit)
        
    return df

if __name__ == "__main__":
    print("Outlier management module ready.")
