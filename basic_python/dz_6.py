# x = int(input("Введите целое число: "))
# if x > 0:
#     print("Число положительное")
# elif x < 0:
#     print("Число отрицательное")
# else: print("Число равно нулю")

# x = int(input("Введите целое число: "))
# if x % 2 == 0:
#     print("Число четное")
# if x % 2 != 0:
#     print("Число нечетноe")

# x = int(input("Введите целое число: "))
# if 1 <= x <= 10:
#     print("Число в диапазоне")
# else: print("Число вне диапазона")

# a = int(input("Введите первое целое число: "))
# b = int(input("Введите второе целое число: "))
#
# if a < b:
#     a, b = b, a
# print(a, b)

# a = int(input("Введите первое целое число: "))
# b = int(input("Введите второе целое число: "))
#
# if a > b:
#     print(b)
# else:print(a)

# marks = [3, 4, 5, 2, 5, 4]
# if 2 in marks:
#     print("Есть неудолетворительная оценка")
# else:print("Все оценки положительные")

# x = int(input("Введите целое число: "))
# if x % 3 == 0 and x % 5 == 0:
#     print("Число делится на 3 и 5")
# elif x % 3 == 0 and x % 5 != 0:
#     print("Число делится только на 3")
# elif x % 5 == 0 and x % 3 != 0:
#     print("Число делится только на 5")
# else:
#     if x % 3 != 0 and x % 5 != 0:
#         print("Число не делится на 3 и 5")

# password = input("Введите пароль: ")
# if password == "admin123":
#     print("Доступ разрешен")
# else: print("Доступ запрещен")

# amount = float(input("Введите сумму покупки: "))
# if amount >= 5000:
#     print("Сумма со скидкой 10%: ", amount * 0.9)
# if amount < 5000 and amount >= 1000:
#     print("Сумма со скидкой 5%: ", amount * 0.95)

# year = int(input("Введите год: "))
# if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
#     print("Год високосный")
# else: print("Год не високосный")

# mark = int(input("Введите оценку: "))
# # if mark == 5:
# #     print("Отлично")
# # elif mark == 4:
# #     print("Хорошо")
# # elif mark == 3:
# #     print("Удолетворительно")
# # elif mark == 2 or mark == 1:
# #     print("Неудолетворительно")
# # else:
# #      print("Некорекатная оценка")

# hours = int(input("Введите текущее время в часах: "))
# if 6 <= hours <= 11:
#     print("Утро")
# elif 12 <= hours <= 17:
#     print("День")
# elif 18 <= hours <= 21:
#     print("Вечер")
# elif 22 <= hours and hours <= 23:
#     print("Ночь")
# elif 0 <= hours <= 5:
#      print("Ночь")
# else: print("Неккорректное время")

# temp = int(input("Введите температуру: "))
#
# if temp < -10:
#     print("Очень холодно")
# elif -10 <= temp <= 0:
#     print("Холодно")
# elif 1 <= temp <= 10:
#     print("Прохладно")
# elif 11 <= temp <= 25:
#     print("Тепло")
# else:
#     if temp > 25:
#         print("Жарко")

# year = int(input("Введите год: "))
# if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
#     print("Год високосный")
# else: print("Год не високосный")

# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# oper = input("Введите операцию: +, -, *, / ")
# if oper == "+":
#     print(a + b)
# elif oper == "-":
#     print(a - b)
# elif oper == "*":
#     print(a * b)
# elif oper == "/":
#     if b != 0:
#         print(a / b)
#     else:
#         if b == 0:
#             print("Ошибка: деление на ноль!")
# else: print("Некорректная операция")

# item = int(input("Введите число: "))
# print("Число четное") if item % 2 == 0 else print("Число нечетное")

# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# print(a) if a > b else print(b)

# a = int(input("Введите число: "))
# res = "Число положительное" if a > 0 else "Число отрицательное" if a < 0  else "Число равно нулю"
# print(res)

# age = int(input("Введите свой возраст: "))
# print("Вход разрешен") if age >= 18 else print("Вход запрещен")

# sum = float(input("Введите сумму покупки: "))
# result = print(f"Итоговая сумма со скидкой 10 %: {sum * 0.9}") if sum > 5000 else print(f"Итоговая сумма: {sum}")