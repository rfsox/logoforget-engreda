import streamlit as st
import requests
import base64

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="LOGO FORGE PRO | REDA", page_icon="🟣", layout="wide")

# 2. وظيفة معالجة صورة الشعار لتصبح دائرية وشفافة
def get_styled_logo(file_path):
    try:
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            # CSS لجعل الصورة دائرية تماماً مع توهج بنفسجي خلفي
            return f'''
            <div style="display: flex; justify-content: center;">
                <img src="data:image/png;base64,{encoded}" 
                style="width: 150px; height: 150px; border-radius: 50%; 
                object-fit: cover; border: 3px solid #9b30ff;
                box-shadow: 0 0 20px #9b30ff;">
            </div>
            '''
    except:
        return "<h1 style='text-align:center;'>🟣</h1>"

# 3. تصميم الـ CSS (الواجهة العصرية المشعة)
st.markdown("""
    <style>
    .main { background-color: #0d0e12; color: white; }
    .neon-text {
        text-align: center; color: white;
        text-shadow: 0 0 10px #fff, 0 0 20px #9b30ff, 0 0 40px #9b30ff;
        font-size: 3.5em; font-weight: bold; margin-bottom: 0px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #6a11cb, #2575fc);
        color: white; border-radius: 12px; border: none; height: 50px;
        font-weight: bold; width: 100%; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 15px #9b30ff; }
    /* تحسين حقول الإدخال */
    input { background-color: #1a1b21 !important; color: white !important; border-radius: 10px !important; }
    </style>
    """, unsafe_allow_html=True)

# 4. الهيدر (الشعار والاسم المشع)
st.markdown("<h1 class='neon-text'>LOGO FORGE PRO</h1>", unsafe_allow_html=True)
logo_html = get_styled_logo("image_4.png")
st.markdown(logo_html, unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9b30ff; font-size: 1.2em;'>Reda AI Studio</p>", unsafe_allow_html=True)

st.markdown("---")

# 5. منطقة العمل (المدخلات والنتائج)
col_input, col_display = st.columns([1, 1.2], gap="large")

with col_input:
    st.markdown("### ⚙️ تخصيص الشعار")
    # خانة اسم الشعار (رجعت مثل ما ردت)
    logo_name = st.text_input("💎 (English) اكتب اسم الشعار المطلوب:", placeholder="مثلاً: Golden Falcon")
    
    # اختيار الستايل
    style = st.selectbox("✨ اختر نمط التصميم:", 
                         ["Cyberpunk Neon", "Luxury Gold", "3D Glossy", "Minimalist Vector", "Gaming Mascot"])
    
    generate_btn = st.button("🚀 ابتكر اللوغو الآن")

with col_display:
    if generate_btn and logo_name:
        with st.spinner("⏳ جاري معالجة طلبك في سيرفرات رضا..."):
            # بناء الأمر النهائي للسيرفر
            prompt = f"logo icon, {logo_name}, {style}, professional, high detail, masterpiece, white background"
            api_url = f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}?width=1024&height=1024&seed=4567&model=flux&nologo=true"
            
            try:
                response = requests.get(api_url, timeout=30)
                if response.status_code == 200:
                    st.image(response.content, caption=f"تم التوليد بنمط {style}", use_container_width=True)
                    st.download_button("📥 تحميل اللوغو (PNG)", data=response.content, file_name=f"{logo_name}_logo.png", mime="image/png")
                else:
                    st.error("السيرفر مشغول، حاول مرة أخرى")
            except:
                st.error("تحقق من اتصالك بالإنترنت")
    elif generate_btn and not logo_name:
        st.warning("⚠️ يرجى كتابة اسم الشعار أولاً")
    else:
        st.markdown('''
            <div style="height: 300px; border: 2px dashed #333; border-radius: 20px; 
            display: flex; align-items: center; justify-content: center; color: #555;">
                سيظهر تصميمك هنا
            </div>
            ''', unsafe_allow_html=True)

# 6. الفوتر

st.markdown("<p style='text-align: center; margin-top: 50px; color: #444;'>Designed with ❤️ by Reda | 2026</p>", unsafe_allow_html=True)
