# lst = ["Hello", -9876, True, 43.2]
# itr = iter(lst)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# str = "Its Me"
# itr = iter(str)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# N = int(input("Введите целое число: "))
# res = [num ** 2 for num in range(1, N)]
# print(res)

# res = [num for num in range(-10,10) if num % 2 ==0]
# print(res)

# words = ["Town", "London", "System", "Programm"]
# res = [len(num) for num in words]
# print(res)

# res = ["Четное" if num % 2 == 0 else "Нечетное" for num in range(1, 20)]
# print(res)

lst = [678, "ball", [1, 2, 3]]
res = ["False" if type(x) == int or type(x) == float or type(x) == bool else "True" for x in lst]
print(res)