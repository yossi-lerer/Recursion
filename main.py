# part 1
# step 1 - Power of a Number
def power(base, exponent):
    if exponent == 0:
        return 1
    exponent -= 1
    return base * power(base, exponent)
print(power(2,15))