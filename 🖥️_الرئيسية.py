import streamlit as st

st.set_page_config(
    page_title="الرئيسية",
    page_icon="🖥️",
)

st.markdown("""<style>html{direction:rtl;}</style>""", unsafe_allow_html=True)

st.title('الرئيسية')

st.markdown(r'''
هذا التطبيق يحاكي التنقيط الممكن الحصول عليه إعتمادا على الجدول المنشور بالجريدة الرسمية. و هو لا يعتبر "التطبيق" مرجعا أساسية لحساب النقاط.
''')