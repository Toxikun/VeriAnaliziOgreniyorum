# API ve Veri Bilimi Öğrenme Günlüğü 🚀

Bu proje, Python dünyasındaki modern API geliştirme araçlarını (FastAPI) ve veri analizi kütüphanelerini (Pandas, Numpy, Matplotlib, Seaborn) öğrenmek amacıyla oluşturulmuş bir çalışma alanıdır.

## 🎯 Motivasyon (Neden?)

Yazılım geliştirme sürecinde sadece kod yazmak değil, veriyi anlamlandırmak ve bu veriyi dış dünyaya açan servisler (API) oluşturmak kritik bir beceridir. Bu projenin temel amaçları:
- **FastAPI** ile hızlı ve güvenilir asenkron API'lar geliştirmeyi öğrenmek.
- **Pandas** ve **Numpy** kullanarak veri setleri üzerinde manipülasyon yapma pratiği kazanmak.
- **Matplotlib** ve **Seaborn** ile veriyi görselleştirerek anlamlı raporlar sunmak.
- Gerçek dünya verileri (Video Oyun Satışları, Trafik Verisi vb.) üzerinde analiz yaparak problem çözme yeteneğini geliştirmek.

## 📂 Dosya Yapısı

- `main.py`: FastAPI ile oluşturulmuş temel API uç noktaları (GET/POST örnekleri).
- `vgsalesanaliz.py`: Video oyun satış verileri (`vgsales.csv`) üzerinde yapılan ilk analizler ve görselleştirme denemeleri.
- `trafikanaliz.py`: Trafik verileri (`trafik_verisi.csv`) üzerinden analiz yapan ve görsel rapor üreten script.
- `pandasdeneme.py` & `numpydeneme.py`: Bu kütüphanelerin temel özelliklerini test etmek için oluşturulmuş örnek scriptler.
- `requirements.txt`: Projenin çalışması için gerekli kütüphanelerin listesi.
- `vgsales.csv` & `trafik_verisi.csv`: Analizlerde kullanılan örnek veri setleri.

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
   python trafikanaliz.py
   ```

## 📈 Öğrenim Notları
Bu süreçte; API'larda tip güvenliği (Pydantic), veri temizleme (NaN değerlerin yönetimi) ve veriyi görselleştirirken dikkat edilmesi gereken grafik türleri hakkında pratik tecrübeler edinilmiştir.
