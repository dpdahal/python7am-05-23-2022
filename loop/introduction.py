# Types of loops
# - while loop
# - for loop
# - nested loops

"""
Repetitive execution of the same block of code over and over is referred to as iteration.
There are two types of iteration:
Definite iteration, in which the number of repetitions is specified explicitly in advance
Indefinite iteration, in which the code block executes until some condition is met
In Python, indefinite iteration is performed with a while loop
"""

# while loop
# while <condition>:
#   <block of code>


i = 1
while i <= 10:
    print(i, end=' ')
    i += 1

# 1. Hello, World
# 2. Hello, World


# increment = 1
# while increment <= 10:
#     print(f"{increment} Hello, World")
#     increment += 1

# total even and total odd
# total sum of even
# total sum of odd

# if x%2==0


# increment = 1
# total_even = 0
# total_odd = 0
# total_odd_sum = 0
# total_even_sum = 0
#
# while increment <= 10:
#     if increment % 2 == 0:
#         total_even += 1
#         total_even_sum += increment
#     else:
#         total_odd += 1
#         total_odd_sum += increment
#
#     increment += 1
#
# print(f"Total even: {total_even} Sum of even: {total_even_sum}")
# print(f"Total odd: {total_odd} Sum of odd: {total_odd_sum}")

# i = 1
# num = int(input("Enter a number: "))
# users = []
#
# while i <= num:
#     name = input("Enter your name: ")
#     users.append(name)
#     i += 1
#
# print(users)

# number of students
# nep,eng,mat,sic,pop
# total marks,percentage,division

# users = ['ram', 'shyam', 'hari', 'sita', 'gita']
# for name in users:
#     print(name)
# i = 0
# while i < len(users):
#     print(users[i])
#     i += 1


# i = 0
# while i < 2:
#     for x in range(1):
#         print(f"{i} Hello")
#         print(f"Python")
#     i += 1


# data = [
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120]
# ]
#
# for n in data:
#     for y in n:
#         print(y)
# else:
#     print("End of data")
