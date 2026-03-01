import pandas as pd
import os
import requests
from datetime import datetime, timedelta

DATA_PATH = "data.csv"
API_RESULT_URL = "https://api.your-live-2d-source.com/results" # တကယ့် API URL နဲ့ လဲရပါမယ်

def update_data_csv():
    """
    API မှ လက်ရှိ session result အထိ ယူပြီး data.csv ကို update လုပ်သည်။
    """
    if not os.path.exists(DATA_PATH):
        #data.csv မရှိရင် အသစ်ဆောက်မယ် (သို့) error ပြမယ်
        print("data.csv not found. Create initial 3-year history first.")
        return False

    # 1. Load existing data
    df = pd.read_csv(DATA_PATH)
    
    # နောက်ဆုံးပါတဲ့ ရက်စွဲကို ယူမယ်
    last_date_str = df.iloc[-1]['date']
    last_date = datetime.strptime(last_date_str, "%Y-%m-%d")

    # 2.Fetch missing results from API
    # ဥပမာ- last_date ကနေ ဒီနေ့အထိ fetching လုပ်မယ်
    today = datetime.now()
    fetch_start_date = last_date + timedelta(days=1)
    
    if fetch_start_date > today:
        print("Data is already up to date.")
        return True

    params = {
        "start_date": fetch_start_date.strftime("%Y-%m-%d"),
        "end_date": today.strftime("%Y-%m-%d")
    }

    try:
        response = requests.get(API_RESULT_URL, params=params)
        if response.status_code == 200:
            new_results = response.json() # API formats ပေါ်မူတည်ပြီး ပြင်ရနိုင်သည်
            
            # 3. Append new results to CSV
            if new_results:
                # new_results ကို DataFrame ပြောင်းပြီး columns တွေ ညှိရမယ်
                new_df = pd.DataFrame(new_results)
                # columns တွေက date, set, value, twod ဖြစ်ရမယ်
                
                updated_df = pd.concat([df, new_df], ignore_index=True)
                updated_df.to_csv(DATA_PATH, index=False)
                print(f"Successfully added {len(new_results)} new records to data.csv.")
                return True
            else:
                print("No new results found on API.")
                return True
        else:
            print(f"Failed to fetch from API. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error during data update: {e}")
        return False
