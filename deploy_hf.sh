#!/bin/bash

# ၁။ Git ကို စတင်ပြင်ဆင်ခြင်း
echo "⚙️  Initializing Git and Branching..."
git init
git branch -m main

# ၂။ Git LFS သတ်မှတ်ခြင်း (ဖိုင်ကြီးများအတွက်)
echo "📦 Setting up Git LFS for Model Weights..."
git lfs install
git lfs track "*.pth"
git lfs track "*.npy"
git lfs track "*.h5"
git lfs track "*.pkl"
git lfs track "data.csv"
git add .gitattributes

# ၃။ မလိုအပ်သောဖိုင်များကို ဖယ်ထုတ်ရန် .gitignore စစ်ဆေးခြင်း
# venv နှင့် __pycache__ တို့ကို မတင်မိအောင် ကာကွယ်ခြင်း
if [ ! -f .gitignore ]; then
  echo "venv/" > .gitignore
  echo "__pycache__/" >> .gitignore
  echo "*.log" >> .gitignore
  echo ".DS_Store" >> .gitignore
fi

# ၄။ ဖိုင်အားလုံးကို Add လုပ်ပြီး Commit ပြုလုပ်ခြင်း
echo "📝 Committing files..."
git add .
git commit -m "Complete Backend Deployment with Trained Weights (Kronos-v1) And Fixed Prediction 2d Result Output"

# ၅။ Remote URL ကို အသစ်ပြန်သတ်မှတ်ခြင်း
echo "🔗 Connecting to Hugging Face..."
git remote remove origin 2>/dev/null
git remote add origin https://huggingface.co/spaces/thura93-gpt/ai-2d-backend

# ၆။ Git Push ပြုလုပ်ခြင်း
echo "🚀 Hugging Face သို့ Push လုပ်နေသည်..."
echo "⚠️  Hugging Face Token တောင်းပါက သင်၏ Access Token (Write) ကို ထည့်ပေးပါ။"

# Git Buffer ကို တိုးမြှင့်ခြင်း (ဖိုင်ကြီးများတင်ရလွယ်ကူစေရန်)
git config http.postBuffer 524288000

git push -u origin main --force

echo "✅ Deployment Process Finished!"
