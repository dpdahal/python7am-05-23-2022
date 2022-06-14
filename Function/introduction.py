# type of function
# inbuilt function
# user define function

# inbuilt function
# print()
# len()
# dir()

# user define function

# define function test
# def test():
#     # function body part / our logic here
#     print("hello ")
#
#
# # calling function
# test()


# function accept value
# def users(name, age):
#     print(name)
#     print(age)
#
#
# users('ram',20)

# def students(name):
#     print(name)
#
#
# name = input("Enter name: ")
# students(name)


# def users(data):
#     print(data)
#
#
# users(['ram','sita'])
#
# a =0
# a=30
#
# def user(name, age=0):
#     print(name)
#     print(age)
#
#
# user('ram', 20)

# a, b, *c = 12, 3, 5, 6, 7, 6, 56
# print(a)
# print(b)
# print(c)
# args
# kwargs
#
# def users(*names, **data):
#     print(names)
#     print(data)
#
#
# users('ram', 'sita', 'gita', 'sophia', name='madan', address='ktm')


# function return  value

# def test():
#     return "hello function"
#
#
#
# print(test())

# def data():
#     a = 40
#     b = 50
#     c = 60
#     return [a, b, c]
#
#
# print(data())

# print(dir(__builtins__))


# function scope
# local
# global

# x = 10
#
#
# def test():
#     global x
#     x = x + 40
#     print(x)
#
#     def a():
#
#         x = 30 + 49
#
#
# test()
# print(x)

# a = lambda x, y: x + y

# def a(x,y):
#     return x+y
# print(a(3, 50))


# def users():
#
#     def name(new_name):
#         return f"I am {new_name}"
#     return name
#
#
# a = users()
# print(a('sophia'))

# print(users()())

# def connection():
#     """
#     connection function use for database connect
#         """
#     return "hello"


# print(connection.__doc__)

# print(print.__doc__)
# print(print.__name__)
# print(__file__)
# print(__name__)


# 5 =120


# def fac(n):
#     if n == 1:
#         return 1
#
#     return n * fac(n - 1)
#
#
# print(fac(5))

"""
5-1 =4 = 20
4-1=3 = 60
3-1=2 = 120
2-1=1 =120

"""


#
# def take_value():
#     pass
#
# def calculate():
#     pass
#
#
# def display():
#     pass

# def test():
#     return "hello"
#
# print(test())

# def outer_function():
#     def inner_function(name):
#         return f"Hi I am {name}"
#
#     return inner_function
#
#
# # print(outer_function()())
# obj = outer_function()
# print(obj('sophia'))


# def data():
#     def add(x, y):
#         return x + y
#
#     return add
#
#
# # print(data()(10, 20))
#
# obj = data()
# print(obj(10, 20))

# def get_doc(any_function):
#     def innner():
#         print(any_function.__doc__)
#
#     return innner
#
# @get_doc
# def test():
#     """this is test function"""
#     print("hello")
#
#
# print(test())


def zero_check(any_function):
    def inner(x, y):
        if y == 0:
            return "Y is zero"
        else:
            return any_function(x, y)

    return inner


@zero_check
def add(x, y):
    return x + y


print(add(10, 10))
