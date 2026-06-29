# Quantum Station Ultimate 

https://birimdonusturucu-nwysqrya6yaijdbbvxlssm.streamlit.app
**Quantum Station Ultimate**, mühendisler, bilim insanları ve yazılımcılar için geliştirilmiş, tek bir Python dosyası üzerinden çalışan premium bir birim dönüştürme ve hesaplama istasyonudur. 


---

## Temel Özellikler

* **Tek Dosya Mimarisi:** Tüm UI (Arayüz), CSS enjeksiyonu ve hesaplama motoru tek bir `app.py` dosyası içindedir.
* **Akıllı Formatlama:** Sonuçlardaki gereksiz sıfırları gizler. Tam sayılar temiz bir şekilde (`15`), küsuratlı sayılar ise maksimum hassasiyetle (`15.123456`) gösterilir.
* **Gelişmiş Hata Yakalama:** `cot(0)` gibi tanımsız trigonometrik işlemlerde veya ikilik (binary) sisteme geçersiz harf girildiğinde uygulama çökmez, şık bir hata arayüzü sunar.
* **Kapsamlı Veritabanı:** SI Temel Birimleri, Türetilmiş Mühendislik Birimleri, Mekanik ve Bilişim dâhil 21 farklı modül barındırır.

---

##  Desteklenen Modüller

Uygulama 5 ana kategori altında 21 farklı hesaplama modülü sunar:

| Kategori | İçerik |
| :--- | :--- |
| **Temel SI Birimleri** | Uzunluk, Kütle, Zaman, Elektrik Akımı, Sıcaklık, Madde Miktarı, Işık Şiddeti |
| **Fizik & Mühendislik** | Basınç, Güç, Enerji & İş, Kuvvet, Tork |
| **Mekanik & Geometri** | Hız, Hacim, Alan, Açı Dönüşümü (Radyan/Derece), Trigonometri |
| **Bilişim & Dijital** | Veri Boyutu (Byte, TB vb.), Veri İletim Hızı, Sayı Sistemleri (Hex, Bin, Oct, Dec) |
| **Otomotiv** | Yakıt Tüketimi (L/100km, km/L, MPG) |

