import numpy as np

class KronosTokenizer:
    """Financial data များကို sequence tokens အဖြစ် ပြောင်းလဲပေးသည့် Tokenizer"""
    def __init__(self, sequence_length=10):
        self.sequence_length = sequence_length

    def tokenize(self, data):
        """Array ကို LSTM သို့မဟုတ် Transformer အတွက် ပြင်ဆင်ခြင်း"""
        if len(data) < self.sequence_length:
            # တိုနေပါက padding လုပ်ပေးခြင်း
            return np.pad(data, (self.sequence_length - len(data), 0), 'constant')
        return data[-self.sequence_length:]

    def encode_market_state(self, set_idx, val):
        """ဈေးကွက်အခြေအနေကို feature vector တစ်ခုအဖြစ် ပြောင်းလဲခြင်း"""
        return np.array([set_idx, val, (set_idx / val) if val != 0 else 0])

if __name__ == "__main__":
    tokenizer = KronosTokenizer()
    print("Kronos Tokenizer is operational.")
