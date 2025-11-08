# x = int(input("Введите число: "))
# if x > 0:
#     print("Число положительное")
# elif x < 0:
#     print("Число отрицательное")
# else:
#     print("Число равно нулю")
#
# x = int(input("Введите целое число: "))
# if x % 2 ==0:
#     print("Число четное")
# else:
#     print("Число нечетное")

# x = int(input("Введите число: "))
# # if 1 < x < 10:
# #     print("Число в диапозоне")
# # else:
# #     print("Число вне диапозона")

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a < b:
#     a, b = b, a
#     print (a, b)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a > b:
#     print(b)
# else:
#     print(a)

# marks = [3, 4, 5, 2, 5, 4]
# if 2 in marks:
#     print("Есть неудовлетворительная оценка")
# else:
#     print("Все оценки положительные")

# x = int(input("Введите число: "))
# if x % 3 == 0 and x % 5 == 0:
#     print("Число делится на 3 и 5")
# elif x % 3 == 0:
#     print("Число делится только на 3")
# elif x % 5 == 0:
#     print("Число делится только на 5")
# else:
#     print("Число не делится на 3 и 5")

# x = input("Введите пароль: ")
# if x == 'admin123':
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# amount = float(input("Сумма покупки: "))
# if amount >= 5000:
#     amount = amount * 0.9
# elif amount >= 1000:
#     amount = amount * 0.95
# print("Итоговая сумма: ", amount)

# year = int(input("Введите год: "))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Год високосный")
# else:
#     print("Год не високосный")

# marks = int(input("Введите оценку: "))
# if marks == 5:
#     print("Отлично")
# elif marks == 4:
#     print("Хорошо")
# elif marks == 3:
#     print("Удовлетворительно")
# elif marks == 2 or marks == 1:
#     print("Неудовлетворительно")
# else:
#     print("Некорректная оценка")

# time = int(input("Введите сколько сейчас время (в часах): "))
# if 6 <= time and time <= 11:
#     print("Утро")
# elif 12 <= time and time <= 17:
#     print("День")
# elif 18 <= time and time <= 21:
#     print("Вечер")
# elif 22 <= time <= 23 or time <= 23:
#     print("Ночь")
# else:
#     print ("Некорекктное время")

# temp = int(input("Введите температуру: "))
# if -10 > temp:
#     print("Очень холодно")
# elif -10 <= temp <= 0:
#     print("Холодно")
# elif 1 <= temp <= 10:
#     print("Прохладно")
# elif 11 <= temp <= 25:
#     print("Тепло")
# elif 25 < temp:
#     print("Жарко")

# r1 = float(input("Введите первое число: "))
# r2 = float(input("Введите второе число: "))
# r3 = (input("Введите операцию: "))
#
# if r3 == "+":
#     print(r1 + r2)
# elif r3 == "-":
#     print(r1 - r2)
# elif r3 == "*":
#     print(r1 * r2)
# elif r3 == "/":
#     if r2 != 0:
#         print(r1 / r2)
#     else:
#         r2 == 0
#         print("Ошибка: деление на ноль!")
# else:
#     print("Некорректная операция")

# pop = int(input("Введите число: "))
# print("Четное число" if pop % 2 == 0 else  "Нечетное число")

# n1 = int(input('Введите первое число: '))
# n2 = int(input('Введите второе число: '))
# print("Первое число больше" if n1 > n2 else "Второе число больше")

# l = int(input('Введите число: '))
# print("Число положительное" if l > 0 else ("Число отрицательное" if l < 0 else "Число равно нулю"))

# age = int(input('Введите свой возраст: '))
# print("Вход разрешен" if age > 18 else "Вход запрещен")

suum = float(input('Введите сумму покупки: '))
suum2 = suum * 0.9 if suum > 5000 else suum
print("Итоговая сумма:", suum2)

