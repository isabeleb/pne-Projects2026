def letter_grade(score):
    if 0 <= score <= 2.9:
        return "F"
    elif 3 <= score <= 4.9:
        return "D"
    elif 5 <= score <= 6.9:
        return "C"
    elif 7 <= score <= 8.9:
        return "B"
    elif 9 <= score <= 10:
        return "A"

print("Score 9.5:", letter_grade(9.5))
print("Score 7:" , letter_grade(7))
print("Score 5.5:" , letter_grade(5.5))
print("Score 3.2:" , letter_grade(3.2))
print("Score 1:" , letter_grade(1))