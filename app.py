import streamlit as st
import anthropic
 
st.title("SUMMARIZE")
st.write("Enter the text!")
 
client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
 
text = st.text_area("اكتب النص هنا...", height=200)
 
if st.button(" لخّص!"):
    if len(text.split()) < 10:
        st.warning(" النص قصير جداً!")
    else:
        with st.spinner(" جاري التلخيص..."):
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=300,
                messages=[
                    {
                        "role": "user",
                        "content": f"أنت مساعد للأطفال. لخّص هذا النص في 3-4 جمل بسيطة بنفس لغة النص:\n\n{text}"
                    }
                ]
            )
            st.success(response.content[0].text)
