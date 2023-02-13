# n = int(input())
# if n % 2:  # True
#     print('odd')
# elif n == 0:
#     print('zero')
# else:  # False
#     print('even')
# print('main thread')

# n = int(input())
# is_even = 'No' if n % 2 else 'Yes' if n != 0 else 'Zero'
# if n % 2:
#     is_even = 'No'
# elif n == 0:
#     is_even = 'Zero'
# else:
#     is_even = 'Yes'
#
# x = True  # 1
# y = False  # 0
# z = False  # 0
# if not x or y:  # 0 + 0 = 0
#     print(1)
# elif not x or not y and z:  # 0 + (1 * 0) = 0 + 0 = 0
#     print(2)
# elif not x or y or not y and x:  # 0 + 0 + (1 * 1) = 0 + 0 + 1 = 1
#     print(3)
# else:
#     print(4)
#
# numbers = []
#
# if any(numbers):
#     pass

# a = 4
# BAD!
# if type(a) is int:
#     pass
# GOOD!
# if isinstance(a, (int, float)):
#     pass

# for number in range(1, 10):  # 1 2 3 4 5 6 7 8 9
#     number **= 2
#     # if number % 2:
#     #     continue
#     if number > 30:
#         break
#     print(number)
# else:
#     print('finish')

# text = 'hello world'
# for el in text:
#     print(el)

# text = 'hello world'
# # str, list, tuple
# for i, j in enumerate(text):
#     print(i, j)

# str, list, tuple
# text = 'hello world'
# for i in range(len(text)):
#     print(text[i])

# data = {
#     'key1': 'val1',
#     'key2': 'val2',
#     'key3': 'val3',
#     'key4': 'val4',
#     'key5': 'val5',
# }
# for key in data.keys():
#     print(key)
# for val in data.values():
#     print(val)
# for key, val in data.items():
#     print(key, val)

# a = 0
# while a < 10:
#     a += 1
#     print(a)

# words = ['hello', 'Python', 'pycharm', 'Belhard']
# for word in words:
#     words.append(word)
# print(words)
#     if word.istitle():
#         words.remove(word)
# for i in range(len(words)):
#     if i == 2:
#         del words[2]
#     # words.append('hello')
# print(words)
# from itertools import *


# for i in count(2, 3):
#     print(i)
# for i in 'hello':
#     print(i)
# for i in cycle('hello'):
#     print(i)
# for i in repeat('hello', 3):
# #     print(i)
#
# # numbers = [6, 2, 4, 3, 5]
# for i in accumulate(numbers):
#     print(i)

# text = 'abcd'
# for i in product(text, repeat=2):
#     print(i)
# for i in permutations(text, 2):
#     print(i)
# n = 3
# for i in combinations_with_replacement(text, 2):
#     print(i)

# text = 'hello python world'
# for i in islice(text, 0, 12, 2):
#     print(i)
# age = input()
# if age.isdigit():
#     age = int(age)
# else:
#     print('Не верные данные, попробуйте еще раз!')
#
# try:
#     age = int(age)
# except ValueError:
#     print('Не верные данные, попробуйте еще раз!')
#
# a = input()
# b = input()
# try:
#     a = int(a)
#     b = int(b)
#     c = a / b
# except ValueError:
#     print('А или Б не число!')
# except ZeroDivisionError:
#     print('На 0 делить нельзя!')
# else:
#     print('Ошибок не было!')
# finally:
#     print('Выполняется в любом случае!')

# raise ValueError('')

# lang = 'en'
#
# match lang:
#     case 'ru' | 'ру':
#         print('Привет')
#     case 'en':
#         print('Hello')
#     case _:
#         print('_')
#
# rgba = (255, 255, 255)
#
# match rgba:
#     case (red, green, blue, alpha):
#         print('rgba')
#     case (red, green, blue):
#         print('rgb')
#     case (_, *a):
#         print('not rgb or rgba')