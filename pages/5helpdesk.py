import streamlit as st

st.set_page_config(
    page_title="Help Desk",
    page_icon="☎",
    layout="wide"
)

st.title("☎ EduVision AI Help Desk")

st.caption("Need help? Contact our support team.")

st.divider()

st.subheader("📧 Email Support")

st.link_button(
    "📩 Send Email",
    "mailto:sanchitasingh9603@gmail.com"
)

st.write("Email: **sanchitasingh9603@gmail.com**")

st.divider()

st.subheader("📞 Phone Support")

st.write("**+91-8181000231**")

st.divider()

st.subheader("🕘 Working Hours")

st.info("""
Monday - Saturday

09:00 AM - 06:00 PM
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home Page", use_container_width=True):
        st.switch_page("Smartedu.py")

with col2:
    if st.button("📋 Back to Summary", use_container_width=True):
        st.switch_page("pages/3summary.py")