import streamlit as st
from groq import Groq

st.title("Summarize")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

text = st.text_area("اكتب النص هنا...", height=200)

if st.button(" لخّص!"):
    if len(text.split()) < 10:
        st.warning(" النص قصير جداً!")
    else:
        with st.spinner("⏳ جاري التلخيص..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": """أنت مساعد للأطفال.
لخّص النص في 3-4 جمل بسيطة.
مهم جداً: إذا كان النص بالعربية لخّص بالعربية. إذا كان النص بالإنجليزية لخّص بالإنجليزية.
لا تغير اللغة أبداً."""},
                    {"role": "user", "content": f"لخّص هذا النص:\n\n{text}"}
                ]
            )
            st.success(response.choices[0].message.content)
