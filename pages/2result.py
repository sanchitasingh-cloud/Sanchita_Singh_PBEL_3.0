import streamlit as st
import time

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Prediction Result",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# Check if prediction exists
# -------------------------------
if "predicted_marks" not in st.session_state:
    st.warning("⚠ Please predict the student's performance first.")
    if st.button("Go to Prediction Page"):
        st.switch_page("pages/1prediction.py")
    st.stop()

with st.spinner("🤖 EduVision AI is generating the result..."):
    time.sleep(2)

progress = st.progress(0)

for i in range(101):
    time.sleep(0.01)
    progress.progress(i)

progress.empty()

# -------------------------------
# Get Data
# -------------------------------
student_name = st.session_state["student_name"]
study_hours = st.session_state["study_hours"]
attendance = st.session_state["attendance"]
sessional1 = st.session_state["sessional1"]
sessional2 = st.session_state["sessional2"]
predicted_marks = st.session_state["predicted_marks"]

# -------------------------------
# Grade Calculation
# -------------------------------
if predicted_marks >= 18:
    grade = "A+"
    performance = "Excellent"
    status = "PASS"
    confidence = 98
    suggestion = "Excellent work! Keep maintaining your consistency."

elif predicted_marks >= 16:
    grade = "A"
    performance = "Very Good"
    status = "PASS"
    confidence = 94
    suggestion = "Very good performance. Practice regularly to reach A+."

elif predicted_marks >= 14:
    grade = "B"
    performance = "Good"
    status = "PASS"
    confidence = 90
    suggestion = "Good job! Increase study hours and revise daily."

elif predicted_marks >= 12:
    grade = "C"
    performance = "Average"
    status = "PASS"
    confidence = 85
    suggestion = "Focus on weak subjects and improve attendance."

elif predicted_marks >= 10:
    grade = "D"
    performance = "Needs Improvement"
    status = "PASS"
    confidence = 80
    suggestion = "Spend more time studying and complete all assignments."

else:
    grade = "F"
    performance = "Poor"
    status = "FAIL"
    confidence = 75
    suggestion = "Meet your teacher, revise the basics, and prepare a study plan."

# -------------------------------
# Save Grade Information
# -------------------------------
st.session_state["grade"] = grade
st.session_state["performance"] = performance
st.session_state["status"] = status
st.session_state["confidence"] = confidence
st.session_state["suggestion"] = suggestion

# -------------------------------
# Title
st.title("🎓 EduVision AI")

st.subheader("📊 Student Performance Prediction Result")

st.caption("AI Powered Student Performance Analysis")

st.success("🎉 Prediction Completed Successfully!")

st.info("🤖 Random Forest Model has analyzed the student's academic performance.")

st.divider()

# -------------------------------
# Student Details
# -------------------------------
st.subheader("👤 Student Information")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
### Student

👤 Name

**{student_name}**
""")

with col2:
    st.info(f"""
### Academic Details

📚 Study Hours : **{study_hours}**

🏫 Attendance : **{attendance}%**
""")

st.divider()
# -------------------------------
# Result Cards
# -------------------------------
col1, col2, col3, col4= st.columns(4)

with col1:
    st.metric("🎯 Predicted Marks", f"{predicted_marks}/20")

with col2:
    st.metric("🏆 Grade", grade)

with col3:
    st.metric("📈 Performance", performance)

with col4:
    st.metric("🤖 Confidence", f"{confidence}%")

if grade in ["A+", "A"]:
    st.success(f"🏆 Grade : {grade}")

elif grade == "B":
    st.info(f"🏅 Grade : {grade}")

elif grade == "C":
    st.warning(f"📘 Grade : {grade}")

else:
    st.error(f"⚠ Grade : {grade}")

if status == "PASS":
    st.success("✅ RESULT : PASS")
else:
    st.error("❌ RESULT : FAIL")

st.divider()

st.subheader("🤖 AI Confidence Score")

st.progress(confidence / 100)

st.caption(f"Model Confidence : {confidence}%")

st.divider()

st.subheader("📋 Performance Summary")

st.info(f"""
**Performance**

{performance}

---

**Suggestion**

{suggestion}
""")



st.divider()


# -------------------------------
# Navigation Buttons
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅ Back to Prediction", use_container_width=True):
        st.switch_page("pages/1prediction.py")

with col2:
    if st.button("📋 View Performance Summary", use_container_width=True):
        st.switch_page("pages/3summary.py")

with col3:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("Smartedu.py")

st.divider()

st.caption("© 2026 EduVision AI | AI Student Performance Prediction System")