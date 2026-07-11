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
# step 6 - Find Maximum Number
def max_number(numbers, bigger=0):
    if numbers == []:
        return bigger
    num = numbers.pop()
    if num > bigger:
        bigger = num
        return max_number(numbers, bigger)
    else:
        return max_number(numbers, bigger)
print(max_number([4, 9, 2, 11, 6]))
# step 7 - Reverse a String
def reverse_string(text, reverse_str=""):
    if len(text) == 0:
        return reverse_str
    last = text[-1]
    text = text[:-1]
    reverse_str += last
    return reverse_string(text,reverse_str)  
print(reverse_string("python"))
# step 8 - Check Palindrome
def is_palindrome(text):
    if len(text) == 0:
        return True
    if text[0] != text[-1]:
        return False
    else:
        return True and is_palindrome(text[1:-1]) 
print(is_palindrome("abba"))
# step 9 - Count How Many Times an Item Appears
def count_value(lst, value):
    if lst == []:
        return 0
    num = lst.pop()
    if num == value:
        return count_value(lst, value) + 1
    else:
        return count_value(lst, value) + 0
print(count_value([1, 2, 2, 3, 2], 2))
# step 10 - Fibonacci
def fibonacci(n):
    lst = [0,1]
    if n == 0:
        lst = [0]
        return lst
    for num in range(1, n):
        lst.append(num)
    for fib in range(n - 2):
        lst[fib + 3] = lst[fib + 2] + lst[fib + 1]
    return lst
print(fibonacci(10))