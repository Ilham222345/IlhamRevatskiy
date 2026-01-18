# fruits = {"огурцы": 120, "помидоры": 150, "морковь": 40, "картофель": 80}
# fruits["яблоки"] = 140
# print(fruits)

# grades = {"Анна": 5, "Борис": 4, "Вкитор": 3, "Галина": 5, "Дмитрий": 2}
# for key, value in grades.items():
#     if value >= 4:
#         print(key)

# countries = {"Россия": "Москва", "Испания": "Мадрид", "Турция": "Анкара", "Молдавия": "Кишинев"}
# n = input("Введите названия страны: ")
# if n in countries:
#     print(countries.get(n))
# else:
#     print("Страна не найдена")

# students = [
#     ("Анна", "Python"),
#     ("Борис", "Java"),
#     ("Виктор", "Python"),
#     ("Галина", "C++"),
#     ("Дмитрий", "Python")
# ]
# result = {"Python": ["Анна", "Виктор", "Дмитрий"], "Java": "Борис", "C++": "Галина"}
# print(result)

# grades = {"Анна": 5, "Борис": 4, "Вкитор": 3, "Галина": 5, "Дмитрий": 3, "Андрей": 2, "Сергей": 3}
# grades.pop("Андрей")
# print(grades)

# students = ["Анна", "Борис", "Виктор", "Галина"]
# students = dict.fromkeys(["Анна", "Борис", "Виктор", "Галина"])
# print(students)
# students["Анна"] = 37
# students["Борис"] = 24
# students["Виктор"] = 43
# students["Галина"] = 19
# print(students)

# exchange_rates = {"USD": 90, "EUR": 98, "GBR": 155}
# val = input("Введите валюту: ")
# if val in exchange_rates:
#     print(exchange_rates[val])
# else:
#     print(exchange_rates.get(val))
#     print("Неизвестная валюта")

# dict1 = {"Python": "Язык программирования", "Java": "Популярный язык", "C++": "Язык для высокопроизводительных систем"}
# dict2 = {"Python": "Простой и мощный", "JavaScript": "Язык для веба"}
# dict1.update(dict2)
# print(dict1)

# x = (23, "WOW", True, ["ABC", 56.87], {"age": 23})
# print(x[1], x[-1])

# nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
# print(nums.count(4))
# print(nums.index(7))

# lst = ["Python", "Java", "C++", "JavaScript"]
# lst1 = tuple(lst)
# print(lst1)
# print("C++" in lst1)

# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(nums[:3])
# print(nums[-3:])
# print(nums[::2])

ppp = (23, ["ABC", "DEF", "GHI"], True, {"name": "Alex", "age": 23})
print(ppp)
ppp[1].append("ICH")
print(ppp)