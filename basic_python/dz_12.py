# x = lambda v: v ** 2
# print(x(5))

# ch = lambda x: x % 2 == 0
# print(ch(67))

words = ["banana", "apple", "cherry"]
def sort_by_last_letter(words):
    return sorted(words, key=lambda x: x[-1])
print(sort_by_last_letter(words))

# def multiply_by(n):
#     def mult(x):
#         return x * n
#     return mult
# times3 = multiply_by(3)
# times5 = multiply_by(5)
# print(times3(10))
# print(times5(10))

# def counter(start=0):
#     def count():
#         nonlocal start
#         start +=1
#         return start
#     return count
#
# c1 = counter(5)
# c2 = counter()
#
# print(c1())
# print(c1())
# print(c2())
# print(c2())
