import streamlit as st
import joblib
import numpy as np
import time

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="Prediction",
    page_icon="🎯",
    layout="wide"
)

# -----------------------------------
# Load Model
# -----------------------------------
model = joblib.load("student_model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------------
# Header
# -----------------------------------
st.title("🎯 AI Student Performance Prediction")

st.caption("Predict the final examination marks using Artificial Intelligence.")

st.success("✨ Enter the student details below and click Predict Performance.")

st.divider()

# -----------------------------------
# Layout
# -----------------------------------
left, right = st.columns([2, 1])

# -----------------------------------
# Student Details Card
# -----------------------------------
with left:

    with st.container(border=True):

        st.subheader("👨‍🎓 Student Details")

        student_name = st.text_input(
            "👤 Student Name",
            placeholder="Enter Student Name"
        )

        study_hours = st.slider(
            "📚 Study Hours (per day)",
            0, 12, 5
        )

        attendance = st.slider(
            "🏫 Attendance (%)",
            0, 100, 80
        )

        sessional1 = st.number_input(
            "📝 First Sessional Marks",
            min_value=0,
            max_value=20,
            value=10
        )

        sessional2 = st.number_input(
            "📖 Second Sessional Marks",
            min_value=0,
            max_value=20,
            value=10
        )

# -----------------------------------
# Information Card
# -----------------------------------
with right:

    with st.container(border=True):

        st.subheader("ℹ Prediction Info")

        st.metric("Maximum Marks", "100")

        st.metric("Sessionals", "20 + 20")

        st.metric("Attendance", "100%")

        st.metric("AI Model", "Random Forest")

        st.info("Fill all fields before predicting.")

# -----------------------------------
# Predict Button
# -----------------------------------
st.divider()

if st.button(
    "🚀 Predict Performance",
    use_container_width=True,
    type="primary"
):

    if student_name.strip() == "":
        st.warning("Please enter the student name.")
        st.stop()

    # Loading Animation
    with st.spinner("🤖 AI is analysing the student's performance..."):

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.02)
            progress.progress(i + 1)

    # Prediction
    input_data = np.array([
        [study_hours,
         attendance,
         sessional1,
         sessional2]
    ])

    input_scaled = scaler.transform(input_data)

    predicted_marks = model.predict(input_scaled)[0]

    predicted_marks = max(0, min(100, predicted_marks))

    # Save Data
    st.session_state["student_name"] = student_name
    st.session_state["study_hours"] = study_hours
    st.session_state["attendance"] = attendance
    st.session_state["sessional1"] = sessional1
    st.session_state["sessional2"] = sessional2
    st.session_state["predicted_marks"] = round(predicted_marks, 2)

    # Go to Result Page
    st.switch_page("pages/2result.py")

# -----------------------------------
# Footer
# -----------------------------------
st.divider()

st.caption(
    "© 2026 EduVision AI • AI Student Performance Prediction System"
)