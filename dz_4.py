# s = "Python для автоматизации"
# print(s.upper())
# print(s.lower())

# msg = "абракадабра"
# print(msg.find("ра"))
# print(msg.count("а", 3))
# print(msg.find("ка"))
# print(msg.rfind("а"))
# print(msg.find("xyz"))
# print("Если использовать метод: find, то результат будет -1. "
#       "А если использовать метод: index, то будет ошибка.")

# text = "Я изучаю Java"
# a = text.replace("Java", "Python")
# print(a)
# print(a.replace(" ", ""))

# a = "Python"
# b = "12345"
# c = "123abc"
# print(a.isalpha())
# print(b.isdigit())
# print(not(c.isdigit()))

# code = "42"
# print(code.rjust(5, "0"))
# print("text".ljust(10, "*"))

# str = "яблоко, груша, банан"
# apple, gru, banana = str.split(',')
# print(apple)
# print(gru)
# print(banana)
# res = str.split(',')
# print(res)
# str1 = "Python;Java;C++"
# wr1, wr2, wr3 = str1.split(';')
# print(wr1)
# print(wr2)
# print(wr3)

# a = ["Привет", "мир", "!"]
# b = (",".join(a).replace(",", " ", ))
# print(b[:10] + "" + b[11])
# c = ["apple", "banana", "cherry"]
# print(",".join(c))

# v = " Python"
# c = "Python "
# m = " Python "
# print(v.lstrip())
# print(c.rstrip())
# print(m.strip())

# text = "программирование"
# print(text.replace("п", "П"))
# print(text.count("р"))
# print(text.index("и"))
# print(text[::-1])

# text = "Hello\nPython"
# print(text)
# print("Потому что \\n это специальный символ, который переходит на новую строку.")
# t = "Python\tAutomation"
# print(t)
# print("Спец. символ \\t создает табуляцию (длинный пробел)")
#
# path = "C:\new\test.txt"
# print(path)
# print("Текст разделился на новую строку и добавилась табуляция")
# path1 = "C:\\new\\test.txt"
# print(path1)
#
# rr = "Марка вина \"Ягодка\""
# print(rr)

# path = r"C:\new\test.txt"
# print(path)
# print("В сырой строке, любые спец. символы, которые указываются не будут работать в отличие от обычной строки.")

# s = "Hello\b World"
# print(s)
# print("Последняя буква перед спец. символом, была удалена.")
# s1 = "Hello\fPython"
# print(s1)

name = "Ilham"
age = "22"
# a1 = "Меня зовут "
# a2 = " мне "
# a3 = " года."
# print(a1 + name + a2 + age + a3)
# res = "Меня зовут " + name + " мне " + age + "года"
# print(res)
# print("Меня зовут " + name + " мне " + age + "года")
# age = 22
# # print(a1 + name + a2 + age + a3)
# print("Будет ошибка, так как конкатенация делается только с одинаковыми типами данных.")

# print(f"Привет, меня зовут {name}, мне {age} года.")
# print("Привет, меня зовут {imya}, мне {god} года.".format(imya = name, god = age))
# print(f"Привет, меня зовут {age}, мне {name} года.")
# print("Привет, меня зовут {god}, мне {imya} года.".format(god = name, imya = age))

# city = "Adygey"
# year = 2026
# print(f"Сегодня {year} год, и я живу в {city}")
# print(f"Через 5 лет будет {year + 5} год.")
#
# age = 22
# print(f"Дважды мой возраст: {age * 2}.")
# name = "Ilham"
# print(name.upper())

# dol = 1
# rub = 92.5
# print(f"Курс валют: {dol} доллар = {rub} рубля.")
sem = 7
print(f"Квадрат числа {sem} равен {sem ** 2}.")