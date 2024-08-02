def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += int(square(n))
    return sum

print(sum_squares(10)) # Should be 285

for x in range(5):
    print(x)

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120
