# from abc import ABC, abstractmethod
#
#
# class Paginator(ABC):
#
#     def __str__(self):
#         return self.name
#
#     @abstractmethod
#     def get_queryset(self, *args, **kwargs) -> list:
#         pass
#
#     @property
#     @abstractmethod
#     def name(self) -> str:
#         pass
#
#
# class CategoryPaginator(Paginator):
#
#     @property
#     def name(self) -> str:
#         return 'Category'
#
#     def get_queryset(self, *args, **kwargs) -> list:
#         return []
#
#
# paginator = CategoryPaginator()
# print(paginator)

# paginator = Paginator()
#
#
# from dataclasses import dataclass, field
#
#
# @dataclass(frozen=True)
# class User:
#     name: str
#     email: str
#     age: int
#     lang: str = field(default='en', repr=False)
#
#     def info(self):
#         return self.name
#
# from datetime import datetime
# from pydantic import BaseModel, EmailStr, Field, validator, root_validator
# from pydantic.types import Decimal
#
#
# class UserModel(BaseModel):
#     name: str
#     email: EmailStr
#     age: int = Field(ge=18, lt=80)
#     password: str
#     register_date: datetime
#
    # @validator('password')
    # def validate_password(cls, value):
    #     for i in value:
    #         if i.isdigit():
    #             break
    #     else:
    #         raise ValueError('not digit in password')
    #     return value
#
#     @root_validator
#     def validate_data(cls, values):
#         if values.get('name').lower() in values.get('password').lower():
#             raise ValueError('имя не должно содержаться в пароле')
#         return values
#
    # @validator('register_date')
    # def validate_register_date(cls, value):
    #     if isinstance(value, (int, float)):
    #         return datetime.fromtimestamp(value)
        # elif isinstance(value, datetime):
        #     return value
        # else:
#             raise TypeError
#
#
# class ProductModel(BaseModel):
#     name: str
#     descr: str
#     price: Decimal = Field(max_digits=8, decimal_places=2)
#
#
# class CategoryModel(BaseModel):
#     name: str = Field(min_length=4)
#     products: list[ProductModel] = None
#     category: "CategoryModel" = None
#
#
# CategoryModel.update_forward_refs()
#
# data = {
#     'name': 'auto',
#     'products': [
#         {
#             'name': 'prod1',
#             'descr': 'descr1',
#             'price': 184.4
#         }
#      ],
#     'category': {
#         'name': 'Cate'
#     }
# }

# category = CategoryModel(**data)


# def __str__(self):
#     return self.name
#
#
# User = type('User', (), {'__str__': __str__, 'name': None})
#
#
# vasya = User()
# vasya.name = 'Vasya'
# print(vasya)
#
#
# def my_metaclass(name, bases, attrs):
#     print(name)
#     print(bases)
#     print(attrs)
#
#     attrs = dict([(key.upper(), val) for key, val in attrs.items()])
#     return type(name, bases, attrs)


# class MyMetaclass(type):
#
#     def __new__(mcs, future_class_name, future_class_parents, future_class_attr, **kwargs):
#         attrs = dict(((name.upper(), value) for name, value in (future_class_attr | kwargs).items()))
#         return super(MyMetaclass, mcs).__new__(mcs, future_class_name, future_class_parents, attrs)
#
#     def __init__(self, name, bases, attrs, **kwargs):
#         super(MyMetaclass, self).__init__(self)
#
#     @classmethod
#     def __prepare__(mcs, name, bases, **kwargs):
#         return super().__prepare__(mcs, name, bases, kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         return super(MyMetaclass, cls).__call__(*args, **kwargs)
#
#
# class User(metaclass=MyMetaclass):
#
#     name: str
#
#     def __str__(self):
#         return self.name
#
#     def __init__(self, surname):
#         self.surname = surname
#
#
# vasya = User(surname='petrov')
# petya = User(surname='nepertrov')
# print(vasya.NAME)
# print(petya)
# from io import BytesIO
#
# file = open('input.txt', 'r', encoding='utf-8')
# print([line.strip() for line in file if line.strip()])
# file.seek(0)
# print(file.read())
# file.close()

# with open('input.txt', 'a', encoding='utf-8') as file:
#     file.write('\nfinish')
#
# from json import dumps, dump, loads, load
#
# with open('input.json', 'r', encoding='utf-8') as file:
#     data = load(file)
#     print(data.get('name'))
#
# with open('output.json', 'w', encoding='utf-8') as file:
#     data = {
#         'name': 'Морган',
#         'surname': 'Freeman',
#         'age': 65
#     }
#     dump(data, file, indent=2, ensure_ascii=False)
# from csv import reader, DictReader, writer, DictWriter, Dialect
#
#
# with open('users.csv', 'r', encoding='utf-8') as file:
#     for line in DictReader(file):
#         print(line)
#
# with open('output.csv', 'w', encoding='utf-8') as file:
#     data = [
#         {'name': 'alex', 'surname': 'petrov'},
#         {'name': 'pavel', 'surname': 'freeman'}
#     ]
#     wr = DictWriter(file, fieldnames=['name', 'surname'], delimiter=';')
#     wr.writeheader()
#     wr.writerows(data)
# from yaml import safe_load, safe_dump
#
# with open('input.yaml', 'r', encoding='utf-8') as file:
#     data = safe_load(file)
#     print(data)
#
# with open('output.yaml', 'w', encoding='utf-8') as file:
#     data = {
#         'name': 'alex',
#         'is_human': True,
#         'lang': ['ru', 'en']
#     }
#     safe_dump(data, file)


# from configparser import ConfigParser
#
#
# parser = ConfigParser()
# parser.read('config.ini')
# data = {
#     'FIRST_SECTION': {
#         'first_option': 'first_value',
#         'first_option2': 'first_value2',
#     },
#     'SECOND_SECTION0': {
#         'third_option': 'third_value'
#     }
# }
# parser.read_dict(data)
# with open('output.ini', 'w') as file:
#     parser.write(file, space_around_delimiters=False)
# print(parser.sections())
# print(parser['FIRST']['key'])
# print(parser.get('FIRST', 'key2'))