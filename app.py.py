import streamlit as st
from g4f.client import Client

# إعداد العميل المجاني
client = Client()

st.set_page_config(page_title="ذكاء اصطناعي يوسف الخارق", page_icon="🧠", layout="centered")
st.title("🧠 ذكاء اصطناعي يوسف الخارق")
st.write("اسألني في أي حاجة في الكون وسأجيبك حالاً!")

# تجهيز الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# صندوق الشات
if q := st.chat_input("اكتب سؤالك هنا يا عبقري..."):
    with st.chat_message("user"):
        st.markdown(q)
    st.session_state.messages.append({"role": "user", "content": q})

    with st.chat_message("assistant"):
        with st.spinner("🤖 يوسف بوت يفكر الآن..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=st.session_state.messages
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error("🤖 عذراً، حاول مرة أخرى!")
