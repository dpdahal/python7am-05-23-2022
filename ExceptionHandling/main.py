# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# NameError
# AttributeError
# ZeroDivisionError
# IndexError

# try:
#     print(10 / 2)
# except Exception as e:
#     print(e)
# finally:
#     print("This will always run")

#
# def add(x, y):
#     if y == 0:
#         raise ValueError("Can't divide by zero")
#     else:
#         return x + y
#
#
# try:
#     print(add(10, 0))
# except Exception as e:
#     print(e)


# print(__name__)
# import demo
#
# if __name__ == "__main__":
#     print("This is the main program")

print(__file__)
