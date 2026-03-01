import pandas as pd

def add_session_context(df):
    """Session အလိုက် ထူးခြားသော လက္ခဏာများကို ထည့်သွင်းခြင်း"""
    # Morning = 0, Evening = 1
    df['is_evening'] = df['session'].apply(lambda x: 1 if x.lower() == 'evening' else 0)
    
    # အပတ်စဉ် ရက်များ (0=Monday, 4=Friday)
    df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek
    
    # လကုန်ရက် နီးကပ်မှု (Payday effect စစ်ဆေးရန်)
    df['is_month_end'] = pd.to_datetime(df['date']).dt.is_month_end.astype(int)
    
    return df

if __name__ == "__main__":
    print("Session context features ready.")
