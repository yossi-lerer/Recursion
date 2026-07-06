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
    return n * factorial(n -1) 
print(factorial(5))
# step 3 - Build a List From 1 to N
def numbers_to_n(n):
    if type(n) == int:
        n = [n]
    else:
        n.insert(0, n[0] - 1)
    if len(n) == n[-1]:
        return n
    return numbers_to_n(n)
print(numbers_to_n(5))
# step 4 - Count Items in a List
def count_items(lst,sum=0):
    if lst == []:
        return sum
    lst.pop()
    sum += 1
    return count_items(lst, sum)
print(count_items(["h", "g", "d"]))
# step 5 - Count Even Numbers in a List
def count_evens(numbers):
    if numbers == []:
        return 0
    num = numbers.pop()
    if num % 2 == 0:
        return 1 + count_evens(numbers)
    else:
        return 0 + count_evens(numbers)
print(count_evens([4, 7, 10, 3, 8]))