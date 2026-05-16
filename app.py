import streamlit as st
from groq import Groq
import PyPDF2
import io

st.title("Summarize")
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

uploaded_file = st.file_uploader("أو ارفع ملف PDF", type=["pdf"])
if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() or ""
    if pdf_text.strip():
        st.info(f" تم استخراج النص من PDF ({len(pdf_reader.pages)} صفحة)")
        text_from_pdf = pdf_text
    else:
        st.warning(" لم يتم العثور على نص في الملف")
        text_from_pdf = ""
else:
    text_from_pdf = ""

text = st.text_area("اكتب النص هنا...", height=200, value=text_from_pdf)
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
