import streamlit as st
import pandas as pd
from charts.chart import create_chart
from report import generate_report

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Performance Summary",
    page_icon="📋",
    layout="wide"
)

# ---------------------------------
# Check Prediction
# ---------------------------------
if "predicted_marks" not in st.session_state:
    st.warning("Please predict student performance first.")
    st.stop()

# ---------------------------------
# Get Data
# ---------------------------------
student_name = st.session_state["student_name"]
study_hours = st.session_state["study_hours"]
attendance = st.session_state["attendance"]
sessional1 = st.session_state["sessional1"]
sessional2 = st.session_state["sessional2"]
predicted_marks = st.session_state["predicted_marks"]

grade = st.session_state["grade"]
performance = st.session_state["performance"]
status = st.session_state["status"]
confidence = st.session_state["confidence"]
suggestion = st.session_state["suggestion"]

st.title("🎓 EduVision AI")

st.subheader("📋 Student Performance Summary")

st.caption("AI Powered Student Performance Analysis")

st.success("✅ Student report generated successfully.")

st.info("📄 Review the student's academic performance and download the report.")

st.divider()

st.subheader("👤 Student Profile")

col1, col2 = st.columns(2)

with col1:
    st.info(f"""
### Student Details

👤 **Name**

{student_name}

📚 **Study Hours**

{study_hours} Hours
""")

with col2:
    st.info(f"""
### Academic Details

🏫 **Attendance**

{attendance}%

📝 **Sessionals**

{sessional1}/20 & {sessional2}/20
""")

st.divider()

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🎯 Predicted Marks", f"{predicted_marks}/100")

with c2:
    st.metric("🏆 Grade", grade)

with c3:
    st.metric("📈 Performance", performance)

with c4:
    st.metric("🤖 Confidence", f"{confidence}%")

st.divider()

# ---------------------------------
# Summary Table
# ---------------------------------

summary = pd.DataFrame({

    "Field":[
        "Student Name",
        "Study Hours",
        "Attendance (%)",
        "First Sessional",
        "Second Sessional",
        "Predicted Marks",
        "Grade",
        "Performance",
        "Result",
        "Confidence"
    ],

    "Value":[
        student_name,
        study_hours,
        attendance,
        sessional1,
        sessional2,
        predicted_marks,
        grade,
        performance,
        status,
        f"{confidence}%"
    ]

})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)
st.subheader("🏆 Final Result")

if grade in ["A+", "A"]:
    st.success(f"🏆 Final Grade : {grade}")

elif grade == "B":
    st.info(f"🥈 Final Grade : {grade}")

elif grade == "C":
    st.warning(f"📘 Final Grade : {grade}")

else:
    st.error(f"⚠ Final Grade : {grade}")

if status == "PASS":
    st.success("✅ RESULT : PASS")
else:
    st.error("❌ RESULT : FAIL")

st.subheader("🤖 AI Prediction Confidence")

st.progress(confidence / 100)

st.caption(f"Confidence Score : {confidence}%")

st.subheader("💡 AI Recommendation")

st.info(suggestion)

st.subheader("📊 Performance Chart")

create_chart(
    sessional1,
    sessional2,
    predicted_marks
)

st.image(
    "performance_chart.png",
    use_container_width=True
)

st.divider()

# ---------------------------------
# Download Report
# ---------------------------------


# ---------------------------------
# Bottom Buttons
# ---------------------------------
st.divider()

st.subheader("⚡ Quick Actions")

col1, col2, col3, col4, col5 = st.columns(5)

# Download Report
with col1:

    pdf_file = generate_report(
        student_name=student_name,
        study_hours=study_hours,
        attendance=attendance,
        sessional1=sessional1,
        sessional2=sessional2,
        predicted_marks=predicted_marks,
        grade=grade,
        status=status,
        confidence=confidence
    )

    with open(pdf_file, "rb") as pdf:

        st.download_button(
            label="📄 Download PDF Report",
            data=pdf,
            file_name=f"{student_name}_Report.pdf",
            mime="application/pdf",
            use_container_width=True
        )
# Help Desk
with col2:

    if st.button("☎ Help Desk", use_container_width=True):
        st.switch_page("pages/5helpdesk.py")

# Home Page
with col3:

    if st.button("🏠 Home Page",use_container_width=True):

        st.switch_page("Smartedu.py")

with col4:
    if st.button("🏠 Prediction Page", use_container_width=True):
        st.switch_page("pages/1prediction.py")

with col5:
    if st.button("⭐ Feedback", use_container_width=True):
        st.switch_page("pages/4feedback.py")

st.divider()

st.caption(
    "© 2026 EduVision AI | AI Student Performance Prediction System"
)