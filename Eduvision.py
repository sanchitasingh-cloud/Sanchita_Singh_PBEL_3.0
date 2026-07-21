import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="EduVision AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Header
# -------------------------------
st.title("🎓 AI Based Student Performance Prediction System")
st.caption("Predict a student's final examination marks using Artificial Intelligence.")

st.divider()

# -------------------------------
# Welcome Section
# -------------------------------
st.info("""
## 👋 Welcome to EduVision AI

EduVision AI is an AI-powered application that predicts a student's final examination performance using Machine Learning.

The prediction is based on:

- 📚 Study Hours
- 🏫 Attendance
- 📝 First Sessional Marks
- 📖 Second Sessional Marks

Navigate to the **Prediction** page from the sidebar to begin.
""")

st.divider()

# -------------------------------
# Dashboard
# -------------------------------
st.subheader("📊 Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎯 Model Accuracy", "96%")

with col2:
    st.metric("⚡ Prediction Time", "< 1 sec")

with col3:
    st.metric("📄 Report", "PDF")

st.divider()

# -------------------------------
# Project Highlights
# -------------------------------
st.subheader("🌟 Why Eduvision AI?")

left, right = st.columns(2)

with left:
    st.success("🤖 Machine Learning Based Prediction")
    st.success("📊 Accurate Performance Analysis")
    st.success("📈 Easy-to-Understand Results")

with right:
    st.success("📄 Download Student Report")
    st.success("⚡ Fast Prediction")
    st.success("🎯 User-Friendly Interface")

st.divider()

# -------------------------------
# Get Started
# -------------------------------
st.subheader("🚀 Get Started")

st.write(
    "Click the button below or select **Prediction** from the sidebar to start predicting student performance."
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("🚀 Start Prediction", use_container_width=True):
        st.switch_page("pages/1prediction.py")

st.divider()

# -------------------------------
# Footer
# -------------------------------
st.caption(
    "Developed using ❤️ Python | Streamlit | Scikit-learn | Pandas | ReportLab"
)
