import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Feedback",
    page_icon="⭐",
    layout="wide"
)

st.title("⭐ EduVision AI")

st.subheader("Feedback & Suggestions")

st.caption("Your valuable feedback helps us improve the AI Student Performance Prediction System.")

st.success("Thank you for using EduVision AI!")

st.divider()

col1, col2 = st.columns(2)

with col1:
    name = st.text_input(
        "👤 Full Name",
        placeholder="Enter your name"
    )

    email = st.text_input(
        "📧 Email Address",
        placeholder="Enter your email"
    )

    rating = st.slider(
        "⭐ Overall Rating",
        1,
        5,
        5
    )

with col2:
    feedback = st.text_area(
        "💬 Your Feedback",
        placeholder="Share your experience..."
    )

    suggestion = st.text_area(
        "💡 Suggestions",
        placeholder="Any suggestions to improve the project?"
    )

st.info("""
### 🌟 Your Opinion Matters

Your feedback helps improve:

- 🤖 AI Prediction Accuracy
- 📊 Performance Analysis
- 🎨 User Interface
- 🚀 Overall Experience
""")

if st.button("📩 Submit Feedback", use_container_width=True):

    if name.strip() == "" or email.strip() == "":
        st.warning("Please enter your Name and Email.")

    else:

        data = {
            "Name": [name],
            "Email": [email],
            "Rating": [rating],
            "Feedback": [feedback],
            "Suggestion": [suggestion]
        }

        df = pd.DataFrame(data)

        file = "feedback.csv"

        if os.path.exists(file):
            df.to_csv(file, mode="a", header=False, index=False)
        else:
            df.to_csv(file, index=False)

        st.success("🎉 Thank you! Your feedback has been submitted successfully.")

        st.balloons()

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🤖 AI Model", "Random Forest")

with col2:
    st.metric("📊 Prediction", "Completed")

with col3:
    st.metric("⭐ Max Rating", "5")

st.divider()

st.subheader("⚡ Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("Smartedu.py")

with col2:
    if st.button("📋 Performance Summary", use_container_width=True):
        st.switch_page("pages/3summary.py")

with col3:
    if st.button("☎ Help Desk", use_container_width=True):
        st.switch_page("pages/5helpdesk.py")

st.divider()

st.success("""
### 🎓 Thank You!

Thank you for using **EduVision AI**.

We hope this AI-powered Student Performance Prediction System
helped you understand student performance more effectively.
""")

st.caption("© 2026 EduVision AI | AI Student Performance Prediction System")