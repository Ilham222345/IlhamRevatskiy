# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     print(f.read())

# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     print(f.readline())

# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     print(f.read(10))

# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     lst = f.readlines()
#     print(lst)

# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     lst = f.readlines()
#     for line in lst:
#         print(line, end="")

# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     print(f.read(5))
#     f.seek(0)
#     print(f.read(5))

# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     f.readlines()
#     print(f.tell())

# file = "data.txt"
# with open(file, "r", encoding="utf-8") as f:
#     print(f.read())

# file = "data.txt"
# try:
#     with open(file, "r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#         print("Файл не найден.")

# file = "data.txt"
# try:
#     with open(file, "r", encoding="utf-8") as f:
#         print(f.read())
# finally:
#     f.close()

# file = "data.txt"
# try:
#     with open(file, "r", encoding="utf-8") as f:
#         print(f.readline())
#         print(f.readline())
#         print(f.readline())
# except FileNotFoundError:
#         print("Файл не найден.")

file = "numbers.txt"
try:
    with open(file, "r", encoding="utf-8") as f:
        lst = f.readlines()
        result = 0
        for i in lst:
            if i != "\n":
                result += int(i)
        print(result)
except FileNotFoundError:
        print("Файл не найден.")

# file = "log.txt"
# with open(file, "a", encoding="utf-8") as f:
#     import datetime
#     print(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
#     f.write(str(datetime.datetime.now()))
#     f.write("\n")
