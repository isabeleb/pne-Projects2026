def fibon(n):
    a, b = 0, 1
    for _ in range(n + 1):
        a, b = b, a + b
    return a

def fibosum(n):
    total_sum = 0
    for i in range(n):
        term = fibon(i)
        total_sum += term
    return total_sum

sum_5 = fibosum(5)
sum_10 = fibosum(10)

print("Sum of the first 5 terms of the Fibonacci series:", sum_5)
print("Sum of the first 10 terms of the Fibonacci series:", sum_10)