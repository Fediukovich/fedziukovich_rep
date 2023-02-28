# import pandas as pd
# # from numpy import int64, NaN
#
# # numbers = [1, 2, 3, 4, 5, 6]
# # series = pd.Series(numbers, index=('a', 'b', 'c', 'd', 'e', 'f'))
# # series = pd.Series({'a': 1, 'b': 4, 'c': 2})
# # series2 = pd.Series({'a': 3, 'b': 4, 'c': 5})
# # print(series + series2)
# # print(series[['a', 'c']])
# # print(series[1:])
# # print(series[series >= 2].sort_values())
#
# # frame = pd.DataFrame(
# #     {
# #         'name': ['alex', 'pavel', 'misha'],
# #         'age': [35, 45, 26]
# #     }
# # )
# #
# # print(frame[frame['age'] > 26])
#
# # frame = pd.read_csv('users.csv')
# # frame.to_excel('output.xlsx', sheet_name='users')
# # print(frame['age'])
# # print(frame.sort_values(['age', 'name']))
# # print([*frame.groupby(['name', 'age'])])
# #
# # for user in frame.iloc:
# #     if isinstance(user['age'], int64):
# #         print(True)
#
# # from random import randint
# from utils import *
#
#
# if __name__ == '__main__':
#     bar()
# from pathlib import Path
import random
from asyncore import loop
from io import BytesIO
from urllib.parse import urlparse

# from itertools import *
#
#
# print(*compress((1, 2, 3, 4, 5), (True, False, True, False, True)))


# BASE_DIR = Path(__file__).resolve().parent
#
# # print([*os.walk('.')])
# print()

# from sys import *
#
# print(getrecursionlimit())
# setrecursionlimit(2000)
# print(getrecursionlimit())

# from datetime import datetime, date, timedelta


# my_date = datetime.now()
# my_date = my_date.replace(hour=14)
# print(my_date.strftime('%a %d %m %Y %H-%M'))

# delta = timedelta()
#
# from http import HTTPStatus
#
# print(HTTPStatus.OK)

# from enum import Enum, IntEnum
#
#
# order_statuses = (('approve', 1), ('revoke', 2), ('cancel', 3))
#
# OrderStatus = IntEnum('OrderStatus', order_statuses)
# print(OrderStatus.approve.value)

# class Season(int, Enum):
#     Winter: int = 1
#     Spring: int = 2
#     Summer: int = 3
#     Autumn: int = 4
#
#
# season = 2
# if season == Season.Spring:
#     print(True)

# from argparse import ArgumentParser
#
#
# parser = ArgumentParser()
# parser.add_argument('-p', '--port', help='Порт запуска', default='8000')
# parser.add_argument('-d', '--debug', action='store_true')
#
# args = parser.parse_args()
# print(args.port)

# import logging
#
#
# logging.basicConfig(
#     format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
# )
#
#
# logging.error('My Error')


# from calendar import *
#
#
# calendar = Calendar()
# print(calendar.monthdatescalendar(year=2023, month=2))

#
# path = urlparse('https://some-site.com/catalog/?category_id=1&product_id=5')
# path = path._replace(scheme='http')
# print(path)
# from string import *
#
#
# text = 'hello python. world pycharm'
# print(capwords(text, '. '))
#
# from array import array
#
# arr = array('b', [1, 2, 3, 4, 5, 6])
# print(arr[0])

# import matplotlib.pyplot as plt
#
#
# plt.pie(
#     [1, 2, 5],
#     colors=['red', 'blue', 'green'],
#     labels=['first', 'second', 'third'],
#     explode=[0.1, 0.1, 0.1],
#     shadow=True,
#     autopct='%1.1f%%'
# )
# axis_x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# axis_y = [100, 150, 155, 160, 157, 162, 157, 158, 169]
# plt.plot(axis_x, axis_y, color='red', label='MyPlot')
# plt.hist([0.2, 0.5, 0.3, 0.7])
# plt.show()
# ing = BytesIO()
# plt.savefig(ing)