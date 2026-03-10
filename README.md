# API ve Veri Bilimi Öğrenme(Basit Düzey) 🚀

Bu proje, Python dünyasındaki modern API geliştirme araçlarını (FastAPI) ve veri analizi kütüphanelerini (Pandas, Numpy, Matplotlib, Seaborn) öğrenmek amacıyla oluşturulmuş bir çalışma alanıdır. Veri analizi dünyasının "Hello World!" projesidir.

## 🎯 Motivasyon (Neden?)

Yazılım geliştirme sürecinde sadece kod yazmak değil, veriyi anlamlandırmak ve bu veriyi dış dünyaya açan servisler (API) oluşturmak kritik bir beceridir. Bu projenin temel amaçları:
- **FastAPI** ile hızlı ve güvenilir asenkron API'lar geliştirmeyi öğrenmek.
- **Pandas** ve **Numpy** kullanarak veri setleri üzerinde manipülasyon yapma pratiği kazanmak.
- **Matplotlib** ve **Seaborn** ile veriyi görselleştirerek anlamlı raporlar sunmak.
- Gerçek dünya verileri (Video Oyun Satışları, Trafik Verisi vb.) üzerinde analiz yaparak problem çözme yeteneğini geliştirmek.

## 📂 Dosya Yapısı

- `main.py`: FastAPI ile oluşturulmuş temel API uç noktaları (GET/POST örnekleri).
- `vgsalesanaliz.py`: Video oyun satış verileri (`vgsales.csv`) üzerinde yapılan **gelişmiş bölgesel ve yıllık analizler**.
- `trafikanaliz.py`: Trafik verileri (`trafik_verisi.csv`) üzerinden analiz yapan ve görsel rapor üreten script.
- `pandasdeneme.py` & `numpydeneme.py`: Bu kütüphanelerin temel özelliklerini test etmek için oluşturulmuş örnek scriptler.
- `requirements.txt`: Projenin çalışması için gerekli kütüphanelerin listesi.
- `vgsales.csv` & `trafik_verisi.csv`: Analizlerde kullanılan örnek veri setleri.

## 📊 Gelişmiş Analiz Özellikleri (vgsalesanaliz.py)

Projenin son aşamasında, video oyun satış verileri üzerinde bölgesel ve zamansal derinlemesine analizler yapılmıştır:

### 1. Bölgesel Satış Görselleştirme
Seaborn kütüphanesi kullanılarak 2x2 subplot yapısında 4 farklı bölge için (Japonya, Kuzey Amerika, Avrupa, Diğer) en popüler 5 oyun türü görselleştirilmiştir.
- **Renk Paletleri**: Analizlerde `magma`, `viridis`, `rocket` ve `mako` paletleri kullanılarak görsel derinlik sağlanmıştır.

### 2. Bölgesel En İyiler
Veri seti üzerinde yapılan sorgularla bölgelere göre en çok satan oyunlar ve türler belirlenmiştir:

| Bölge | En Çok Satan Oyun | En Popüler Tür |
| :--- | :--- | :--- |
| **Kuzey Amerika (NA)** | Wii Sports | Sports |
| **Avrupa (EU)** | Wii Sports | Sports |
| **Japonya (JP)** | Pokemon Red/Pokemon Blue | Role-Playing |
| **Diğer (Other)** | Grand Theft Auto: San Andreas | Action |

### 3. Yıllara Göre Tahtın Sahipleri (Best Sellers By Years)
1980'den itibaren her yılın küresel satış şampiyonları Pandasta `groupby` ve `idxmax` fonksiyonları ile analiz edilmiştir. Bazı önemli yıllar:

- **1985**: Super Mario Bros. (40.24M)
- **1989**: Tetris (30.26M)
- **1996**: Pokemon Red/Blue (31.37M)
- **2004**: GTA: San Andreas (20.81M)
- **2006**: Wii Sports (82.74M - Tüm zamanların rekoru!)
- **2013**: Grand Theft Auto V (21.40M)

## 🛠️ Kurulum

Projeyi yerelinizde çalıştırmak için şu adımları izleyebilirsiniz:

1. **Bağımlılıkları Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

2. **API Sunucusunu Başlatın:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Analiz Scriptlerini Çalıştırın:**
   ```bash
   python vgsalesanaliz.py
   ```

## 📈 Öğrenim Notları
- **Zaman Serisi Analizi**: Yıllara göre veriyi gruplayarak trendleri takip etme.
- **Veri Gruplama**: `groupby()` ve `idxmax()` fonksiyonları ile karmaşık veri setlerinden spesifik bilgiler çıkarma.
- **Görselleştirme**: Birden fazla grafiği (`plt.subplots`) tek bir pencerede düzenli şekilde sunma.
- **API Geliştirme**: Pydantic modelleri ile veri doğrulama ve asenkron işlem yönetimi.
