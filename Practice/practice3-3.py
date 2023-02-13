n = int(input('n: '))
users = {
    i: {'name': input('name: '), 'email': input('email: ')}
    for i in range(n)
}
print(users)