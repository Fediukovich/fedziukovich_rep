# class User:
#
#     role = 'user'
#
#     def __init__(self, name, email, age):
#         if not isinstance(name, str):
#             raise TypeError('argument `name` must be string')
#         if not isinstance(email, str):
#             raise TypeError('argument `email` must be string')
#         if not isinstance(age, int):
#             raise TypeError('argument `age` must be integer')
#         if age < 18:
#             raise ValueError('argument `age` must ge great then 18')
#         self.first_name = name.title()
#         self.email = email.lower()
#         self.age = age
#
#     def __str__(self):
#         return f'User: {self.first_name=} {self.email=} {self.age=}'
#
#     def __len__(self):
#         return self.age ** 2
#
#     def __getitem__(self, item):
#         return getattr(self, item)
#
#     def __add__(self, other):
#         if isinstance(other, int | float):
#             return self.age + other
#         elif isinstance(other, User):
#             return self.age + other.age
#
#     def __radd__(self, other):
#         self.__add__(other)

    # def __eq__(self, other):
    #     if isinstance(other, int | float):
    #         return self.age == other
    #     elif isinstance(other, User):
    #         return self.age == other.age
    #
    # def __gt__(self, other):
    #     if isinstance(other, int | float):
    #         return self.age < other
    #     elif isinstance(other, User):
    #         return self.age < other.age

    # @classmethod
    # def change_role(cls, role):
    #     cls.role = role


# vasya = User('vasya', 'vasya@info.com', 35)
# pavel = User('pavel', 'pavel@info.com', 24)
# print(vasya + pavel)
# print(vasya + 35)
# print(vasya > pavel)
# print(vasya > 75)
# print(vasya.info())
# print(pavel.info())
# vasya.change_role('admin')
# print(pavel.role)
# print(len(pavel))
# print(vasya['first_name'])
# print(vasya)

# class MyClass:

#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self, arg, arg2):
#         self.arg = arg
#         self.arg2 = arg2
#
#
# obj = MyClass('singleton', 1)
# # print(obj.arg2)
# obj2 = MyClass('singleton', 2)
# print(obj2.arg2)
# print(obj.arg2)
# print(obj is obj2)


# class User:
#
#     def __init__(self, name, email, age, city):
#         self.name = name.title()
#         self.email = email.lower()
#         self.age = age
#         self.city = city.title()
#
#     def dict(self):
#         return {
#             'name': self.name,
#             'email': self.email,
#             'age': self.age,
#             'city': self.city
#         }
#
#
# vasya = User('vasya', 'vasya@info.com', 34, 'Minsk')
# print(vasya.dict())

# age: int = 34
#
#
# def is_palindrome(text: str) -> bool:
#     """Проверка текста на палиндром
#
#     :param text: строка для проверки
#     :return: True - если text палиндром, иначе False
#     """
#     return text == text[::-1]


# class Person:
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __str__(self):
#         return f'Person {self.name=} {self.email=}'
#
#     def dict(self):
#         return {'name': self.name, 'email': self.email}
#
#
# class Manager(Person):
#
#     def __init__(self, name, email, salary):
#         super().__init__(name, email)
#         self.salary = salary
#
#     def __int__(self):
#         return self.salary
#
#
# vasya = Manager('vasya', 'vasya@info.com', 1500)
# print(vasya.dict())
#
# print(Manager.mro())

# class Diamond:
#     pass
#
#
# class A(Diamond):
#     pass
#
#
# class B(Diamond):
#     pass
#
#
# class C(A, B):
#     pass
#
#
# class D:
#     pass
#
#
# class E(D):
#     pass
#
#
# class F(C, E):
#     pass
#
#
# class A:
#
#     def info(self):
#         return 'A'
#
#
# class C(A):
#     pass
#
#
# class B(A):
#
#     def info(self):
#         res = super(B, self).info()
#         res += 'B'
#         return res
#
#
# b = B()
# print(b.info())
#
#
# class Category:
#
#     @classmethod
#     def all(cls):
#         return ('cat1', 'cat2', 'cat3', 'cat4')
#
#
# class Product:
#
#     @classmethod
#     def all(cls):
#         return ('prod1', 'prod2', 'prod3', 'prod4')
#
#
# def paginator(obj: Category | Product):
#     instances = obj.all()
#     iter_instances = iter(instances)
#     return [*zip(iter_instances, iter_instances)]
#
#
# print(paginator(Category()))


# class API:
#
#     def __get_response(self, **kwargs):
#         print(f'совершаю гет запрос {kwargs}')
#
#     def get(self, **kwargs):
#         print('pre process')
#         self.__get_response(**kwargs)
#
#
# class APIV2(API):
#     pass
#
#
# api = API()
# api._API__get_response()
#
#
# class API:
#
#     def __init__(self, token):
#         self.__token = token
#
#     @property
#     def token(self):
#         return self.__token[:6] + '*' * (len(self.__token) - 6)
#
#     @token.setter
#     def token(self, value):
#         if not isinstance(value, str):
#             raise TypeError('argument `token` must be string')
#         self.__token = value
#
# # Композиция (агрегация)
#
# class Button:
#
#     def __init__(self, text: str, color: str, size: tuple[int, int]) -> None:
#         self.text = text
#         self.color = color
#         self.size = size
#
#     def __str__(self):
#         return self.text
#
#     def dict(self) -> dict:
#         return {
#             'text': self.text,
#             'color': self.color,
#             'size': self.size
#         }
#
#     def scale(self, delta: float) -> None:
#         self.size = self.size[0] * delta, self.size[1] * delta
#
#
# class Keyboard:
#
#     buttons = []
#
#     @classmethod
#     def create_button(
#             cls,
#             text: tuple[str],
#             colors: tuple[str],
#             sizes: tuple[tuple[int, int]]
#     ) -> list[Button]:
#         buttons = [
#             Button(text[1], colors[i], sizes[i])
#             for i in range(len(text))
#         ]
#         cls.buttons.extend(buttons)
#         return buttons
#
#
# # Ассоциация
#
#
# class Engine:
#
#     def __init__(self, volume):
#         self.volume = volume
#
#
# class Car:
#
#     def __init__(self, engine: Engine):
#         self.engine = engine
#
#
# eng = Engine(5)
# bwm = Car(eng)