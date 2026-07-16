from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from datetime import datetime


def generate_report(
        student_name,
        study_hours,
        attendance,
        sessional1,
        sessional2,
        predicted_marks,
        grade,
        status,
        confidence,
        filename="Student_Report.pdf"
):

    # -----------------------------
    # Create PDF
    # -----------------------------
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    # -----------------------------
    # Title
    # -----------------------------
    title = styles["Heading1"]
    title.alignment = TA_CENTER

    story.append(
        Paragraph(
            "<b>EduVision AI</b>",
            title
        )
    )

    story.append(
        Paragraph(
            "<b>AI Student Performance Prediction Report</b>",
            title
        )
    )

    story.append(Spacer(1, 20))

    # -----------------------------
    # Date & Time
    # -----------------------------
    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M %p")

    story.append(
        Paragraph(
            f"<b>Date :</b> {date}<br/><b>Time :</b> {time}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    # -----------------------------
    # Student Information Heading
    # -----------------------------
    story.append(
        Paragraph(
            "<b>STUDENT INFORMATION</b>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 10))

    # -----------------------------
    # Student Information Table
    # -----------------------------
    student_table = [

        ["Student Name", student_name],

        ["Study Hours", f"{study_hours} Hours"],

        ["Attendance", f"{attendance}%"]

    ]

    table = Table(
        student_table,
        colWidths=[180, 220]
    )

    table.setStyle(TableStyle([

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BACKGROUND", (0, 0), (0, -1), colors.lightblue),

        ("BACKGROUND", (1, 0), (1, -1), colors.whitesmoke),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

        ("ALIGN", (0, 0), (-1, -1), "CENTER")

    ]))

    story.append(table)

    story.append(Spacer(1, 20))
    # ---------------------------------
# Academic Performance Heading
# ---------------------------------

    story.append(
    Paragraph(
        "<b>ACADEMIC PERFORMANCE</b>",
        styles["Heading2"]
    )
)

    story.append(Spacer(1, 10))

# ---------------------------------
# Academic Performance Table
# ---------------------------------

    performance_table = [

       ["First Sessional", f"{sessional1}/20"],

       ["Second Sessional", f"{sessional2}/20"],

       ["Predicted Marks", f"{round(predicted_marks,2)}/100"],

       ["Grade", grade],

       ["Result", status],

       ["Confidence", f"{confidence}%"]

]
    table2 = Table(
    performance_table,
    colWidths=[180,220]
)

    table2.setStyle(TableStyle([

    ("GRID",(0,0),(-1,-1),1,colors.black),

    ("BACKGROUND",(0,0),(0,-1),colors.beige),

    ("BACKGROUND",(1,0),(1,-1),colors.whitesmoke),

    ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

    ("BOTTOMPADDING",(0,0),(-1,-1),8),

    ("ALIGN",(0,0),(-1,-1),"CENTER")

]))

# ---------------------------------
# Teacher's Remark
# ---------------------------------

    if predicted_marks >= 90:
       remark = "Outstanding performance. Keep up the excellent work."

    elif predicted_marks >= 75:
       remark = "Excellent performance. Continue regular revision and maintain your attendance."

    elif predicted_marks >= 60:
       remark = "Good performance. Practice regularly to improve further."

    elif predicted_marks >= 40:
       remark = "Average performance. Spend more time on revision and assignments."

    else:
       remark = "Needs improvement. Meet your teacher regularly and follow a study schedule."

    story.append(
        Paragraph(
          "<b>TEACHER'S REMARK</b>",
           styles["Heading2"]
    )
)

    story.append(
         Paragraph(
           remark,
           styles["Normal"]
    )
)

    story.append(Spacer(1,30))

# ---------------------------------
# Signature Section
# ---------------------------------

    signature_table = [

        ["Teacher Signature", "Principal Signature"],

        ["__________________", "__________________"]

]
    signature = Table(
        signature_table,
        colWidths=[220,220]
)

    signature.setStyle(TableStyle([

      ("ALIGN",(0,0),(-1,-1),"CENTER"),
  
      ("BOTTOMPADDING",(0,0),(-1,-1),10),
 
      ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold")

]))

    story.append(signature)
# ---------------------------------
# Performance Chart Heading
# ---------------------------------

    from reportlab.graphics.shapes import Drawing
    from reportlab.graphics.charts.barcharts import VerticalBarChart

    story.append(
       Paragraph(
        "<b>PERFORMANCE CHART</b>",
        styles["Heading2"]
    )
)

    story.append(Spacer(1, 10))

# ---------------------------------
# Create Bar Chart
# ---------------------------------

    drawing = Drawing(400, 220)

    chart = VerticalBarChart()

    chart.x = 50
    chart.y = 30
    chart.width = 280
    chart.height = 150
    chart.data = [[
    sessional1,
    sessional2,
    predicted_marks
]]

    chart.categoryAxis.categoryNames = [
         "Sessional 1",
        "Sessional 2",
        "Prediction"
]

    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = 100
    chart.valueAxis.valueStep = 20

    drawing.add(chart)

    story.append(drawing)

    story.append(Spacer(1,20))

# ---------------------------------
# Grade Highlight Box
# ---------------------------------

    story.append(
       Paragraph(
        "<b>FINAL GRADE</b>",
        styles["Heading2"]
    )
)

    if grade == "A+":
         grade_color = colors.green

    elif grade == "A":
          grade_color = colors.darkgreen

    elif grade == "B":
        grade_color = colors.blue

    elif grade == "C":
        grade_color = colors.orange

    elif grade == "D":
       grade_color = colors.darkorange

    else:
       grade_color = colors.red

    grade_table = Table(
       [[f"Grade : {grade}"]],
       colWidths=[200]
)

    grade_table.setStyle(TableStyle([

     ("BACKGROUND",(0,0),(-1,-1),grade_color),

      ("TEXTCOLOR",(0,0),(-1,-1),colors.white),

     ("ALIGN",(0,0),(-1,-1),"CENTER"),

     ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

     ("FONTSIZE",(0,0),(-1,-1),18),

     ("BOTTOMPADDING",(0,0),(-1,-1),10),
 
     ("TOPPADDING",(0,0),(-1,-1),10)

]))

    story.append(grade_table)

    story.append(Spacer(1,20))

# ---------------------------------
# PASS / FAIL Box
# ---------------------------------

    if status == "PASS":
       result_color = colors.green
    else:
        result_color = colors.red

    result_table = Table(
      [[f"Result : {status}"]],
      colWidths=[200]
)

    result_table.setStyle(TableStyle([

       ("BACKGROUND",(0,0),(-1,-1),result_color),

      ("TEXTCOLOR",(0,0),(-1,-1),colors.white),

       ("ALIGN",(0,0),(-1,-1),"CENTER"),

       ("FONTNAME",(0,0),(-1,-1),"Helvetica-Bold"),

      ("FONTSIZE",(0,0),(-1,-1),16),

      ("BOTTOMPADDING",(0,0),(-1,-1),10),

       ("TOPPADDING",(0,0),(-1,-1),10)

]))

    story.append(result_table)

    story.append(Spacer(1,25))

# ---------------------------------
# Footer
# ---------------------------------

    story.append(
       Paragraph(
        "<b>Generated by EduVision AI</b>",
        title
    )
)

    story.append(
     Paragraph(
        "<font size='10'>AI Student Performance Prediction System</font>",
        styles["Normal"]
    )
)

# ---------------------------------
# Build PDF
# ---------------------------------

    doc.build(story)

    return filename