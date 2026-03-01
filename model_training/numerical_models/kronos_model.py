import torch
import torch.nn as nn

class KronosModel(nn.Module):
    def __init__(self, input_size=10, hidden_size=64):
        super(KronosModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 2) # Output: [SET, VALUE]
        
    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

def load_kronos():
    # Kronos Model ကို load လုပ်သည့် function
    model = KronosModel()
    # model.load_state_dict(torch.load('model_training/weights/kronos_v1.pth'))
    model.eval()
    return model
