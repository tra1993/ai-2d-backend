import pandas as pd
from evaluation.metrics import calculate_performance_metrics

def run_backtest(model, historical_df):
    """Walk-forward validation နည်းလမ်းဖြင့် အတိတ်ဒေတာများကို ပြန်လည်စမ်းသပ်ခြင်း"""
    print("⏳ Running Backtesting with Kronos Engine...")
    
    predictions = []
    actuals = historical_df['target'].values
    
    for i in range(len(historical_df)):
        # Model ထံမှ prediction ယူခြင်း (Simulated)
        pred = model.predict(historical_df.iloc[i])
        predictions.append(pred)
    
    results = calculate_performance_metrics(actuals, predictions)
    print(f"✅ Backtest Results: {results}")
    return results

if __name__ == "__main__":
    print("Backtesting module initialized.")
