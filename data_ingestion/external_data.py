import datetime

def get_trading_calendar():
    """၂၀၂၅ ခုနှစ်အတွက် ဈေးကွက်ဖွင့်ရက်များကို တွက်ချက်ထုတ်ပေးခြင်း"""
    start = datetime.date(2025, 1, 1)
    end = datetime.date(2025, 12, 31)
    
    # ထိုင်းစတော့ဈေးကွက်နှင့် မြန်မာ့ရုံးပိတ်ရက်များ (နမူနာ)
    holidays = [
        datetime.date(2025, 1, 1),
        datetime.date(2025, 2, 12),
        datetime.date(2025, 4, 7),
        datetime.date(2025, 4, 14),
        datetime.date(2025, 4, 15),
        datetime.date(2025, 5, 1),
        datetime.date(2025, 5, 5),
        datetime.date(2025, 5, 12),
        datetime.date(2025, 6, 3),
        datetime.date(2025, 7, 10),
        datetime.date(2025, 7, 28),
        datetime.date(2025, 8, 12),
        datetime.date(2025, 10, 13),
        datetime.date(2025, 10, 23),
        datetime.date(2025, 12, 5),
        datetime.date(2025, 12, 10),
        datetime.date(2025, 12, 31),
    ]
    
    trading_days = []
    current = start
    while current <= end:
        # Weekday < 5 ဆိုသည်မှာ တနင်္လာမှ သောကြာအထိ (စနေ၊ တနင်္ဂနွေ မပါ)
        if current.weekday() < 5 and current not in holidays:
            trading_days.append(current.isoformat())
        current += datetime.timedelta(days=1)
        
    return trading_days

if __name__ == "__main__":
    days = get_trading_calendar()
    print(f"Total Trading Days in 2025: {len(days)}")
    # ပထမ ၅ ရက်ကို စမ်းသပ်ထုတ်ကြည့်ခြင်း
    print(f"First 5 days: {days[:5]}")
