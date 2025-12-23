import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. VERİYİ OKUMA (Kitabı Açıyoruz)
# Verinin 'data/raw' klasöründe olduğunu varsayıyoruz.
# Eğer indirdiğin dosya adı farklıysa aşağıyı değiştir (örn: 'araba_verisi.csv')
dosya_yolu = 'data/raw/audi.csv' 

# Dosya var mı kontrol edelim
if os.path.exists(dosya_yolu):
    df = pd.read_csv(dosya_yolu)
    print("✅ Veri başarıyla okundu!")
else:
    print("❌ HATA: Dosya bulunamadı! Lütfen data/raw içine csv dosyasını koyduğuna emin ol.")
    exit()

# 2. VERİYİ ANLAMA (Kitabın Özetine Bakıyoruz)
print("\n--- Veri Seti Özeti ---")
print(f"Toplam Araç Sayısı: {len(df)}")
print("\nİlk 5 Satır:")
print(df.head())

# 3. GRAFİK ÇİZME (Görselleştirme) [PDF: Insightful Visualization]
# KM ve Fiyat arasındaki ilişkiyi çizelim.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='km_driven', y='selling_price', data=df, alpha=0.5)
plt.title('Kilometre vs Satış Fiyatı (Ne kadar çok KM, o kadar düşük fiyat)')
plt.xlabel('Kilometre (KM)')
plt.ylabel('Fiyat (TL)')

# 4. GRAFİĞİ KAYDETME
# Grafiği ekranda göstermek yerine dosyaya kaydedelim.
grafik_yolu = 'fiyat_km_grafigi.png'
plt.savefig(grafik_yolu)
print(f"\n✅ Grafik çizildi ve '{grafik_yolu}' olarak kaydedildi. O dosyayı açıp bakabilirsin!")

# Ortalama fiyatı da söyleyelim
ort_fiyat = df['selling_price'].mean()
print(f"\nBu veri setindeki araçların ortalama fiyatı: {ort_fiyat:.2f} TL")
