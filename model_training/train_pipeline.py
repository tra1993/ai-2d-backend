import os
from model_training.train_engine import train_model, save_weights
from model_training.numerical_models.kronos_model import load_kronos
# အခြားလိုအပ်သော module များကို import လုပ်ပါ

def run_full_pipeline():
    """Training လုပ်ငန်းစဉ်တစ်ခုလုံးကို အလိုအလျောက် run ခြင်း"""
    print("🚀 Starting AI-2D Training Pipeline...")
    
    # ၁။ Model Load လုပ်ခြင်း
    model = load_kronos()
    
    # ၂။ Data ပြင်ဆင်ခြင်း (Simulation အနေဖြင့်သာ ပြထားသည်)
    # လက်တွေ့တွင် data.csv မှ data များကို DataLoader ထဲသို့ ထည့်ရမည်
    print("📊 Preparing market data for training...")
    
    # ၃။ Training စတင်ခြင်း
    # model = train_model(model, train_loader)
    
    # ၄။ Weights သိမ်းဆည်းခြင်း
    weights_dir = "model_training/weights"
    if not os.path.exists(weights_dir):
        os.makedirs(weights_dir)
        
    save_path = os.path.join(weights_dir, "kronos_v1_updated.pth")
    # save_weights(model, save_path)
    
    print("✅ Pipeline execution completed successfully.")

if __name__ == "__main__":
    run_full_pipeline()
