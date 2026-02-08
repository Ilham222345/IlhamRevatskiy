items = [5, "hello", [1, 2], 3.14, {"a": 1}, "world"]
result = []
for item in items:
    if isinstance(item, (list, str)):
        result.append(item)
print(result)

def describe_type(x):
    if isinstance(x, bool):
        print("Это булевое значениие")
    elif isinstance(x, str):
        print("Это строка")
    elif isinstance(x, (int, float)):
        print("Это число")
    elif not isinstance(x, (str, int, float, bool)):
        print("Неизвестный тип")
describe_type(5.5)
describe_type(True)
describe_type("Привет")
describe_type([1, 2, 3])

def filter_list(f, data: list[int]) -> list[int]:
    result = []
    for item in data:
        if f(item):
            result.append(item)
    return result
print(filter_list(lambda x: x > 3, [1, 3, 5, 7]))

def print_info(name: str, age: int, tags: list) -> None:
    print(name, age, tags)

def analyze(data: list[int | float]):
    if data:
        print("Количество элементов: ", len(data), "Среднее значение: ", sum(data) / len(data))
analyze([1, 2, 3])

flags = [True, True, True, False]
print(all(flags))
print(any(flags))

field = ['x', 'x', 'x', 'o', 'o', '', '', '', '']
result = all(x == x for x in field[0:3])
print(result)

P = ['0', '0', '0', '*', '0']
result = any(x == '*' for x in P)
print(result)

import random
colors = ['red', 'green', 'blue', 'yellow', 'purple']
print(random.choice(colors))

random.seed(42)
x = [random.randint(1,100) for i in range(10)]
print(x)

def greet(name: str) -> str:
    return f"Привет, {name}!"
print(greet("Анна"))

def multiply(a: int, b: float) -> float:
    return a * b
print(multiply(10, 2))

def area(length: float, width: float) -> float:
    return length * width
print(area.__annotations__)