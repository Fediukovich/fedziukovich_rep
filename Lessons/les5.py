# def is_palindrome(text):
#     text = text.lower().strip().replace(' ', '')
#     print(text == text[::-1])
#
# is_palindrome('шалаш')
# is_palindrome('python')
#
# def is_palindrome(text):
#     text = text.lower().strip().replace(' ', '')
#     return text == text[::-1], text
#
# a = is_palindrome('шалаш')
# b = is_palindrome('python')
# print(a)
# print(b)

# def foo(a, numbers=None):
#     if numbers is None:
#         numbers = []
#     numbers.append(a)
#     return numbers
#
#
# print(foo(4))  # [4]
# print(foo(4))  # [4]

# def bar(*args):
#     print(args)
#
#
# bar(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# def baz(**kwargs):
#     print(kwargs)
#
#
# baz(a=1, b=2, text='Hello')
#
# def foo(a, b=10, *args, c=None, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(kwargs)
#
#
# foo(1, 2, 3, 4, 5, 6, 7, 8, 9, c=0, d=4, e=7)

# def foo():
#     def bar():
#         print('bar')
#     bar()


# def zamikanie(a):
#     def wrapper(b):
#         def wrapper2(c):
#             return a * b * c
#         return wrapper2
#     return wrapper


# # func = zamikanie(5)(4)(3)
# # print(func)
#
# def foo():
#     print('foo')

#
# def bar():
#     print('bar')
#
#
# def baz():
#     print('baz')
#
#
# def error():
#     print('error')
#
#
# a = int(input())
# data = {
#     1: foo,
#     2: bar,
#     3: baz,
# }
# func = data.get(a, error)
# func()
# if a == 1:
#     foo()
# elif a == 2:
#     bar()
# elif a == 3:
#     baz()
# else:
#     error()
#
#
# multiply = lambda x, y: x * y
#
# print(multiply(4, 5))
#
#
# def multiple(x, y):
#     return x * y
#
#
# words = ['Hello', 'python', 'apple', 'age', 'Pycharm', 1, 2, 3, 4]
# ['hello', 'python', 'apple', 'age', 'pycharm', '1', '2', '3', '4']
# words.sort(key=lambda x: f'{x}'.lower())
# print(words)
#
# numbers = [1, 2, 5, 34, -23, -5, -3]
# numbers.sort(key=lambda x: abs(x))
# print(numbers)


# numbers = [*range(11)]
# result = []
# for number in numbers:
#     if number % 2 == 0:
#         result.append(number**2)
#     else:
#         result.append(number)

# result = [*map(lambda x: x ** 2 if x % 2 == 0 else x, range(11))]
# print(result)

# objs = [1, 2, 3, 'hello', 'python', 4, 5, 'world']
# result = []
# for obj in objs:
#     if isinstance(obj, str):
#         result.append(obj)
#
# result = [*filter(lambda x: isinstance(x, str), objs)]
#
# print(result)

# words = ['hello', '', '', None, 'world', 'python']
# result = [*filter(lambda x: x, words)]
# print(result)
#
#
# text = 'Hello'
# numbers = [1, 2, 3, 4]
# objs = (True, False, None)
# result = [*zip(text, numbers, objs, strict=False)]
# print(result)
#
# a = 5
#
#
# def foo():
#     a = 4
#
#     def bar():
#         nonlocal a
#         a += 1
#         print(a)
#     print(locals())
#
#     bar()
#
#
# foo()
#
#
# globals().get('foo')()

# numbers = [1, 2, 3, 4]
# numbers = reversed(numbers)
# print(list(numbers))
# print(list(numbers))

# db = [f'user{i}' for i in range(100)]
#
#
# def get_user():
#     for user in db:
#         yield user
#
#
# a = get_user()
# for user in a:
#     print(user)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# a = iter([1, 2, 3, 4, 5])
# print(next(a))
# print(next(a))
# print(next(a))


# numbers = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, [6, 7, 4, 6, 3], 6, 3, 5, [4, 2, 4, 2, ]], 5, 4, [6, 2, 3, 5, 3]]
#
#
# def recursive_multiple(numbers):
#     result = 1
#     for number in numbers:
#         if isinstance(number, list):
#             result *= recursive_multiple(number)
#         else:
#             result *= number
#     return result
#
#
# print(recursive_multiple(numbers))


# def validate_arguments(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, str):
#                 raise TypeError
#
#         for val in kwargs.values():
#             if not isinstance(val, str):
#                 raise TypeError
#
#         result = func(*args, **kwargs)
#         result = f'Результат: {result}'
#         return result
#
#     return wrapper
#
#
# @validate_arguments
# def is_palindrome(text):
#     return text == text[::-1]
#
#
# wrapped_is_palindrome = validate_arguments(is_palindrome)
#
#
# @validate_arguments
# def is_equal(text1, text2):
#     return text1 == text2
#
#
# print(is_palindrome('шалаш'))


# def decorator(c):
#     def wrapper(func):
#         def _wrapper(a, b):
#             a += c
#             b += c
#             return func(a, b)
#         return _wrapper
#     return wrapper
#
#
# @decorator(2)
# def multiply(a, b):
#     return a * b
#
#
# print(multiply(2, 5))


# def foo(a):
#     foo.a = 'argument'
#     return a
#
#
# foo(3)
#
#
# print(foo.a)
#
#
# def dispatcher():
#     _registry = {}
#
#     def _dispatcher(**filters):
#         def wrapper(func):
#
#             def _wrapper(*args, **kwargs):
#                 _registry.update({func.__name__: {'link': func, 'filters': filters}})
#                 return func(*args, **kwargs)
#
#             return _wrapper
#
#         return wrapper
#     _dispatcher.registry = _registry
#
#     return _dispatcher
#
#
# dp = dispatcher()
#
#
# @dp(name='username')
# def foo():
#     print('foo')
#
#
# @dp(name='fullname', age=18)
# def bar():
#     print('bar')
#
# print(dp.registry)
#
# def main(**kwargs):
#     print(kwargs)
#     for func in dp.registry:
#         print(func)
#         # print(func.get('filters'))
#         # for key, val in func.get('filters').items():
#         #     if key not in kwargs or val != kwargs.get(key):
#         #         break
#         # else:
#         #     func.get('link')(**kwargs)
#         #     break

#
# main(name='username')

# from functools import *
# from datetime import datetime
# from time import sleep

# a=2, b=100, c=2 => [2, 4, 6, 8, ..., 98]
# @lru_cache()
# def foo(a, b, c):
#     sleep(3)
#     return [*range(a, b, c)]

# start_time = datetime.now()

# foo(a=2, b=100000, c=2)
# foo(a=2, b=100000, c=2)
#
# end_time = datetime.now()
# print(end_time - start_time)

# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = reduce(lambda x, y: x * y, numbers)
# print(result)

# from itertools import *

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # result = [*filter(lambda x: not x % 2, numbers)]
# # print(result)
# result = [*dropwhile(lambda x: x ** 2 < 17, numbers)]
# print(result)
# result = [*takewhile(lambda x: x ** 2 < 17, numbers)]
# print(result)
# text = 'hello'
# numbers = [1, 2, 3, 4]
# objs = (True, False)
# result = [*zip_longest(text, numbers, objs, fillvalue='')]
# print(result)

# numbers = [(1, 2, 3, 4), (5, 6, 7, 8, 9)]
# c = chain((1, 2, 3, 4), (5, 6, 7, 8, 9))
# for i in chain.from_iterable(numbers):
#     print(i)

# numbers = [*range(100)]
# # print([[*x] for x in tee(numbers, 5)])
# for line in tee(numbers, 5):
#     for number in line:
#         print(number, end=' ')
#     print()