name = 'Ilham'
age = 22
height = 1.78
print("Имя", name)
print("Возраст", age)
print("Рост", height)

x = 10
print(type(x))
x = 25.5
print(type(x))
x = "Python"
print(type(x))
print(x)

a = 7
b = a
print(a,b)
a = 10
print(b)
print("Потому что б, ссылается на объект, а не на переменную")

x = y = z = 100
print(x,y, z)
print(id(x), id(y), id(z))
x, y, z = 342, 678, 198
print(id(x), id(y), id(z))

a = 5
b = 10
a, b = b, a
print (a,b)

var1 = 42
var2 = 3.14
var3 = "Hello"
print(type(var1), type(var2), type(var3))
var1 = "Someone"
print(type(var1))

House = 2
Car = 3.24
Man = "Brain"
Horse = "Run"
Ball = "Football"
print(House, Car, Man, Horse, Ball)
print(type(House), type(Car), type(Man), type(Horse), type(Ball))

