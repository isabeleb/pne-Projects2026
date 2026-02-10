def fibon(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

term_5 = fibon(5)
term_10 = fibon(10)
term_15 = fibon(15)

print("5th Fibonacci term:" , term_5)
print("10th Fibonacci term:", term_10)
print("15th Fibonacci term:" , term_15)