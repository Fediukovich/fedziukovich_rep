# numbers = [1, 2, 3, 4, 5, 'hello']
# text = 'hello'
# letters = list(text)
# print(letters)
#
# print(numbers[2])
# numbers[2] = 'world'
# print(numbers)

# numbers = [[1, 2, 3], [4, 5, 6], [7,8,9]]

# numbers = [1, 2, 3, [4, 5, 6]]
# print(numbers[3][1])

# words = ['hello', 'world', 'python']
# del words[2]
# print(words)

# words = ['hello', 'world', 'python']
# word = words.pop(2)
# print(words)

# words.remove('hello')
# print(words)

# words = ['hello', 'world', 'python', 'hello']
# words.append([1, 2, 3])
# words.insert(2, 'pycharm')
# words.extend([1, 2, 3, 4])
# words.extend('hello')
# print(words)

# numbers1 = [1,2,3,4,5]
# numbers2 = [6,7,8,9,0]
# numbers3 = numbers1 + numbers2
# print(numbers3)
# print(numbers3 * 3)

# numbers = [3,4,5,2,4,5,6,7,8,4,3,9,6,1]
# numbers.sort(reverse=True)
# print(numbers)

# words = ['Hello', 'world', 'python', 'hello', 'age']
# words.sort()
# words.sort(key=len)
# sorted_words = sorted(words)
# print(words)
# print(sorted_words)
# words.reverse()
# reversed_words = words[::-1]
# reversed_words = reversed(words)
# print(words)
# print(reversed_words)

# words = ['Hello', 'world', 'python', 'hello', 'age']
# words2 = words[:]
# words.append('good')
# print(words2)

# words = ['Hello', 'world', 'python', 'hello', 'age',[1,2,3,4]]
# words2 = words[:]
# words[5].append('good')
# print(words2)

# from copy import copy, deepcopy
# words = ['Hello', 'world', 'python', 'hello', 'age',[1,2,3,4]]
# words2 = deepcopy(words)
# words[5].append('good')
# print(words2)

# words = ['hello', 'python']
# lst = ['good','scholl']
# lst[2].append('age')
# print(words)

# numbers = [0 for i in range(100)]
# print(numbers)
# numbers = [i for i in range(100)]
# print(numbers)
# numbers = [i**i for i in range(100)]
# print(numbers)

# from pprint import pprint
# n = int(input()) #3
# matrix =  [[0 for j in range(n)] for i in range(n)]
# pprint(matrix)

# КОРТЕЖИ
# numbers = (5, )
# result = numbers + (6, 7)
# print(result)

# numbers = (1,2,3,[4,5,6,7])
# numbers[3].clear()
# print(numbers)

# Множества
# print(set('hello'))
# print({1,2,3,4,5,6,7,8,5,4,3})
# print({1,2,3,4,5,6,7,8,5,4,3,45})

# a = {1,2,3,4}
# b = {1,2,3,4,5,6,7}
# print(a <= b)
# print(a.issubset(b))

# words = {'words', 'hello', 'python'}
# words.add('pycharm')
# words.pop()
# words.discard('Minsk')
# words.remove('words')
# print(words)

# a = {1,2,3}
# b = {4,5,6,7}
# c = {4,2,6}
# s = c.union(a, b)
# print(c.union(a, b))
# print(s)

# print(a.difference(b))
# print(a - b)

# print(b.difference(a))
# print(b - a)

# print(b.intersection(c,a))
# print(a & b & c)

# print(b.symmetric_difference(c))
# print(c.symmetric_difference(b))
# print(b^c)
#
# a.update()
# a |= b |= c

# frozenset

# DICTIONARY

# print(type({4,5,6}))
# data = {
#     'name': 'Alex',
#     'age': 34
# }
# data['city'] = 'Minsk'
# print(data['name'])
# print(data)

# user = (('name', 'alex), ('age', 34), ('city', 'Minsk'))
#
# data = dict(user))
# print(date)

# # data = {keys}
# data = dict.fromkeys(('name', 'age', 'city'))
# print(data)

# data = {
#     'name': 'Alex',
#     'age': 34
# }
# print(data.get('name'))
# print(data.get('city', 'N/Y'))
# print(data.setdefault('name', 'N/Y'))
# print(data.pop('city', None))
# print(data)
# print(list(data.keys()))

# data.update({
#     'city': 'Minsk',
#     'age': 35
# })
# print(data)
#
# data2 = {
#     'city': 'Minsk',
#     'age': 35
# }

# new_data = data | data2
# print(new_data)
# print(data)
# print(data2)

# COLLECTIONS
# from collections import *

# numbers = [2,2,3,4,5,6,7,8,8,6,5,4,3,0,3,2,7,6,9,0,1,4]
# numbers2 = [4,5,6,7,8,8,9,9,0,3,4,6]
# numbers = [21345669095474888237]
# numbers2 = [5628926532982384]
# numbers_counter = Counter(numbers)
# numbers_counter2 = Counter(numbers2)
# print(numbers_counter)
# print(numbers_counter.total())
# print(numbers_counter.most_common(3))
# print(list(numbers_counter.elements()))
#
# numbers_counter.subtract(numbers_counter2)
# print(numbers_counter)
# print(numbers_counter2)
# print(numbers_counter - numbers_counter2)

# q = deque([1,2,3,4,5])
# q.rotate(2)
# print(q)
# q.rotate(-3)
# print(q)

# user = defaultdict(list)
# user['languages'].append('ru')
# user(user['name']
# print(user)

# user = OrderedDict({'age': 35, 'city': 'Minsk', 'name': 'Alex'})
# user.move_to_end('city', last=True)
# user.move_to_end('name', last=False)
# print(user)

# user = namedtuple('User', ('name', 'age', 'city'))
# vasya = user(name='vasya', age=34, city='Minsk')
# print(vasya.name)

# data1 = {'a': 1, 'b': 2}
# data2 = {'c': 3, 'd': 4, 'b': 5}
# chain = ChainMap(data1, data2)
# print(chain['b'])
# chain['e'] = 6
# print(chain)
# print(chain.parents)
# chain.parents['e':8]
