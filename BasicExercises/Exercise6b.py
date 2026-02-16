def classify_triangle(a, b, c):
    if a == b == c:
        return "equilateral"
    elif a != b != c:
        return "scalene"
    else:
        return "isosceles"

print("-Triangle with sides 5,5 and 5 ->" , classify_triangle(5,5,5))
print("-Triangle with sides 3,3 and 4 ->" , classify_triangle(3,3,4))
print("-Triangle with sides 3,4 and 5 ->" , classify_triangle(3,4,5))





