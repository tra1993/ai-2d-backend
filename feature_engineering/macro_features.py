def add_macro_indicators(df, exchange_rate=35.5):
    """နိုင်ငံတကာ စီးပွားရေး အပြောင်းအလဲများကို ထည့်သွင်းခြင်း"""
    # USD/THB ငွေလဲနှုန်း အကျိုးသက်ရောက်မှု
    df['currency_impact'] = df['set'] / exchange_rate
    
    # နိုင်ငံတကာ စတော့ဈေးကွက် (ဥပမာ Dow Jones) နှင့် ဆက်စပ်မှု (Simulated)
    df['global_trend'] = df['set'] * 0.001 
    
    return df

if __name__ == "__main__":
    print("Macro-economic features module ready.")
