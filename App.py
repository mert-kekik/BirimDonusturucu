import streamlit as st
import math

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(
    page_title="Quantum Converter Pro",
    page_icon="📐",
    layout="centered"
)

# 2. PREMIUM CSS ENJEKSİYONU
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
    }
    
    h1, h2, h3, p, span, label, div {
        color: #CCCCCC !important;
        font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .premium-title {
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 300;
        color: #D4AF37 !important;
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
    
    div[data-baseweb="select"] > div, 
    div[data-baseweb="input"] > div {
        background-color: #080808 !important;
        border: 1px solid #222222 !important;
        border-radius: 1px !important;
        box-shadow: none !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    div[data-baseweb="select"] > div:hover, 
    div[data-baseweb="input"] > div:hover,
    div[data-baseweb="input"] > div:focus-within {
        border-color: #D4AF37 !important;
    }
    
    div[data-baseweb="popover"] ul {
        background-color: #080808 !important;
        border: 1px solid #222222 !important;
    }
    
    .result-card {
        background-color: #050505;
        border: 1px solid #151515;
        border-top: 2px solid #D4AF37;
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
    
    .error-text {
        font-size: 2rem;
        color: #FF4444 !important;
        font-family: 'Courier New', Courier, monospace;
    }
</style>
""", unsafe_allow_html=True)

# 3. BAŞLIKLAR
st.markdown("<div class='premium-title'>QUANTUM CONVERTER PRO</div>", unsafe_allow_html=True)
st.markdown("<div class='premium-subtitle'>Tüm SI Temel Birimleri & Trigonometri Motoru</div>", unsafe_allow_html=True)

# 4. KATEGORİ SEÇİMİ
kategoriler = [
    "UZUNLUK (m)", "KÜTLE (kg)", "ZAMAN (s)", "ELEKTRİK AKIMI (A)", 
    "SICAKLIK (K)", "MADDE MİKTARI (mol)", "IŞIK ŞİDDETİ (cd)", 
    "AÇI DÖNÜŞÜMÜ (rad/°)", "TRİGONOMETRİ (sin/cos/tan/cot)"
]
kategori = st.selectbox("AKTİF MODÜL", kategoriler)

# 5. VERİ SÖZLÜKLERİ VE HESAPLAMA MANTIĞI
is_trig = False
is_undefined = False
sonuc = 0.0
to_unit_display = ""
sonuc_str = ""

if kategori == "TRİGONOMETRİ (sin/cos/tan/cot)":
    is_trig = True
    col1, col2, col3 = st.columns([1, 1, 1])
    # Burada formatı kaldırdık ki gereksiz sıfırlar görünmesin
    with col1: deger = st.number_input("AÇI DEĞERİ", value=0.0)
    with col2: aci_birimi = st.selectbox("BİRİM", ["Derece (°)", "Radyan (rad)"])
    with col3: fonk = st.selectbox("FONKSİYON", ["Sinüs (sin)", "Kosinüs (cos)", "Tanjant (tan)", "Kotanjant (cot)"])
    
    rad_deger = math.radians(deger) if aci_birimi == "Derece (°)" else deger
    
    if fonk == "Sinüs (sin)": sonuc = math.sin(rad_deger)
    elif fonk == "Kosinüs (cos)": sonuc = math.cos(rad_deger)
    elif fonk == "Tanjant (tan)":
        if math.isclose(math.cos(rad_deger), 0, abs_tol=1e-9):
            is_undefined = True; sonuc_str = "Tanımsız (∞)"
        else: sonuc = math.tan(rad_deger)
    elif fonk == "Kotanjant (cot)":
        if math.isclose(math.sin(rad_deger), 0, abs_tol=1e-9):
            is_undefined = True; sonuc_str = "Tanımsız (∞)"
        else: sonuc = 1 / math.tan(rad_deger)
        
    to_unit_display = ""

else:
    if kategori == "UZUNLUK (m)":
        birimler = ["Metre (m)", "Kilometre (km)", "Santimetre (cm)", "Milimetre (mm)", "Mil (mi)", "İnç (in)", "Ayak (ft)"]
        carpanlar = {"Metre (m)": 1.0, "Kilometre (km)": 1000.0, "Santimetre (cm)": 0.01, "Milimetre (mm)": 0.001, "Mil (mi)": 1609.344, "İnç (in)": 0.0254, "Ayak (ft)": 0.3048}
    elif kategori == "KÜTLE (kg)":
        birimler = ["Kilogram (kg)", "Gram (g)", "Miligram (mg)", "Pound (lb)", "Ons (oz)"]
        carpanlar = {"Kilogram (kg)": 1.0, "Gram (g)": 0.001, "Miligram (mg)": 0.000001, "Pound (lb)": 0.45359237, "Ons (oz)": 0.028349523}
    elif kategori == "ZAMAN (s)":
        birimler = ["Saniye (s)", "Milisaniye (ms)", "Mikrosaniye (μs)", "Dakika (min)", "Saat (h)", "Gün (d)"]
        carpanlar = {"Saniye (s)": 1.0, "Milisaniye (ms)": 0.001, "Mikrosaniye (μs)": 0.000001, "Dakika (min)": 60.0, "Saat (h)": 3600.0, "Gün (d)": 86400.0}
    elif kategori == "ELEKTRİK AKIMI (A)":
        birimler = ["Amper (A)", "Miliamper (mA)", "Mikroamper (μA)", "Kiloamper (kA)"]
        carpanlar = {"Amper (A)": 1.0, "Miliamper (mA)": 0.001, "Mikroamper (μA)": 0.000001, "Kiloamper (kA)": 1000.0}
    elif kategori == "MADDE MİKTARI (mol)":
        birimler = ["Mol (mol)", "Milimol (mmol)", "Mikromol (μmol)"]
        carpanlar = {"Mol (mol)": 1.0, "Milimol (mmol)": 0.001, "Mikromol (μmol)": 0.000001}
    elif kategori == "IŞIK ŞİDDETİ (cd)":
        birimler = ["Kandela (cd)", "Milikandela (mcd)"]
        carpanlar = {"Kandela (cd)": 1.0, "Milikandela (mcd)": 0.001}
    elif kategori == "AÇI DÖNÜŞÜMÜ (rad/°)":
        birimler = ["Derece (°)", "Radyan (rad)"]
    elif kategori == "SICAKLIK (K)":
        birimler = ["Kelvin (K)", "Celsius (°C)", "Fahrenheit (°F)"]

    col1, col2, col3 = st.columns([1, 1, 1])
    # Burada da formatı kaldırdık
    with col1: deger = st.number_input("GİRİŞ DEĞERİ", value=1.0)
    with col2: from_unit = st.selectbox("KAYNAK", birimler)
    with col3: to_unit = st.selectbox("HEDEF", birimler)
    
    to_unit_display = to_unit.split(' ')[-1].replace("(", "").replace(")", "")

    lineer_kategoriler = ["UZUNLUK (m)", "KÜTLE (kg)", "ZAMAN (s)", "ELEKTRİK AKIMI (A)", "MADDE MİKTARI (mol)", "IŞIK ŞİDDETİ (cd)"]
    
    if kategori in lineer_kategoriler:
        baz_deger = deger * carpanlar[from_unit]
        sonuc = baz_deger / carpanlar[to_unit]
        
    elif kategori == "AÇI DÖNÜŞÜMÜ (rad/°)":
        if from_unit == "Derece (°)" and to_unit == "Radyan (rad)": sonuc = math.radians(deger)
        elif from_unit == "Radyan (rad)" and to_unit == "Derece (°)": sonuc = math.degrees(deger)
        else: sonuc = deger

    elif kategori == "SICAKLIK (K)":
        if from_unit == to_unit: sonuc = deger
        elif from_unit == "Celsius (°C)" and to_unit == "Fahrenheit (°F)": sonuc = (deger * 9/5) + 32
        elif from_unit == "Celsius (°C)" and to_unit == "Kelvin (K)": sonuc = deger + 273.15
        elif from_unit == "Fahrenheit (°F)" and to_unit == "Celsius (°C)": sonuc = (deger - 32) * 5/9
        elif from_unit == "Fahrenheit (°F)" and to_unit == "Kelvin (K)": sonuc = (deger - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin (K)" and to_unit == "Celsius (°C)": sonuc = deger - 273.15
        elif from_unit == "Kelvin (K)" and to_unit == "Fahrenheit (°F)": sonuc = (deger - 273.15) * 9/5 + 32

# 6. AKILLI FORMATLAMA VE ÇIKTI EKRANI
if is_undefined:
    html_output = f"""
        <div class="result-card">
            <div class="result-label">SİSTEM ÇIKTISI (HATA)</div>
            <div class="error-text">{sonuc_str}</div>
        </div>
    """
else:
    # --- YENİ EKLENEN AKILLI FORMATLAMA MANTIĞI ---
    # Eğer sayı 15.0 gibi bir tam sayıysa direkt "15" yap
    if float(sonuc).is_integer():
        gosterilecek_sonuc = f"{int(sonuc):,}"
    else:
        # Değilse maksimum 6 hane göster ama sağdaki gereksiz sıfırları ve varsa boşta kalan noktayı temizle
        gosterilecek_sonuc = f"{sonuc:,.6f}".rstrip('0').rstrip('.')
        
    html_output = f"""
        <div class="result-card">
            <div class="result-label">{'FONKSİYON SONUCU' if is_trig else 'SİSTEM ÇIKTISI (OUTPUT)'}</div>
            <div class="result-value">{gosterilecek_sonuc}<span class="result-unit">{to_unit_display}</span></div>
        </div>
    """

st.markdown(html_output, unsafe_allow_html=True)
