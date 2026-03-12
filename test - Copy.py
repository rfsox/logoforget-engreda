import streamlit as st
import requests
import base64

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="REDA AI | Marketing Suite", page_icon="💰", layout="wide")

# وظيفة معالجة الشعار الخاص بك
def get_styled_logo(file_path):
    try:
        with open(file_path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            return f'<div style="display: flex; justify-content: center;"><img src="data:image/png;base64,{encoded}" style="width: 150px; border-radius: 50%; box-shadow: 0 0 20px #9b30ff;"></div>'
    except: return ""

# 2. ستايل البراند المحترف
st.markdown("""
    <style>
    .main { background-color: #050505; color: white; }
    .title { text-align: center; color: #9b30ff; font-size: 3em; font-weight: bold; text-shadow: 2px 2px 10px #000; }
    .subtitle { text-align: center; color: #888; margin-bottom: 30px; }
    .stButton>button { background: linear-gradient(90deg, #9b30ff, #00d4ff); color: white; border-radius: 10px; border: none; padding: 10px 20px; font-weight: bold; width: 100%; }
    .stTextInput>div>div>input { background-color: #111 !important; color: white !important; border: 1px solid #333 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة التطبيق
st.markdown(get_styled_logo("image_4.png"), unsafe_allow_html=True)
st.markdown("<h1 class='title'>REDA AI PRO</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>الأداة المتكاملة لتصميم الهوية الإعلانية للشركات</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 🛠️ تفاصيل الإعلان")
    product_name = st.text_input("📦 شنو منتجك؟ (مثلاً: عطر، مطعم، ملابس)")
    ad_style = st.selectbox("🎯 نوع المحتوى المطلوب:", ["إعلان فيسبوك جذاب", "بوست إنستغرام فخم", "وصف منتج للموقع"])
    
    generate_all = st.button("🚀 ابدأ السحر")

with col2:
    if generate_all and product_name:
        with st.spinner("⏳ جاري تحضير حملتك الإعلانية..."):
            # توليد الصورة
            img_prompt = f"professional product photography of {product_name}, luxury lighting, 8k resolution, highly detailed"
            img_url = f"https://pollinations.ai/p/{img_prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
            
            # عرض النتائج
            st.image(img_url, caption=f"تصميم إعلاني لـ {product_name}", use_container_width=True)
            
            st.markdown("---")
            st.markdown("### ✍️ النص التسويقي المقترح:")
            # هنا محاكاة بسيطة لنص ذكي (تكدر نطورها بـ API ثاني مستقبلاً)
            st.info(f"✨ بوست مقترح: \n\n حاب تميز {product_name} مالتك؟ 🔥 جبنالك الحل الأمثل اللي يجمع بين الفخامة والجودة. احجز الآن وخلي مشروعك يلمع! \n\n #تسويق #ذكاء_اصطناعي #رضا_ستوديو")
            
            st.download_button("📥 تحميل التصميم", requests.get(img_url).content, file_name="ad_design.png")
    else:
        st.info("اكتب اسم المنتج واضغط (ابدأ السحر) حتى تشوف النتيجة")
