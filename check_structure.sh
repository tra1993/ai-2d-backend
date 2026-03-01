#!/bin/bash

# --- အရောင်သတ်မှတ်ချက်များ ---
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔍 AI-2D Master Pro: Project Integrity Inspection စတင်နေသည်...${NC}"
echo "------------------------------------------------------------"

# ၁။ လိုအပ်သော Folder များ ရှိမရှိ စစ်ဆေးခြင်း
echo -e "${YELLOW}📁 Folders စစ်ဆေးခြင်း:${NC}"
folders=(
    "model_training" 
    "model_training/weights" 
    "model_training/numerical_models" 
    "inference"
)

for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo -e "  [${GREEN}OK${NC}] Folder: $folder"
    else
        echo -e "  [${RED}MISSING${NC}] Folder: $folder"
        mkdir -p "$folder"
        echo -e "       ${BLUE}-> ဖန်တီးပေးလိုက်ပါပြီ။${NC}"
    fi
done

echo ""

# ၂။ AI Model Weights (.pth) ဖိုင်များ ရှိမရှိ စစ်ဆေးခြင်း
echo -e "${YELLOW}⚖️ AI Model Weights စစ်ဆေးခြင်း:${NC}"
weights=(
    "model_training/weights/kronos_v1.pth" 
    "model_training/weights/timesfm_base.pth"
)

for weight in "${weights[@]}"; do
    if [ -f "$weight" ]; then
        size=$(ls -lh "$weight" | awk '{print $5}')
        echo -e "  [${GREEN}FOUND${NC}] $weight ($size)"
    else
        echo -e "  [${RED}NOT FOUND${NC}] $weight"
        echo -e "       ${RED}⚠️ သတိပေးချက်: weights မရှိလျှင် AI ခန့်မှန်းချက် အလုပ်လုပ်မည်မဟုတ်ပါ။${NC}"
    fi
done

echo ""

# ၃။ Core Python Scripts များ စစ်ဆေးခြင်း
echo -e "${YELLOW}📄 Python Scripts များ စစ်ဆေးခြင်း:${NC}"
files=(
    "app.py" 
    "requirements.txt" 
    "model_training/ensemble.py" 
    "model_training/numerical_models/kronos_model.py" 
    "model_training/numerical_models/timesfm_model.py" 
    "model_training/numerical_models/gluonts_engine.py" 
    "inference/predict_daily.py"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        size=$(wc -c <"$file")
        if [ $size -gt 10 ]; then
            echo -e "  [${GREEN}OK${NC}] $file ($size bytes)"
        else
            echo -e "  [${YELLOW}EMPTY${NC}] $file (ဖိုင်ရှိသော်လည်း code မရှိပါ)"
        fi
    else
        echo -e "  [${RED}MISSING${NC}] $file"
    fi
done

echo "------------------------------------------------------------"
echo -e "${BLUE}🚀 စစ်ဆေးမှု ပြီးဆုံးပါပြီ။${NC}"
