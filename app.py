import streamlit as st
from groq import Groq

st.title(" ملخصي")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

text = st.text_area("اكتب النص هنا...", height=200)

if st.button(" لخّص!"):
    if len(text.split()) < 10:
        st.warning(" النص قصير جداً!")
    else:
        with st.spinner(" جاري التلخيص..."):

            # كشف اللغة
            arabic_letters = sum(1 for c in text if '\u0600' <= c <= '\u06FF')
            language = "العربية" if arabic_letters > 5 else "الإنجليزية"

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": f"You are a helpful assistant for kids. Summarize the text in 3-4 simple sentences. You MUST respond in {language} only."},
                    {"role": "user", "content": text}
                ]
            )
            st.success(response.choices[0].message.content)
