import pandas as pd
import requests
import os
class DataUpdater:
    def __init__(self, csv_path): self.csv_path = csv_path
    def sync_2026_data(self):
        try:
            res = requests.get("https://api.thaistock2d.com/2d_result", timeout=10)
            if res.status_code == 200:
                new_df = pd.DataFrame(res.json())
                new_df.to_csv(self.csv_path, index=False)
                return True
        except: return False
