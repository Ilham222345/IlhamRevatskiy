# lst = ["Python", 123, "Java", 456, "C++", 789]
# def finder():
#     for x in lst:
#         if type(x) == str:
#             yield x
# print(list(finder()))

# import random
# def counter():
#     count = 0
#     while count != 10:
#         x = random.randint(1, 100)
#         count += 1
#         yield x
# x = list(counter())
# print(max(x))

# def gen():
#     with open("word.txt", "r") as f:
#         for line in f:
#             for word in line.split():
#                     if len(word) > 5:
#                         yield word
# print(list(gen()))

# def gen():
#     with open("text.txt", "r") as f:
#         f1 = f.readlines()
#         for x in f1:
#             if "Python" in x:
#                 yield x
# lst = list(gen())
# for x in lst:
#     print(x, end="")

# import random
# def gen():
#     while True:
#         x = random.randint(1, 100)
#         yield x
#         if x == 50:
#             return
# for y in gen():
#     print(y)

print("Не понимаю решения задачи №6 и что такое N")

# def gen():
#     x = 0
#     while x != 5:
#         x += 1
#         yield f"Полученные данные {x}"
# for y in gen():
#     print(y)

# x = input("Введите число: ")
# numbers = list(map(int, x.split()))
# result = map(lambda y: y * 2, numbers)
# print(list(result))

# cities = ["Москва", "Санкт-Петербург", "Казань"]
# result = map(lambda x: x.upper(), cities)
# print(list(result))

# numbers = [15, 30, 45, 22, 60, 77, 90, 100]
# result = filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers)
# print(list(result))

# lst = ["hello", "world42", "python3", "abc", "123", "data1science"]
# result = filter(lambda x: not x.isalpha(), lst)
# print(list(result))

# countries = ["Россия", "Франция", "Германия"]
# capitals = ["Москва", "Париж", "Берлин"]
# result = zip(countries, capitals)
# print(dict(result))

# data = [(1, "a"), (2, "b"), (3, "c")]
# a, b = zip(*data)
# print(list(a))
# print(list(b))

# names = ["петр", "Иван", "мария", "Анна"]
# print(sorted(names, key=lambda x: ord(x[0])))

# products = [("Телефон", 500), ("Ноутбук", 1000), ("Планшет", 700)]
# products_1, products_2 = zip(*products)
# products_3 = sorted(products_2)
# result = zip(products_1, products_3)
# print(list(result))