import streamlit as st
import requests
import base64

# 1. إعدادات الصفحة
st.set_page_config(page_title="LOGO FORGE PRO | REDA", page_icon="🟣", layout="wide")

# 2. وظيفة معالجة الشعار
def get_styled_logo(file_path):
    try:
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            return f'''
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{encoded}" 
                style="width: 180px; height: 180px; border-radius: 30px; 
                object-fit: cover; box-shadow: 0 0 25px rgba(155, 48, 255, 0.6);">
            </div>
            '''
    except:
        return "<div style='text-align:center;'>🟣</div>"

# 3. ستايل CSS فخم
st.markdown("""
    <style>
    .main { background-color: #0d0e12; color: white; }
    .neon-text {
        text-align: center; color: white;
        text-shadow: 0 0 10px #fff, 0 0 20px #9b30ff, 0 0 40px #9b30ff;
        font-size: 3.5em; font-weight: bold; margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white; border-radius: 12px; border: none; height: 55px;
        font-weight: bold; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px #9b30ff; }
    input { background-color: #1a1b21 !important; color: white !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. واجهة التطبيق (العنوان ثم الشعار تحته)
st.markdown("<h1 class='neon-text'>LOGO FORGE PRO</h1>", unsafe_allow_html=True)
st.markdown(get_styled_logo("image_5.png"), unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9b30ff; font-size: 1.3em; font-weight: bold;'>Reda AI Studio</p>", unsafe_allow_html=True)

st.markdown("---")

# 5. منطقة التصميم
col_in, col_out = st.columns([1, 1.2], gap="large")

with col_in:
    st.markdown("### 🛠️ تخصيص الشعار")
    logo_name = st.text_input("🎨 (English) اكتب اسم الشعار المطلوب:", placeholder="e.g. Majestic Lion Head")
    style = st.selectbox("✨ اختر نمط التصميم:", 
                         ["Cyberpunk Neon", "Luxury Gold", "3D Glossy", "Minimalist Vector", "Gaming Mascot"])
    generate_btn = st.button("🚀 ابتكر اللوغو الآن")

with col_out:
    if generate_btn and logo_name:
        with st.spinner("⏳ جاري ابتكار شعارك الخاص..."):
            prompt = f"logo icon, {logo_name}, {style}, professional, masterpiece, high quality"
            api_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=1234&model=flux&nologo=true"
            try:
                response = requests.get(api_url, timeout=30)
                if response.status_code == 200:
                    st.image(response.content, caption="شعارك الجاهز - تصميم رضا", use_container_width=True)
                    st.download_button("📥 تحميل الشعار (PNG)", data=response.content, file_name="reda_logo.png")
                else: st.error("عذراً، السيرفر مشغول")
            except: st.error("تحقق من اتصالك بالإنترنت")
    else:
        st.markdown('<div style="height: 300px; border: 2px dashed #333; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: #555;">سيظهر تصميمك هنا</div>', unsafe_allow_html=True)

