import os
import logging
from datetime import datetime

# Logs folder ဖန်တီးခြင်း
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def get_logger(name):
    """လုပ်ဆောင်ချက်များကို မှတ်တမ်းတင်ရန် Logger object ထုတ်ပေးခြင်း"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # ဖိုင်ထဲသို့ သိမ်းဆည်းမည့် format
    log_file = os.path.join(LOG_DIR, f"system_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(file_handler)
        
    return logger

if __name__ == "__main__":
    log = get_logger("UtilsTest")
    log.info("Logging system initialized.")
