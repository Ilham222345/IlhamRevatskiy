# N = int(input("Введите любое целое число: "))
# while N > 0:
#     print(list(range(1, N + 1)))
#     break

# N = int(input("Введите любое целое число: "))
# sum_chet = 0
# i = 0
# lst = list(range(1, N))
# while i < len(lst):
#     if lst[i] % 2 == 0:
#      sum_chet += lst[i]
#     i +=1
# print("Сумма всех четных чисел до {N}: ", sum_chet)

# nat = int(input("Введите натуральное число: "))
# while nat != 0:
#     print(len(str(nat)))
#     break

# nat = int(input("Введите натуральное число: "))
# lst_nat = list(str(nat))
# i = 0
# res = "0"
# while i < len(lst_nat):
#     if lst_nat[i] > res:
#         res = lst_nat[i]
#     i += 1
# print(res)

# password = input("Введите пароль: ")
# tr_password = "qwerty123"
#
# while password != tr_password:
#     password = (input("Введите пароль: "))
# print("Доступ разрешен.")

# lst = [1,3,5,9,11,13,14,15]
# chls = 0
# i = 0
# while i < len(lst):
#     if lst[i] % 2 == 0:
#         chls += lst[i]
#         print(chls)
#         break
#     i += 1
# else: print("Четное число не найдено.")

# h = int(input("Введите число: "))
# summa = 0
# summa += h
# while h != 0:
#     h = int(input("Введите любое целое число или ноль для выхода: "))
#     if h > 0: summa += h
#     continue
# print("Сумма всех положительных числе: "summa)


# a = int(input("Введите первое целое число: "))
# b = int(input("Введите второе целое число: "))
# lst = range(a, b)
# i = 0
# summa = []
# while i < len(lst):
#     if lst[i] % 2 == 0:
#         i += 1
#         continue
#     summa.append(lst[i])
#     i += 1
# print(f"Все нечетные числа начиная с {a} и до {b},", summa)

# N = int(input("Введите любое целое число: "))
# while N > 0:
#     if N % 2 != 0:
#         print(f"Число: {N} - простое число.")
#     break

# ss = input("Введите любое целое число: ")
# mx = ss
# while ss > "0":
#     if ss == "":
#         break
#     if int(ss) > int(mx):
#         mx = ss
#     ss = input("Введите число любое целое число или о для выхода: ")
#
# print(f"Наибольшее число: {mx}")

st = input("Введите какую-либо строку: ")
res = []
for opp in st:
    res += opp
res = res[::-1]
print("".join(res))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         numbers[i] = 0
# print(numbers)

# N = int(input("Введите любое целое число: "))
# res = list(range(0, N))
# result = []
# for i in res:
#     result.append(2 ** i)
# print(result)

# A = int(input("Введите любое целое число: "))
# B = int(input("Введите любое целое число: "))
# K = int(input("Введите любое целое число: "))
# result = []
# for i in range(A, B+1, K):
#     result.append(i)
# print(result)