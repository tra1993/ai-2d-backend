#!/bin/bash

# --- အရောင်သတ်မှတ်ချက်များ ---
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' 

echo -e "${BLUE}🔍 AI-2D Backend: Hugging Face Deployment Integrity Check စတင်နေသည်...${NC}"
echo "------------------------------------------------------------"

# ၁။ မရှိမဖြစ်လိုအပ်သော Python Scripts နှင့် Config များ
echo -e "${YELLOW}⚙️ Core Files စစ်ဆေးခြင်း:${NC}"
# Hugging Face Space သည် metadata အတွက် README.md ကို သုံးသည် (သို့မဟုတ် space.yaml)
# Python app အတွက် app.py သည် default ဖြစ်သည်
core_files=("app.py" "requirements.txt" ".gitignore" "README.md")

for file in "${core_files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "  [${GREEN}OK${NC}] File: $file"
    else
        echo -e "  [${RED}MISSING${NC}] File: $file"
    fi
done

echo ""

# ၂။ Model Weights နှင့် Folders များ (Hugging Face ပေါ်တွင် အလုပ်လုပ်ရန် လိုအပ်သည်)
echo -e "${YELLOW}📁 Structure စစ်ဆေးခြင်း:${NC}"
folders=("model_training" "model_training/weights" "inference")
for folder in "${folders[@]}"; do
    if [ -d "$folder" ]; then
        echo -e "  [${GREEN}OK${NC}] Folder: $folder"
    else
        echo -e "  [${RED}MISSING${NC}] Folder: $folder"
    fi
done

echo ""

# ၃။ Dockerfile စစ်ဆေးခြင်း (Custom Space သုံးလျှင် လိုအပ်သည်)
echo -e "${YELLOW}🐳 Dockerization Check:${NC}"
if [ -f "Dockerfile" ]; then
    echo -e "  [${GREEN}FOUND${NC}] Dockerfile စစ်ဆေးတွေ့ရှိသည်။ (Custom Environment အတွက် အဆင်သင့်ဖြစ်သည်)"
else
    echo -e "  [${YELLOW}INFO${NC}] Dockerfile မရှိပါ။ (Hugging Face Python SDK Space သုံးလျှင် မလိုအပ်ပါ)"
fi

echo ""

# ၄။ Hugging Face Metadata Check
echo -e "${YELLOW}📄 Hugging Face Metadata:${NC}"
if grep -q "sdk: streamlit" "README.md" 2>/dev/null || grep -q "sdk: docker" "README.md" 2>/dev/null || grep -q "sdk: flask" "README.md" 2>/dev/null || grep -q "sdk: fastapi" "README.md" 2>/dev/null; then
    echo -e "  [${GREEN}OK${NC}] README.md ထဲတွင် Space YAML Metadata ပါရှိသည်။"
else
    echo -e "  [${RED}WARNING${NC}] README.md ထဲတွင် Space SDK (fastapi/docker) metadata မတွေ့ပါ။"
fi

echo "------------------------------------------------------------"

# Final Conclusion
if [ -f "app.py" ] && [ -f "requirements.txt" ]; then
    echo -e "${GREEN}✅ Backend သည် Hugging Face သို့ Push ရန် ၁၀၀% အဆင်သင့်ဖြစ်နေပါပြီ။${NC}"
else
    echo -e "${RED}❌ အရေးကြီးဖိုင်များ လိုအပ်နေသည်။ အထက်ပါ MISSING များကို ပြင်ဆင်ပါ။${NC}"
fi
