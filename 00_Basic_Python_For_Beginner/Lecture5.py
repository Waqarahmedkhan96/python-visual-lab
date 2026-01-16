#Loops

"""while True:
    print("Hello World")
    break  # it will run once and break the loop"""

"""i = 0
while i < 5:
    print("Hello World", i)
    i += 1  # i = i + 1 """

# print numbers from 10 to 1
"""i = 10
while i > 0:
    print(i)
    i -=1  # i = i - 1
print("Happy New Year!")"""


"""n= int(input("Enter a number: "))
# print first n natural numbers 

i=1
while i<=10:
    print(n*i)
    i+=1"""

# print sum of first n natural numbers
"""n = int(input("Enter a number: ")) 

sum = 0
for i in range(1, n+1):
    sum +=i
    print(sum)
    
     print("Sum of first", n, "natural numbers is:", sum) """

# factorial of a number
n = int(input("Enter a number: "))
i = 1
factorial = 1
while i <= n:
    factorial *= i
    i += 1
print(factorial)
