import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- AYARLAR ---
dosya_yolu = 'data/raw/skoda.csv'  # Sadece bu dosyaya bakacağız

print(f"📂 '{dosya_yolu}' dosyası aranıyor...")

# 1. DOSYAYI KONTROL ET VE OKU
if os.path.exists(dosya_yolu):
    df = pd.read_csv(dosya_yolu)
    print("✅ Dosya bulundu ve okundu!")
else:
    print(f"❌ HATA: '{dosya_yolu}' bulunamadı!")
    print("Lütfen 'data/raw' klasörünün içine 'skoda.csv' isminde bir dosya olduğundan emin ol.")
    exit()

# 2. VERİYİ SENİN İSTEDİĞİN KRİTERLERE GÖRE DÜZENLEME
# Sütun isimlerini kontrol edelim (Genelde İngilizce olur: price, mileage/km, fuelType vb.)
# Skoda verisetinde genelde sütunlar şöyledir: 'year', 'price', 'mileage', 'fuelType', 'transmission'

print("\n--- İlk 5 Satır (Ham Veri) ---")
print(df.head())

# "200.000 KM'yi aşmış mı?" sütununu ekleyelim
# Not: Sütun adı 'mileage' ise onu kullanacağız.
if 'mileage' in df.columns:
    df['200k_Ustu_Mu'] = df['mileage'] > 200000
    print("\n--- KM Analizi ---")
    print(f"200.000 KM üzeri araç sayısı: {df['200k_Ustu_Mu'].sum()}")
elif 'km_driven' in df.columns: # Bazı verisetlerinde isim budur
    df['200k_Ustu_Mu'] = df['km_driven'] > 200000

# 3. GRAFİK ÇİZME (Fiyat Analizi)
# Yıl ve Fiyat arasındaki ilişkiyi görelim
plt.figure(figsize=(10, 6))

# Renklendirmeyi (hue) Vites türüne göre yapalım (Manuel/Otomatik farkını görmek için)
# Eğer sütun adı 'transmission' ise:
x_ekseni = 'year'
y_ekseni = 'price'

if x_ekseni in df.columns and y_ekseni in df.columns:
    sns.scatterplot(x=x_ekseni, y=y_ekseni, data=df, hue='transmission', alpha=0.6)
    plt.title('Skoda Araçların Yıl ve Fiyat Dağılımı')
    plt.xlabel('Model Yılı')
    plt.ylabel('Fiyat (Euro/TL)')
    plt.grid(True)
    
    # Grafiği kaydet
    kayit_ismi = 'skoda_fiyat_analizi.png'
    plt.savefig(kayit_ismi)
    print(f"\n✅ Grafik çizildi ve '{kayit_ismi}' olarak kaydedildi.")
else:
    print("⚠️ Grafik çizilemedi çünkü 'year' veya 'price' sütunları bulunamadı.")

# 4. ORTALAMA FİYATLAR (Dizel vs Benzin)
print("\n--- Yakıt Türüne Göre Ortalama Fiyatlar ---")
if 'fuelType' in df.columns and 'price' in df.columns:
    print(df.groupby('fuelType')['price'].mean())
