FROM python:3.9-slim

WORKDIR /app

# Gereksinimleri yükleyin
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama dosyalarını kopyalayın
COPY . .

# Uygulamayı çalıştırın
CMD ["python", "app.py"]
