students = open('students1.txt', mode="w")

LINES = ["Marcos 10\n","Felipe 4\n","José 6\n","Ana 10\n","Maria 9\n", "Miguel 5\n"]
for student in LINES:
    student = student.split(" ")
    if int(student[1]) < 6:
      students.writelines(student[0] +"\n")

# students.writelines(LINES)
students.close()
# recovery_students = []
# with open("file.txt") as grades_file:
#     for line in grades_file:
#         student_grade = line
#         student_grade = student_grade.split(" ")
#         if int(student_grade[1]) < 6:
#             recu_students.append(student_grade[0] + "\n")


# with open("recuStudents.txt", mode="w") as recu_students_file:
#     print(recuStudents)
#     recu_students_file.writelines(recuStudents)


