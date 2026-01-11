# cities = ["Москва", "Тверь", "Вологда"]
# numbers = [1, 2, 3, 4, 5]
# mixed = [345, "Stroka", False, 34.56]
# print(cities[0])
# print(numbers[-1])
# # print(cities[10])
# print("Произойдет ошибка, так как мы вышли за диапазон.")
# numbers[1] = 10
# mixed[-1] = "Python"
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

# a = [1, 2, 3]
# b = [4, 5]
# print(a + b)
# c = ["Python", "is", "awesome"]
# print(c * 3)

# print(3 in numbers)
# print("Москва" in cities)
# print([1, 2] in mixed)

# del numbers[2]
# del cities[-1]

# a = list("Python")
# b = list("Java")
# print(a)
# print(max(a))
# print(min(a))
# # print(sum(a))
# print("Будет ошибка, потому что у нас в переменной только список. Функция sum(), начинает сложение с 0, если не указано другое начальное значение.")

# towns = ["Istanbul", "Moscow", "Komrat", "Maykop"]
# towns2 = towns[:]
# print(id(towns))
# print(id(towns2))
# print(towns[1:3])
# print(towns[2:])
# print(towns[:3])
# print(towns[:])
# print(towns[-2:])
# print(towns[::2])
# print(towns[::-1])
# print(towns[::-2])
# towns[1:3] = "Сочи", "Нижний Новгород"
# print(towns)
# towns[::2] = "Город", "Город"
# print(towns)
# cities[1:3] = "Волгоград", "Омск"

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# c = ["Python", "rocks"]
# print(c * 2)

# print([1, 2, 3] == [1, 2, 3])
# print([10, 5, 3] > [5, 10, 3])
# print([1, 2, 3] >= [1, 2, "abc"])
# print("Произойдет ошибка, потому что числа, нельзя сранивать со строками. Сравнение без ошибок, будет есть использовать знаки: == или !=")
#
# chars = list("Python")
# print(max(chars))
# print(min(chars))
# # print(sum(chars))
# print("Будет ошибка, потому что у нас в переменной только список. Функция sum(), начинает сложение с 0, если не указано другое начальное значение.")

# numbers = [5, 10, 15]
# numbers.append(20)
# print(numbers)
# numbers.insert(1, 7)
# print(numbers)
# numbers.append("Python")
# print(numbers)
# numbers.remove(10)
# print(numbers)
# last = numbers.pop()
# print(numbers)
# print(last)
# numbers.pop(1)
# print(numbers)
# numbers.clear()
# print(numbers)

# letters = ["a", "b", "c"]
# letters1 = letters.copy()
# letters2 = list(letters)
# print(letters)
# print(letters1)
# print(letters2)
# print(id(letters))
# print(id(letters1))
# print(id(letters2))

# marks = [2, 3, 5, 3, 4, 5, 2, 3]
# print(marks.count(3))
# print(marks.index(5))
# print(marks.count(6))

# nums = [8, 2, 5, 1, 7]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# nums.reverse()
# print(nums)

# cities = ["Rize", "Baky", "Gaza", "Tbilisi"]
# cities.sort()
# print(cities)
# sort = sorted(cities)
# print(sort)

# chars = list("programming")
# print(chars)
# print(chars.count("g"))
# chars.reverse()
# print(chars)
# chars.sort()
# print(chars)
# print("Порядок букв изменился, согласно их значениям ord.")

matrix = [
    ["one", "two", "three"],
    [1, 2, 3,
     4, 5, 6,
     7, 8, 9,
     10, 11, 12]
]
print(matrix)
print(matrix[1][0:3])
print(matrix[1][3])
matrix[0][:] = 0, 0, 0
print(matrix)
matrix[1][2] = "Python"
print(matrix)