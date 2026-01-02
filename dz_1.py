name = "Ильхам"
age = 22
height = 1.78
print("Имя:", name)
print("Возраст:", age)
print("Рост:", height)

# x = 10
# print(type(x))
# x = 25.5
# print(type(x))
# x = "Python"
# print(x)
# print(type(x))

# a = 7
# b = a
# print(a)
# print(b)
# a = 10
# print(b)
# print("Потому что b ссылается на объект, а не на переменную.")

x = y = z = 100
print(x)
print(y)
print(z)
print(id(x))
print(id(y))
print(id(z))
x, y, z = 1, 2, 3
print(id(x))
print(id(y))
print(id(z))

a = 5
b = 10
a, b = b, a
print(a)
print(b)

print("Использовать такие слова как: True, print, if - нельзя. Они подчеркиваются красным, будет ошибка, так как они являются зарезервивоннами словами в python")
import keyword
print(keyword.kwlist)

var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1))
print(type(var2))
print(type(var3))
var1 = "Goodbye"
print(type(var1))

Car = "BMW"
Year = 2026
Metr = 1.0
Sea = 'Black'
Hours = 24
print(Car)
print(Year)
print(Metr)
print(Sea)
print(Hours)
print(type(Car))
print(type(Year))
print(type(Metr))
print(type(Sea))
print(type(Hours))
переменная = 10
print(переменная)
print("Переменная на русском работает, так как программа разрешает использовать названия на разных языках")