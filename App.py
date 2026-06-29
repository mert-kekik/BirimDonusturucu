import streamlit as st
import math

# 1. SAYFA YAPILANDIRMASI
st.set_page_config(
    page_title="Quantum Station Ultimate",
    page_icon="📐",
    layout="wide" # Çok fazla kategori olduğu için geniş görünüm daha iyi durur
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
        margin-top: -3rem;
        margin-bottom: 5px;
        text-transform: uppercase;
        font-size: 28px;
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
        border-radius: 2px !important;
        box-shadow: none !important;
        transition: all 0.4s ease;
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
        border-radius: 4px;
        text-align: center;
        margin-top: 3rem;
    }
    
    .result-label {
        color: #444444 !important;
        font-size: 11px;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 15px;
    }
    
    .result-value {
        font-size: 3.5rem;
        font-family: 'Courier New', Courier, monospace; 
        color: #FFFFFF !important;
        font-weight: 700;
        letter-spacing: -1px;
        word-wrap: break-word;
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
st.markdown("<div class='premium-title'>QUANTUM STATION ULTIMATE</div>", unsafe_allow_html=True)
st.markdown("<div class='premium-subtitle'>Merkezi Mühendislik ve Bilimsel Dönüşüm İstasyonu</div>", unsafe_allow_html=True)

# 4. KATEGORİ LİSTESİ (21 Modül)
kategoriler = [
    "--- TEMEL BİRİMLER (SI) ---",
    "UZUNLUK (m)", "KÜTLE (kg)", "ZAMAN (s)", "ELEKTRİK AKIMI (A)", "SICAKLIK (K)", "MADDE MİKTARI (mol)", "IŞIK ŞİDDETİ (cd)",
    "--- FİZİK & MÜHENDİSLİK ---",
    "BASINÇ (Pa)", "GÜÇ (W)", "ENERJİ & İŞ (J)", "KUVVET (N)", "TORK (Nm)",
    "--- MEKANİK & MEKANSAL ---",
    "HIZ (m/s)", "HACİM (L)", "ALAN (m²)", "AÇI DÖNÜŞÜMÜ (rad/°)", "TRİGONOMETRİ (sin/cos/tan/cot)",
    "--- BİLİŞİM & DİJİTAL ---",
    "VERİ BOYUTU (Byte)", "VERİ İLETİMİ (bps)", "SAYI SİSTEMLERİ",
    "--- OTOMOTİV ---",
    "YAKIT TÜKETİMİ"
]

# Ayırıcı metinleri seçilemez yapmak mantıklı olmadığından, eğer seçilirse default bir yere atlatıyoruz.
secilen = st.selectbox("AKTİF MODÜL", kategoriler)
kategori = "UZUNLUK (m)" if secilen.startswith("---") else secilen

# 5. KONTROL DEĞİŞKENLERİ
is_trig = False
is_undefined = False
is_text_output = False
sonuc = 0.0
to_unit_display = ""
sonuc_str = ""

# 6. SÖZLÜKLER VE HESAPLAMA MOTORU
if kategori == "SAYI SİSTEMLERİ":
    # Sayı sistemleri metin (string) girdisi gerektirir.
    is_text_output = True
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1: deger_str = st.text_input("GİRİŞ DEĞERİ", value="10")
    with col2: from_unit = st.selectbox("KAYNAK", ["Onluk (Decimal)", "İkilik (Binary)", "Sekizlik (Octal)", "On altılık (Hex)"])
    with col3: to_unit = st.selectbox("HEDEF", ["Onluk (Decimal)", "İkilik (Binary)", "Sekizlik (Octal)", "On altılık (Hex)"])
    
    to_unit_display = " " + to_unit.split(' ')[0]
    try:
        if from_unit == "Onluk (Decimal)": base_10 = int(deger_str, 10)
        elif from_unit == "İkilik (Binary)": base_10 = int(deger_str, 2)
        elif from_unit == "Sekizlik (Octal)": base_10 = int(deger_str, 8)
        elif from_unit == "On altılık (Hex)": base_10 = int(deger_str, 16)
        
        if to_unit == "Onluk (Decimal)": sonuc_str = str(base_10)
        elif to_unit == "İkilik (Binary)": sonuc_str = bin(base_10)[2:]
        elif to_unit == "Sekizlik (Octal)": sonuc_str = oct(base_10)[2:]
        elif to_unit == "On altılık (Hex)": sonuc_str = hex(base_10)[2:].upper()
    except ValueError:
        is_undefined = True; sonuc_str = "HATA (Geçersiz Karakter)"

elif kategori == "TRİGONOMETRİ (sin/cos/tan/cot)":
    is_trig = True
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1: deger = st.number_input("AÇI DEĞERİ", value=0.0)
    with col2: aci_birimi = st.selectbox("BİRİM", ["Derece (°)", "Radyan (rad)"])
    with col3: fonk = st.selectbox("FONKSİYON", ["Sinüs (sin)", "Kosinüs (cos)", "Tanjant (tan)", "Kotanjant (cot)"])
    
    rad_deger = math.radians(deger) if aci_birimi == "Derece (°)" else deger
    
    if fonk == "Sinüs (sin)": sonuc = math.sin(rad_deger)
    elif fonk == "Kosinüs (cos)": sonuc = math.cos(rad_deger)
    elif fonk == "Tanjant (tan)":
        if math.isclose(math.cos(rad_deger), 0, abs_tol=1e-9): is_undefined = True; sonuc_str = "Tanımsız (∞)"
        else: sonuc = math.tan(rad_deger)
    elif fonk == "Kotanjant (cot)":
        if math.isclose(math.sin(rad_deger), 0, abs_tol=1e-9): is_undefined = True; sonuc_str = "Tanımsız (∞)"
        else: sonuc = 1 / math.tan(rad_deger)
    to_unit_display = ""

else:
    # STANDART VE TÜRETİLMİŞ BİRİMLER SÖZLÜĞÜ
    if kategori == "UZUNLUK (m)":
        birimler, carpanlar = ["Metre (m)", "Kilometre (km)", "Santimetre (cm)", "Milimetre (mm)", "Mil (mi)", "İnç (in)", "Ayak (ft)"], {"Metre (m)": 1.0, "Kilometre (km)": 1000.0, "Santimetre (cm)": 0.01, "Milimetre (mm)": 0.001, "Mil (mi)": 1609.344, "İnç (in)": 0.0254, "Ayak (ft)": 0.3048}
    elif kategori == "KÜTLE (kg)":
        birimler, carpanlar = ["Kilogram (kg)", "Gram (g)", "Miligram (mg)", "Pound (lb)", "Ons (oz)"], {"Kilogram (kg)": 1.0, "Gram (g)": 0.001, "Miligram (mg)": 0.000001, "Pound (lb)": 0.45359237, "Ons (oz)": 0.028349523}
    elif kategori == "ZAMAN (s)":
        birimler, carpanlar = ["Saniye (s)", "Milisaniye (ms)", "Dakika (min)", "Saat (h)", "Gün (d)"], {"Saniye (s)": 1.0, "Milisaniye (ms)": 0.001, "Dakika (min)": 60.0, "Saat (h)": 3600.0, "Gün (d)": 86400.0}
    elif kategori == "ELEKTRİK AKIMI (A)":
        birimler, carpanlar = ["Amper (A)", "Miliamper (mA)", "Kiloamper (kA)"], {"Amper (A)": 1.0, "Miliamper (mA)": 0.001, "Kiloamper (kA)": 1000.0}
    elif kategori == "MADDE MİKTARI (mol)":
        birimler, carpanlar = ["Mol (mol)", "Milimol (mmol)"], {"Mol (mol)": 1.0, "Milimol (mmol)": 0.001}
    elif kategori == "IŞIK ŞİDDETİ (cd)":
        birimler, carpanlar = ["Kandela (cd)", "Milikandela (mcd)"], {"Kandela (cd)": 1.0, "Milikandela (mcd)": 0.001}
    elif kategori == "BASINÇ (Pa)":
        birimler, carpanlar = ["Pascal (Pa)", "Bar", "Atmosfer (atm)", "PSI", "mmHg"], {"Pascal (Pa)": 1.0, "Bar": 100000.0, "Atmosfer (atm)": 101325.0, "PSI": 6894.76, "mmHg": 133.322}
    elif kategori == "GÜÇ (W)":
        birimler, carpanlar = ["Watt (W)", "Kilowatt (kW)", "HP (Metrik)", "HP (Mekanik)"], {"Watt (W)": 1.0, "Kilowatt (kW)": 1000.0, "HP (Metrik)": 735.49875, "HP (Mekanik)": 745.699872}
    elif kategori == "ENERJİ & İŞ (J)":
        birimler, carpanlar = ["Joule (J)", "Kilokalori (kcal)", "BTU", "Kilowatt-saat (kWh)"], {"Joule (J)": 1.0, "Kilokalori (kcal)": 4184.0, "BTU": 1055.06, "Kilowatt-saat (kWh)": 3600000.0}
    elif kategori == "KUVVET (N)":
        birimler, carpanlar = ["Newton (N)", "Pound-kuvvet (lbf)", "Kilogram-kuvvet (kgf)"], {"Newton (N)": 1.0, "Pound-kuvvet (lbf)": 4.44822, "Kilogram-kuvvet (kgf)": 9.80665}
    elif kategori == "TORK (Nm)":
        birimler, carpanlar = ["Newton-metre (Nm)", "Pound-foot (lb-ft)"], {"Newton-metre (Nm)": 1.0, "Pound-foot (lb-ft)": 1.355818}
    elif kategori == "HIZ (m/s)":
        birimler, carpanlar = ["Metre/saniye (m/s)", "Kilometre/saat (km/h)", "Mil/saat (mph)", "Knot", "Mach"], {"Metre/saniye (m/s)": 1.0, "Kilometre/saat (km/h)": 0.277778, "Mil/saat (mph)": 0.44704, "Knot": 0.514444, "Mach": 343.0}
    elif kategori == "HACİM (L)":
        birimler, carpanlar = ["Litre (L)", "Metreküp (m³)", "US Galon", "UK Galon", "Sıvı Ons (fl oz)"], {"Litre (L)": 1.0, "Metreküp (m³)": 1000.0, "US Galon": 3.78541, "UK Galon": 4.54609, "Sıvı Ons (fl oz)": 0.0295735}
    elif kategori == "ALAN (m²)":
        birimler, carpanlar = ["Metrekare (m²)", "Hektar (ha)", "Dönüm", "Acre", "İnçkare (sq in)"], {"Metrekare (m²)": 1.0, "Hektar (ha)": 10000.0, "Dönüm": 1000.0, "Acre": 4046.86, "İnçkare (sq in)": 0.00064516}
    elif kategori == "VERİ BOYUTU (Byte)":
        birimler, carpanlar = ["Byte (B)", "Kilobyte (KB)", "Megabyte (MB)", "Gigabyte (GB)", "Terabyte (TB)"], {"Byte (B)": 1.0, "Kilobyte (KB)": 1024.0, "Megabyte (MB)": 1048576.0, "Gigabyte (GB)": 1073741824.0, "Terabyte (TB)": 1099511627776.0}
    elif kategori == "VERİ İLETİMİ (bps)":
        birimler, carpanlar = ["bit/saniye (bps)", "Kilobit/saniye (Kbps)", "Megabit/saniye (Mbps)", "Gigabit/saniye (Gbps)", "Megabyte/saniye (MB/s)"], {"bit/saniye (bps)": 1.0, "Kilobit/saniye (Kbps)": 1000.0, "Megabit/saniye (Mbps)": 1000000.0, "Gigabit/saniye (Gbps)": 1000000000.0, "Megabyte/saniye (MB/s)": 8000000.0}
    elif kategori == "AÇI DÖNÜŞÜMÜ (rad/°)":
        birimler = ["Derece (°)", "Radyan (rad)"]
    elif kategori == "SICAKLIK (K)":
        birimler = ["Kelvin (K)", "Celsius (°C)", "Fahrenheit (°F)"]
    elif kategori == "YAKIT TÜKETİMİ":
        birimler = ["L/100km", "Kilometre/Litre (km/L)", "Mil/Galon (MPG US)"]

    # Ortak UI
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1: deger = st.number_input("GİRİŞ DEĞERİ", value=1.0)
    with col2: from_unit = st.selectbox("KAYNAK", birimler)
    with col3: to_unit = st.selectbox("HEDEF", birimler)
    
    # Birim formatlama (Görsel temizlik için)
    to_unit_display = to_unit.split(' ')[-1].replace("(", "").replace(")", "")
    if kategori == "YAKIT TÜKETİMİ": to_unit_display = to_unit.split('(')[-1].replace(")", "") if "(" in to_unit else to_unit

    # --- DOĞRUSAL VE ÖZEL DÖNÜŞÜM MANTIĞI ---
    lineer_kategoriler = ["UZUNLUK (m)", "KÜTLE (kg)", "ZAMAN (s)", "ELEKTRİK AKIMI (A)", "MADDE MİKTARI (mol)", "IŞIK ŞİDDETİ (cd)", "BASINÇ (Pa)", "GÜÇ (W)", "ENERJİ & İŞ (J)", "KUVVET (N)", "TORK (Nm)", "HIZ (m/s)", "HACİM (L)", "ALAN (m²)", "VERİ BOYUTU (Byte)", "VERİ İLETİMİ (bps)"]
    
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
        
    elif kategori == "YAKIT TÜKETİMİ":
        if deger == 0:
            is_undefined = True; sonuc_str = "Sıfıra Bölünme"
        else:
            # Önce ortak baz olan L/100km'ye çevir
            if from_unit == "L/100km": base = deger
            elif from_unit == "Kilometre/Litre (km/L)": base = 100 / deger
            elif from_unit == "Mil/Galon (MPG US)": base = 235.215 / deger
            
            # Sonra hedefe çevir
            if to_unit == "L/100km": sonuc = base
            elif to_unit == "Kilometre/Litre (km/L)": sonuc = 100 / base
            elif to_unit == "Mil/Galon (MPG US)": sonuc = 235.215 / base

# 7. AKILLI FORMATLAMA VE ÇIKTI EKRANI
if is_undefined:
    html_output = f"""
        <div class="result-card">
            <div class="result-label">SİSTEM ÇIKTISI (HATA)</div>
            <div class="error-text">{sonuc_str}</div>
        </div>
    """
elif is_text_output:
    html_output = f"""
        <div class="result-card">
            <div class="result-label">SİSTEM ÇIKTISI (OUTPUT)</div>
            <div class="result-value">{sonuc_str}<span class="result-unit">{to_unit_display}</span></div>
        </div>
    """
else:
    # Sayısal Değerler İçin Akıllı Format (Ondalık Temizleme)
    if float(sonuc).is_integer():
        gosterilecek_sonuc = f"{int(sonuc):,}"
    else:
        gosterilecek_sonuc = f"{sonuc:,.6f}".rstrip('0').rstrip('.')
        
    html_output = f"""
        <div class="result-card">
            <div class="result-label">{'FONKSİYON SONUCU' if is_trig else 'SİSTEM ÇIKTISI (OUTPUT)'}</div>
            <div class="result-value">{gosterilecek_sonuc}<span class="result-unit">{to_unit_display}</span></div>
        </div>
    """

st.markdown(html_output, unsafe_allow_html=True)
