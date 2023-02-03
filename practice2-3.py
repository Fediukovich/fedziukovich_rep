name = 'Artem'
age = 34
city = 'Minsk'
text1 = 'Hello, my name is %s, my age is %d, i am from Minsk' % (name, age)
text2 = 'Hello, my name is {}, age {}, from {}'.format(name, age, city)
text3 = f'Hello, i am from {city}, my name is {name}, my age is {age}'
print(text1)
print(text2)
print(text3)