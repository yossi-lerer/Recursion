# part 1
# step 1 - Power of a Number
def power(base, exponent):
    if exponent == 0:
        return 1
    exponent -= 1
    return base * power(base, exponent)
print(power(2,15))
# step 2 - Factorial
def factorial(n):
    if n == 0:
        return 1 
    n -= 1
    return (n + 1) * factorial(n)
print(factorial(5))