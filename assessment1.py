# Python Loop Assessment
# Complete each function using loops.

def sum_to_n(n):
    """
    Return the sum of all numbers from 1 to n (inclusive).
    Example:
    sum_to_n(5) -> 15
    """
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
print(sum_to_n(5))

def count_even_numbers(n):
    """
    Count how many even numbers exist between 1 and n (inclusive).
    """
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total = total + 1
    return total
print(count_even_numbers(23))

def factorial(n):
    """
    Return the factorial of n using a loop.

    Example:
    factorial(5) -> 120
    """
    count = 1
    for i in range(1, n + 1):
        count = count * i
    return count
print(factorial(5))

def multiplication_table(n):
    """
    Return a list containing the multiplication table for n from 1 to 10.

    Example:
    multiplication_table(3)
    -> [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    """
    multiple_list = []
    for i in range(1, 11):
        calc = i * n
        multiple_list.append(calc)
    return multiple_list
print(multiplication_table(3))
  
def sum_of_digits(num: int):
    """
    Return the sum of the digits in a number.

    Example:
    sum_of_digits(1234) -> 10
    """
    total = 0
    cat = str(num)
    for i in cat:
        total = total + int(i)
    return total
print(sum_of_digits(1234))
    
def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in the given string.

    Example:
    count_vowels("hello") -> 2
    """
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count = count + 1
    return count
print(count_vowels("hello"))

def find_primes(n):
    """
    Return a list of all prime numbers from 2 up to n.

    Example:
    find_primes(10) -> [2, 3, 5, 7]
    """
    prime_list = [2, 3]
    if n ==2 :
        return [2]
    if n == 3 :
        return prime_list
    
    for i in range(2, n):
        if i % 2 != 0 and i % 3 != 0:
            prime_list.append(i)
    return prime_list
        

def reverse_string(text):
    return text[::-1]

def pyramid_pattern(n):
    """
    Return a list of strings forming a pyramid pattern of stars.

    Example:
    pyramid_pattern(3)
    -> [
        "*",
        "**",
        "***"
       ]
    """
    pyramid = []
    for i in range(1, n + 1):
        pyramid.append("*" * i)
    return pyramid
print(pyramid_pattern(3))

def multiplication_grid(n):
    """
    Create an n x n multiplication grid using nested loops.

    Example:
    multiplication_grid(3)if n == 2:
            return [2]
    -> [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
       ]
    """
    grid = []
    for i in range(1, n+ 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        grid.append(row)
    return grid
