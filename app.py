import streamlit as st
from groq import Groq
 
st.title("Summarize")
st.write("اكتب النص الذي تريده")
 
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
 
text = st.text_area("اكتب النص هنا...", height=200)
 
if st.button(" لخّص!"):
    if len(text.split()) < 20:
        st.warning("النص قصير جداً!")
    else:
        with st.spinner("جاري التلخيص..."):
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "أنت مساعد للأطفال. لخّص النص في 3-4 جمل بسيطة بنفس لغة النص."},
                    {"role": "user", "content": text}
                ]
            )
            st.success(response.choices[0].message.content)
