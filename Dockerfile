FROM python:3.9

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# .py မပါဘဲ 'app:app' လို့ပဲ သုံးရပါမယ်
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]
