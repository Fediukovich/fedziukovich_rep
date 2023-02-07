text = 'Hello, my name is Artem'
print(text)
print(text.replace(' ', '-'))

text = '-'.join(text)
print(text)

text = 'my name Artem'
print('Hello, ', text, sep='-')

text = 'Hello, my name is Artem'
print("-".join(text.split()))