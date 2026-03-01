import pandas as pd
import os

class HistoricalLearner:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists(self.csv_path):
                # skiprows=[0] ထည့်ခြင်းဖြင့် Header စာသား Error ကို ဖြေရှင်းသည်
                self.df = pd.read_csv(self.csv_path, header=None, skiprows=lambda x: x == 0)
                self.df.columns = ['date', 'time', 'set', 'value', 'twod', 'extra1', 'extra2']
                
                # String ထဲက comma တွေနဲ့ quote တွေကို ရှင်းထုတ်ပြီး float ပြောင်းခြင်း
                self.df['set'] = self.df['set'].astype(str).str.replace('"', '').str.replace(',', '').astype(float)
                self.df['twod'] = self.df['twod'].astype(str).str.split('.').str[0].str.zfill(2)
                
                print(f"Engine Success: {len(self.df)} records loaded correctly.")
        except Exception as e:
            print(f"Data Load Error: {e}")

    def get_target_lock(self, current_set):
        if self.df is None or self.df.empty:
            return {"type": "CALCULATING", "digit": "..."}

        # လက်ရှိ SET ရဲ့ ဒသမကိန်းနဲ့ အနီးစပ်ဆုံး Pattern ကို ရှာသည်
        curr_decimal = round(current_set % 1, 2)
        matched = self.df[self.df['set'].apply(lambda x: round(x % 1, 2)) == curr_decimal]
        
        if not matched.empty:
            most_frequent_2d = matched['twod'].value_counts().idxmax()
            return {"type": "HEAD", "digit": most_frequent_2d[0]}
        else:
            # Pattern အသစ်အတွက် ကျိန်းသေသော တွက်ချက်မှု
            digit = str(int(current_set * 100))[-1]
            return {"type": "TAIL", "digit": digit}
