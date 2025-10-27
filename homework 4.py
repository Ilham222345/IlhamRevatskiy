s = "Python для автоматизации"
print(s.upper())
print(s.lower())

msg = "абракадабра"
print(msg.count ("ра"))
print(msg.count ("а", 3))
print(msg.find("ка"))
print(msg.rfind("а"))
print(msg.find("xyz"))

text1 = "Я изучаю Java"
print(text1.replace("Java", "Python"))
print(text1.replace(" ", ""))

stroka = "Python"
print(stroka.isalpha())
cfr = "12345"
print(cfr.isdigit())
noy = "123abc"
print(noy.isdigit())

code = "42"
print(code.rjust(5, "0"))
p = ("text")
print(p.ljust(10, "*"))

wer = "яблоко, груша, банан"
f, c, v = wer.split()
print(f, c, v)
ppp = "Python;Java;C++"
q, j, l = ppp.split(";")
print(q)
print(j)
print(l)

open = ["Привет", "мир", "!"]
print(" ".join(open))
uio = ["apple", "banana", "cherry"]
print(",".join(uio))

rtt = " Python"
print(rtt.lstrip())
rtt2 = "Python "
print(rtt2.rstrip())
rtt3 = " Python "
print(rtt3.strip())

text = "программирование"
print(text.replace("п", "П"))
print(text.count("р"))
print(text.find("и"))
print(text [::-1])

text2 = "Hello\nPython"
print(text2)
potomy = "Потому что команда слэш н, выводит на новую строку"
print(potomy)

t = "Python\tAutomation"
print(t)
chodelayet = ("Слэщ т создает большой пробел")
print(chodelayet)
path = "C:\\new\\test.txt"
print(path)
pppp = 'Марка сока "Ягодка"'
print(pppp)

path2 = r"C:\new\test.txt"
print(path2)
potomychto = "raw string - отключает обработку спецсимволов"
print(potomychto)

s = "Hello\b World"
print(s)
s2 = "Hello\fPython"
print(s2)

# name = "Ilham"
# age = "22"
# result = "Меня зовут " + name + "," + " мне " + age + "года"
# print(result)

name = "Ilham"
age = "22"
print(type(age))
# result = "Привет, меня зовут {}, мне {} года". format(name, age)
# print(result)
# result = f"Привет, меня зовут {name}, мне {age} года."
# print(result)
# result = f"Мне {age} года, привет, меня зовут {name}"
# print(result)
result = f"Привет, меня зовут {age}, мне {name} года."
print(result)

sehir = "Адыгеи"
yil = "2025"
text = f"Сегодня {yil} год, и я живу в {sehir}"
print(text)
yil = int(yil)
text2 = f"Через 5 лет будет {yil + 5} год."
print(text2)

age = int(age)
p = f"Дважды мой возраст: {age * 2}"
print(p)
print(name.upper())

dollar = 1
ruble = 92.5
text6 = f"Курс валют: {dollar} доллар = {ruble} рубля"
print(text6)
opo = 7
text7 = f"Квадрат числа {opo} равен {opo ** 2}"
print(text7)