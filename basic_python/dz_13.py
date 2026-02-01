# def uppercase_decorate(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         res1 = res.upper()
#         return res1
#     return wrapper
# @uppercase_decorate
# def say_hello():
#     return "hello, world!"
# print(say_hello())
import time


# def repeat(n):
#     def count_func(func):
#         def wrapper(*args, **kwargs):
#             for i in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return count_func
# @repeat(3)
# def hello():
#     print("Hello")
# hello()

def cache(func):
    cache1 = {}
    def wrapper(*args, **kwargs):
        if args in cache1:
            return cache1[args]
        result = func(*args, **kwargs)
        cache1[args] = result
        return result
    return wrapper
@cache
def slow_add(a, b):
    print(f"Вычисляю {a} + {b}...")
    return a + b
print(slow_add(2, 3))
print(slow_add(2, 3))

# import time

# def timer(repeat):
#     def decor(func):
#         def wrapper(*args, **kwargs):
#             total_time = 0
#             for i in range(repeat):
#                 start_time = time.time()
#                 result = func(*args, **kwargs)
#                 end_time = time.time()
#                 total_time += end_time - start_time
#             avarage_time = total_time / repeat
#             print(f"Среднее время выполнения: {avarage_time} сек")
#             return result
#         return wrapper
#     return decor
# @timer(3)
# def slow_function():
#     time.sleep(1)
# slow_function()