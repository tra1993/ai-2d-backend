def check_overfitting(train_loss, val_loss, threshold=0.1):
    """Training loss နှင့် Validation loss ကို နှိုင်းယှဉ်၍ Overfitting စစ်ဆေးခြင်း"""
    gap = abs(train_loss - val_loss)
    
    if gap > threshold:
        print(f"⚠️ Warning: Overfitting detected! Gap: {gap:.4f}")
        return True
    
    print("✅ Model generalization looks healthy.")
    return False

if __name__ == "__main__":
    print("Overfitting check module operational.")
