# API ve Veri Bilimi Öğrenme(Basit)🚀

Bu proje, Python dünyasındaki modern API geliştirme araçlarını (FastAPI) ve veri analizi kütüphanelerini (Pandas, Numpy, Matplotlib, Seaborn) öğrenmek amacıyla oluşturulmuş bir çalışma alanıdır. Bu projedeki her şey alanının temel yapıtaşlarına hakim olmak içindir.

## 🎯 Motivasyon (Neden?)

Yazılım geliştirme sürecinde sadece kod yazmak değil, veriyi anlamlandırmak ve bu veriyi dış dünyaya açan servisler (API) oluşturmak kritik bir beceridir. Bu projenin temel amaçları:
- **FastAPI** ile hızlı ve güvenilir asenkron API'lar geliştirmeyi öğrenmek.
- **Pandas** ve **Numpy** kullanarak veri setleri üzerinde manipülasyon yapma pratiği kazanmak.
- **Matplotlib** ve **Seaborn** ile veriyi görselleştirerek anlamlı raporlar sunmak.
- Gerçek dünya verileri (Video Oyun Satışları, Trafik Verisi vb.) üzerinde analiz yaparak problem çözme yeteneğini geliştirmek.

## 📂 Dosya Yapısı

- `main.py`: FastAPI ile oluşturulmuş temel API uç noktaları (GET/POST örnekleri).
- `vgsalesanaliz.py`: Video oyun satış verileri (`vgsales.csv`) üzerinde yapılan **gelişmiş bölgesel analizler** ve görselleştirmeler.
- `trafikanaliz.py`: Trafik verileri (`trafik_verisi.csv`) üzerinden analiz yapan ve görsel rapor üreten script.
- `pandasdeneme.py` & `numpydeneme.py`: Bu kütüphanelerin temel özelliklerini test etmek için oluşturulmuş örnek scriptler.
- `requirements.txt`: Projenin çalışması için gerekli kütüphanelerin listesi.
- `vgsales.csv` & `trafik_verisi.csv`: Analizlerde kullanılan örnek veri setleri.

## 📊 Gelişmiş Analiz Özellikleri (vgsalesanaliz.py)

Projenin son aşamasında, video oyun satış verileri üzerinde bölgesel bazda derinlemesine analizler yapılmıştır:

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
- **Veri Gruplama**: `groupby()` ve `idxmax()` fonksiyonları ile karmaşık veri setlerinden spesifik bilgiler çıkarma.
- **Görselleştirme**: Birden fazla grafiği (`plt.subplots`) tek bir pencerede düzenli şekilde sunma.
- **API Geliştirme**: Pydantic modelleri ile veri doğrulama ve asenkron işlem yönetimi.
