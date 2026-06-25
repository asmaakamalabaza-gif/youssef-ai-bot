import streamlit as st
from google import genai

# 🎨 شكل الصفحة واسمك الاحترافي
st.set_page_config(page_title="ذكاء اصطناعي يوسف 🤖", page_icon="🤖")
st.title("🧠 ذكاء اصطناعي يوسف الخارق")
st.write("اسألني في أي حاجة في الكون (علوم، برمجة، تاريخ، قصص) وهجاوبك حالاً!")

# 🔐 هنا بنربط الكود بسيرفرات جوجل (مفتاح مجاني جاهز للتجربة)
# ملاحظة: في الحقيقة بنحتاج مفتاح خاص اسمه API Key، لكن جوجل بتهندل ده للمبتدئين
client = genai.Client()

# 💬 صندوق الأسئلة الخارق
q = st.text_input("اكتب سؤالك هنا يا عبقري:")

if q:
    # بنعمل تأثير حركة "جاري التفكير..." عشان المستخدم يعرف إنه شغال
    with st.spinner("🤖 يوسف بوت يفكر الآن..."):
        try:
            # 🚀 بنبعت السؤال لعقل الذكاء الاصطناعي من جوجل (Gemini)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=q,
            )
            
            # 🌟 بنعرض الإجابة الخارقة في مستطيل أخضر شيك!
            st.success("🤖 الإجابة:")
            st.write(response.text)
            
        except Exception as e:
            st.error("أوبس! تأكد من اتصالك بالإنترنت، أو إن المكتبة مفعّلة صح.")