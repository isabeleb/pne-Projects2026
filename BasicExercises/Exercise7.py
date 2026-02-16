student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

grades = student["grades"]

grades_list = []
grades_sum = 0
for key, value in grades.items():
    grades_list.append(value)
    grades_sum += value

average_grade = grades_sum / len(grades_list)

print("-Name:" , student["name"])
print("-Number of subjects:" , len(student["subjects"]))
print("-Enrolled in PNE:" , "PNE" in student["subjects"])
print("-Grade in Databases:" , grades["Databases"])
print("-Average grade:" , round(average_grade, 2))
print("-Subject grades:")
for s, g in grades.items():
    print( s , "->" , g)








