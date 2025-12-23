# Dosya Yolu: src/data_ingest.py

import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import os

print("Veri indirme işlemi başlıyor...")

# 1. Senin attığın kod bloğu: Veriyi Kaggle'dan çeker
# Not: Bu veri seti birden fazla araba markasını (Audi, BMW, Ford vb.) içeriyor olabilir.
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "adityadesai13/used-car-dataset-ford-and-mercedes",
  # Dosya yolu belirtilmezse genelde tüm csvleri ya da ana csvyi getirmeye çalışır
  # Hata almamak için kütüphanenin indirdiği yeri kullanıp birleştirme yapabiliriz
)

# Eğer df bir sözlük (dictionary) dönerse (çoklu dosya varsa), bunları birleştirelim
if isinstance(df, dict):
    print("Birden fazla dosya bulundu, hepsi birleştiriliyor...")
    df = pd.concat(df.values(), ignore_index=True)

print("Veri başarıyla indirildi!")
print("İlk 5 kayıt:", df.head())

# 2. ÖNEMLİ KISIM: Veriyi 'data/raw' klasörüne kaydetmek
# PDF kuralı: Ham veriler data klasöründe olmalı[cite: 45].

# Üst klasöre çıkıp data/raw yolunu bulalım
save_path = os.path.join("..", "data", "raw", "araba_verisi.csv")

# Klasör yoksa oluştur
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# CSV olarak kaydet
df.to_csv(save_path, index=False)
print(f"Veri şuraya kaydedildi: {save_path}")
