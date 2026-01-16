# Functions & Recursions
# B/c of Functions, code reusability is possible in Python. Reduce code redundancy.

"""# Function definition
def calculate_sum(a, b):
    return a + b
# Function call & arguments
result = calculate_sum(10, 10)
print("Sum:", result)"""

"""average = lambda x, y, z: (x + y + z) / len([x, y, z])
print("Average:", average(20, 30, 40)) """

"""def cal_fact(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print("Factorial; ", cal_fact(5))"""


"""def converter(usd_currency):
    pkr_currency = usd_currency * 285
    return pkr_currency
print("PKR Currency: ", converter(100))"""

# Recursion
#### Recursive Function
"""def function(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * function(n - 1)
print("Factorial: ", function(4))"""

# Practice Problems
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n - 1) + n
print("Proivded Natural Numbers Sum is :", calc_sum(5))