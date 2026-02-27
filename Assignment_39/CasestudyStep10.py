#-----------------------------------------------------------------
#
#  File name   : Assigment38Question10.py
#  Descreption : Plot SleepHours against FinalResult
#  Author      : Kartik Ganesh Jare
#  Date        : 24/2/26
#
#-----------------------------------------------------------------

# Does sleeping more guarantee success? Explain

import pandas as pd
import matplotlib.pyplot as plt

Datasetpath = "student_performance_ml.csv"

df = pd.read_csv(Datasetpath)

print("Dataset gets loaded successfully...")

pass_students = df[df["FinalResult"] == 1]
fail_students = df[df["FinalResult"] == 0]

plt.scatter(pass_students["FinalResult"],
            pass_students["SleepHours"],
            label="Pass")

plt.scatter(fail_students["FinalResult"],
            fail_students["SleepHours"],
            label="Fail")

plt.xlabel("Final Result")
plt.ylabel("Sleep Hours")
plt.title("Sleep Hours vs Final Result")
plt.legend()
plt.show()


# It is show how sleep more has pass the exam and who sleep less fails it
