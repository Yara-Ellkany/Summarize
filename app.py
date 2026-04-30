import streamlit as st
from transformers import pipeline
 
st.title("Summarize")

#يحمل النموذج مره واحده فقط
@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="marefa-nlp/summarization-arabic-english-news")
 
summarizer = load_model()
 
text = st.text_area("اكتب النص هنا...", height=200)
 
if st.button(" لخّص!"):
    if len(text.split()) < 30:
        st.warning("النص قصير جداً! اكتب 30 كلمة على الأقل.")
    else:
        with st.spinner("جاري التلخيص..."):
            result = summarizer(text, max_length=120, min_length=30, do_sample=False)
            st.success(result[0]["generated_text"])
