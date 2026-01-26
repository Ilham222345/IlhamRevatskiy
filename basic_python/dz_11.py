# def greet(name):
#     print(f"Привет, {name}! Добро пожаловать!")
# greet("Анна")
#
# def square(num):
#     return num ** 2
# print(square(5))
from itertools import chain


# def is_even(num):
#     return num % 2 == 0
# print(is_even(4))
# print(is_even(7))

# def repeat_string(text, times):
#     return text * times
# print(repeat_string("Python", 3))

# def add(a, b):
#     return a + b
# print(add(3,7))

# def get_max(a, b, c):
#     return max(a, b, c)
# print(get_max(10, 25, 7))

# def calculate(a, b, operation):
#     if operation == "+" :
#         return a + b
#     if operation == "-" :
#         return a - b
#     if operation == "*" :
#         return a * b
#     if operation == "/" :
#         return a / b
#
# print(calculate(10, 5, "+"))
# print(calculate(10, 5, "*"))

# def reverse_string(text):
#     return text[::-1]
# print(reverse_string("Python"))

# def compare_strings(s1, s2, ignore_case=True):
#     if ignore_case:
#         s1 = s1.lower()
#         s2 = s2.lower()
#         s1 = s1.strip()
#         s2 = s2.strip()
#         s1 = s1.rstrip()
#         s2 = s2.rstrip()
#         s1 = s1.lstrip()
#         s2 = s2.lstrip()
#         return s1 == s2
#     else:
#         return s1 == s2
#
# print(compare_strings("Hello", " hello "))
# print(compare_strings("Hello", "HELLO", ignore_case=False))
# print(compare_strings("Hello ", "Hello", ignore_case=False))

# def summarize(*args):
#     results = 0
#     for arg in args:
#         if type(arg) == int:
#             results += arg
#     return results
#
#
# print(summarize(1, 2, 3))
# print(summarize(10, "abc", 5, 2))

# def create_profile(name, age, **extra):
#     print("Профиль пользователя:")
#     print(f"Имя: {name}")
#     print(f"Возраст: {age}")
#     print("Дополнительная информация: ")
#     for key, value in extra.items():
#         print(f"{key}: {value}")
# create_profile("Иван", 30, city="Москва", job="Инженер")

# def process_orders(*orders, discount=0):
#     print(f"Сумма заказа: {sum(orders)}")
#     # res = sum(orders) * (discount / 100)
#     # return f"С учетом скидки: {sum(orders) - res}"
#     return f"С учетом скидки: {sum(orders) * (1 - (discount / 100))}"
# print(process_orders(100, 200, 300, discount=10))

# def merge_lists(*lists):
#     res = []
#     for lst in lists:
#         for x in lst:
#             res.append(x)
#     return res
# print(merge_lists([1, 2], [3, 4], [5, 6]))

# def merge_dicts(*dicts):
#     res = {}
#     for arg in dicts:
#         res.update(arg)
#     return res
# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
# d3 = {"c": 5, "d": 6}
# print(merge_dicts(d1, d2, d3))