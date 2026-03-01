import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

def train_model(model, train_loader, epochs=10, lr=0.001):
    """Model တစ်ခုကို ပေးထားသော data ဖြင့် သင်ကြားပေးခြင်း"""
    criterion = nn.MSELoss() # Mean Squared Error Loss
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for inputs, targets in train_loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            
        print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}")
    
    return model

def save_weights(model, path):
    """သင်ကြားပြီးသော Model ၏ weights များကို သိမ်းဆည်းခြင်း"""
    torch.save(model.state_dict(), path)
    print(f"Weights saved to {path}")

if __name__ == "__main__":
    print("Training Engine initialized and ready.")
