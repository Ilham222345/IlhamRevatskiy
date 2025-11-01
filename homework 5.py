cities = ['Москва', 'Тверь', 'Вологда']
numbers = [1, 2, 3, 4, 5]
mixed = [345, 'Gaza', False, 78.23]
print(cities)
print(numbers [-1])
# print(cities[10])
numbers[1]= 10
mixed[-1] = "Python"
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers,reverse=True))

a = [1, 2, 3]
b = [4, 5]
# a.append(b)
oba = a + b
print(oba)
sps = ["Python", "is", "awesome"]
print(sps * 3)

print(3 in numbers)
print("Москва" in cities)
print([1, 2] in mixed)
numbers.remove(3)
del cities[-1]
print(cities)
lll=list(sps [0])
print(lll)
print(max(lll))
print(min(lll))
# print(sum(lll))

towns = ["Дамаск", "Стамбул", "Алжир", "Барселона"]
towns_copy = towns [:]
print(id(towns))
print(id(towns_copy))
print(towns[1:3])
print(towns[2:4])
print(towns[:3])
print(towns[:])
print(towns[-2:])
print(towns[::2])
print(towns[::-1])
print(towns[::-2])
towns[1:3]= ["Сочи", "Нижний Новгород"]
print(towns)
towns [::2] = ["Город", "Город"]
print(towns)
towns[1:3]="Волгоград", "Омск"
print(towns)

qw = [1, 2, 3]
qw2 = [4, 5, 6]
qw3 = qw + qw2
print(qw3)
er = ["Python", "rocks"] *2
print(er)

o1 = [1, 2, 3]
o2 = [1, 2, 3]
print(o1 == o2)
print([10, 5, 3] > [5, 10, 3])
o3 = [1,2, 'abc']
print(o1 == o3)

chars = list("Python")
print(max(chars))
print(min(chars))
# print(sum(chars))
print("Нельзя скдладывать строки друг с другом")

numbers = [5, 10 , 15]
numbers.append(20)
numbers.insert(1, 7)
numbers.append("Python")
numbers.remove(10)
z = numbers.pop()
print(z)
z2 = numbers.pop(1)
numbers.clear()

letters = ['a', 'b', 'c']
letters2 = letters.copy()
letters3 = list(letters)
print(id(letters))
print(id(letters2))
print(id(letters3))

marks = [2, 3, 5, 3, 4, 5, 2, 3]
print(marks.count(3))
print(6 in marks)
print(marks.index(5))

nums = [8, 2, 5, 1, 7]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
nums.reverse()
print(nums)

cities2 = ["Стамбул", "Мерсин", "Газа", "Хан-Юнис", "Багдад", "Малага"]
cities2.sort()
print(cities2)
cities3 = sorted(cities2)
print(id(cities2))
print(id(cities3))

chars = list("programming")
print(chars.count('g'))
chars.reverse()
print(chars)
chars.sort()
print(chars)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)
print(matrix[1])
print(matrix[2][0])
matrix [0]= [0, 0, 0, 0]
print(matrix)
matrix[1][3] = 'Python'
print(matrix)
