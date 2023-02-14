# Вывести первые N чисел кратные M и больше K

# N = int(input('N:'))
# M = int(input('M:'))
# K = int(input('K:'))
#
# numbers = []
# while len(numbers) < N:
#     if K % M == 0:
#         numbers.append(K)
#         K += M
#     else:
#         K += 1
# print(numbers)

# НЕПРАВИЛЬНОЕ БАРАХЛО
# for i in range(10):
#     i = 0
#     if i % M == 0 and i > K:
#     i += 1
#     print(i)

# ПРОСТОЙ КАЛЬКУЛЯТОР
# print('Калькулятор')
# while True:
#     s = input("Операция (+,-,*,/): ")
#     if s in ('+', '-', '*', '/'):
#         x = float(input("x="))
#         y = float(input("y="))
#         if s == '+':
#             print(x+y)
#         elif s == '-':
#             print(x-y)
#         elif s == '*':
#             print(x*y)
#         elif s == '/':
#             if y != 0:
#                 print(x/y)
#             else:
#                 print("На ноль делить нельзя!")
#     else:
#         print("Неверный знак операции!")


# TASK 3

# N = int(input('N:'))
# VAR 1
# count = 0
# for number in range(2, N+1, 2):
#     if count % 5 == 0:
#         print()
#         count +=1
#         print(number, end=' ')

# VAR2
# for number in range(2, N+1, 2):
#     print(number, end=' ')
#     if number % 10 == 0:
#         print()

# VAR3
# for i in range(2, N+1, 10):
#     for j in range(i, i+9, 2):
#         if j <= N:
#             print(j, end=' ')
#         else:
#             break
# print()