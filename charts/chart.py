import matplotlib.pyplot as plt


def create_chart(sessional1, sessional2, predicted_marks):

    exams = [
        "Sessional 1",
        "Sessional 2",
        "Predicted"
    ]

    marks = [
        sessional1,
        sessional2,
        predicted_marks
    ]

    plt.figure(figsize=(7,4))

    bars = plt.bar(exams, marks)

    plt.ylim(0,100)

    plt.xlabel("Examinations")

    plt.ylabel("Marks")

    plt.title("Student Performance Analysis")

    # Display values on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x()+bar.get_width()/2,
            height+1,
            f"{height:.1f}",
            ha="center",
            fontsize=10
        )

    plt.tight_layout()

    plt.savefig("performance_chart.png")

    plt.close()