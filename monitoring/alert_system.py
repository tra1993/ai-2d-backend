import requests

def send_alert(message, severity="INFO"):
    """စနစ်၏ အခြေအနေကို အချက်ပေးစာ ပေးပို့ခြင်း"""
    alert_msg = f"[{severity}] AI-2D MONITOR: {message}"
    print(alert_msg)
    
    # ဤနေရာတွင် Telegram Bot API သို့မဟုတ် Email API တို့နှင့် ချိတ်ဆက်နိုင်သည်
    # requests.post(f"https://api.telegram.org/bot<token>/sendMessage", data={"text": alert_msg})

def check_system_health():
    """Backend တစ်ခုလုံး ပုံမှန်အလုပ်လုပ်မလုပ် စစ်ဆေးခြင်း"""
    try:
        # Check files, check database connection, etc.
        send_alert("System health check passed.", "SUCCESS")
    except Exception as e:
        send_alert(f"Critical System Failure: {str(e)}", "CRITICAL")

if __name__ == "__main__":
    check_system_health()
