students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
    ]

#Write the following functions
#average(grades): receives a list of grades and returns the average
#get_status(avg): receives an average and returns "PASS" if >= 5.0
#or "FAIL" otherwise
#Then, for each student, print their name, average (rounded to 1 decimal),
#and status. At the end, print how many students passed and how many failed.

def average(grades):
    grades = []
    grades_sum = 0
    for grade in grades:
        grades_sum += grade
    average = grades_sum / len(grades)
    return average

for