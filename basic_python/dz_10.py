# mn = {123, 56, "str", 56.7, False, (1,2,3)}
# print(mn)
# mn.add(98)
# print(mn)
# mn.add("str")
# print(mn)

# cities = {"Ankara", "Dublin", "Kemer", "Krasnodar"}
# print(cities)
# print("Все города уникальны, потому что множество содержит, только уникальные данные.")

# numbers = set(range(1, 11))
# print(numbers)
# numbers.remove(5)
# print(numbers)
# numbers.discard(15)
# print(numbers)

# str = "abracadabra"
# print(set(str))
# print(len(set(str)))

# mn = set()
# mn.add(10)
# print(mn)
# mn.add("Hello")
# print(mn)
# mn.add((1, 2, 3))
# print(mn)
# mn.add([4, 5, 6])
# print("Списки нельзя добавить во множества. Во множествах хранятся, только неизменяемые типы данных, список - изменяемый.")

# s1 = {34.5, "Table", 345, True}
# s2 = {39.5, "Table", 2200, True}
# res = s1 & s2
# print(res)
# res1 = s1 | s2
# print(res1)
# res2 = s1 - s2
# print(res2)
# res3 = s2 - s1
# print(res3)
# res4 = s1 ^ s2
# print(res4)

# even_numbers = set()
# odd_numbers = set()
# for num in range(1, 11):
#     if num % 2 == 0:
#         even_numbers.add(num)
#     else: odd_numbers.add(num)
# print(even_numbers)
# print(odd_numbers)
# res = even_numbers & odd_numbers
# print(res)
# res1 = even_numbers | odd_numbers
# print(res1)
#
# python_students = {"Анна", "Иван", "Мария", "Сергей"}
# java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
# print("На оба курса записаны: ", python_students & java_students)
# print("Записаны только на один курс: ", python_students ^ java_students)
# print("Записаны хотя бы на один курс: ", python_students | java_students)

# text1 = set("программирование")
# text2 = set("автоматизация")
# print(text1 | text2)
# print(text1 - text2)
# print(text1 ^ text2)

# sss = {x ** 2 for x in range(1,11) if x % 2 == 0}
# print(sss)

# words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
# words1 = [w.upper() for w in words]
# print(set(words1))

# grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
# res = {x:"Отлично" if y >= 80 else "Удолетворительно" for x,y in grades.items()}
# print(res)

# text = {"Python", "automation", "programming", "testing"}
# res = {x: len(x) for x in text}
# print(res)

x = range(1,11)
res = {x1:{y ** 2 for y in range(1,x1+1)} for x1 in x}
print(res)