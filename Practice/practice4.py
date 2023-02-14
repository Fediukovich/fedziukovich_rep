# Вывести первые N чисел кратные M и больше K

N = int(input('N:'))
M = int(input('M:'))
K = int(input('K:'))
for i in range(N):
    count = 0
    if i % M == 0 and i > K:
    count += 1
    print(count)

# ПРОСТОЙ КАЛЬКУЛЯТОР
print('Калькулятор')
while True:
    s = input("Операция (+,-,*,/): ")
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print(x+y)
        elif s == '-':
            print(x-y)
        elif s == '*':
            print(x*y)
        elif s == '/':
            if y != 0:
                print(x/y)
            else:
                print("На ноль делить нельзя!")
    else:
        print("Неверный знак операции!")