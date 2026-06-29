import streamlit as st

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(
    page_title="Quantum Converter",
    page_icon="📐",
    layout="centered"
)

# 2. PREMIUM CSS ENJEKSİYONU (Tüm sistemi siyah yapan sihirli kısım)
st.markdown("""
<style>
    /* Üst bar, menü ve logoları gizle */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* ANA PLAN: Tüm ekranı derin OLED siyahı yap */
    [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
    }
    
    /* Yazı Tipleri ve Genel Renkler (Göz yormayan mat gümüş) */
    h1, h2, h3, p, span, label, div {
        color: #CCCCCC !important;
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Başlık Alanı Tasarımı */
    .premium-title {
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        color: #D4AF37 !important; /* Şampanya Altını */
        letter-spacing: 5px;
        margin-top: -1rem;
        margin-bottom: 5px;
        text-transform: uppercase;
        font-size: 26px;
    }
    
    .premium-subtitle {
        text-align: center;
        font-size: 11px;
        color: #555555 !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 3rem;
    }
    
    /* Girdileri Keskin Köşeli ve Mat Siyah Yap (Endüstriyel Cihaz Hissiyatı) */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div {
        background-color: #080808 !important;
        border: 1px solid #222222 !important;
        border-radius: 1px !important; /* Keskin köşeler */
        box-shadow: none !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Aktif/Seçili Kutularda Altın Rengi Parlama Efekti */
    div[data-baseweb="select"] > div:hover, 
    div[data-baseweb="input"] > div:hover,
    div[data-baseweb="input"] > div:focus-within {
        border-color: #D4AF37 !important;
    }
    
    /* Açılır menü listelerinin içini de siyah yap */
    div[data-baseweb="popover"] ul {
        background-color: #080808 !important;
        border: 1px solid #222222 !important;
    }
    
    /* SONUÇ KARTI (Ölçüm Cihazı Ekranı) */
    .result-card {
        background-color: #050505;
        border: 1px solid #151515;
        border-top: 2px solid #D4AF37; /* Üstte altın çizgi accent */
        padding: 30px;
        border-radius: 2px;
        text-align: center;
        margin-top: 3rem;
    }
    
    .result-label {
        color: #444444 !important;
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 12px;
    }
    
    /* Monospace dijital font */
    .result-value {
        font-size: 3.2rem;
        font-family: 'Courier New', Courier, monospace; 
        color: #FFFFFF !important;
        font-weight: 700;
        letter-spacing: -1px;
    }
    
    .result-unit {
        color: #D4AF37 !important;
        font-size: 1.3rem;
        font-family: 'Helvetica Neue', sans-serif;
        margin-left: 10px;
        font-weight: 300;
    }
</style>
""", unsafe_allow_html=True)

# 3. BAŞLIKLAR
st.markdown("<div class='premium-title'>QUANTUM CONVERTER</div>", unsafe_allow_html=True)
st.markdown("<div class='premium-subtitle'>Mühendislik Standartlarında Hassas Ölçüm</div>", unsafe_allow_html=True)

# 4. DÖNÜŞTÜRME SEÇENEKLERİ VE MANTIĞI
kategori = st.selectbox("DÖNÜŞTÜRÜLECEK BOYUT", ["UZUNLUK", "KÜTLE", "SICAKLIK"])

# Birim Sözlükleri ve Hesaplama Mantığı
if kategori == "UZUNLUK":
    birimler = ["Metre (m)", "Kilometre (km)", "Mil (mi)", "İnç (in)", "Ayak (ft)"]
    carpanlar = {"Metre (m)": 1.0, "Kilometre (km)": 1000.0, "Mil (mi)": 1609.344, "İnç (in)": 0.0254, "Ayak (ft)": 0.3048}
elif kategori == "KÜTLE":
    birimler = ["Kilogram (kg)", "Gram (g)", "Pound (lb)", "Ons (oz)"]
    carpanlar = {"Kilogram (kg)": 1.0, "Gram (g)": 0.001, "Pound (lb)": 0.45359237, "Ons (oz)": 0.028349523}
else: # SICAKLIK
    birimler = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]

# 5. INPUT TASARIMI (Arayüz Kolonları)
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    deger = st.number_input("GİRİŞ DEĞERİ", value=1.0000, format="%.4f")

with col2:
    from_unit = st.selectbox("KAYNAK", birimler)

with col3:
    to_unit = st.selectbox("HEDEF", birimler)

# 6. HESAPLAMA MOTORU
if kategori in ["UZUNLUK", "KÜTLE"]:
    # Standart referans birime (m veya kg) çevir, sonra hedefe böl
    baz_deger = deger * carpanlar[from_unit]
    sonuc = baz_deger / carpanlar[to_unit]
else:
    # Sıcaklık için özel doğrusal formüller
    if from_unit == to_unit:
        sonuc = deger
    elif from_unit == "Celsius (°C)" and to_unit == "Fahrenheit (°F)":
        sonuc = (deger * 9/5) + 32
    elif from_unit == "Celsius (°C)" and to_unit == "Kelvin (K)":
        sonuc = deger + 273.15
    elif from_unit == "Fahrenheit (°F)" and to_unit == "Celsius (°C)":
        sonuc = (deger - 32) * 5/9
    elif from_unit == "Fahrenheit (°F)" and to_unit == "Kelvin (K)":
        sonuc = (deger - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin (K)" and to_unit == "Celsius (°C)":
        sonuc = deger - 273.15
    elif from_unit == "Kelvin (K)" and to_unit == "Fahrenheit (°F)":
        sonuc = (deger - 273.15) * 9/5 + 32

# 7. ÖLÇÜM CİHAZI EKRANI ÇIKTISI
st.markdown(f"""
    <div class="result-card">
        <div class="result-label">SİSTEM ÇIKTISI (OUTPUT)</div>
        <div class="result-value">{sonuc:,.4f}<span class="result-unit">{to_unit.split(' ')[0]}</span></div>
    </div>
""", unsafe_allow_html=True)
