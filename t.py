def factorial(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        while n >= 1:
            fact *= n
            n -= 1
        return fact

n = int(input())
print(factorial(n))
