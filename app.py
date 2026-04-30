import streamlit as st
from transformers import pipeline
 
st.title(" Summarizer ")
st.write("اكتب اي نص تريده!")
 
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")
 
summarizer = load_model()
 
text = st.text_area("اكتب النص هنا...", height=200)
 
if st.button(" لخّص!"):
    if len(text.split()) < 30:
        st.warning("⚠️ النص قصير جداً! اكتب 30 كلمة على الأقل.")
    else:
        with st.spinner("جاري التلخيص..."):
            result = summarizer(text, max_length=80, min_length=30, do_sample=False)
            st.success(result[0]["summary_text"])
