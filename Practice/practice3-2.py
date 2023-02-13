letters = input('буквы: ')
result = {key: letters.count(key) for key in set(letters)}
print(result)

words = ('words', 'hello', 'python', 'words', 'hello', 'python', 'words', 'hello', 'python')
result = {w: words.count(w) for w in set(words)}
print(result)


