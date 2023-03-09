from csv import DictReader, reader

import asyncio
from typing import Any

import aiofiles
from psycopg2 import connect
from psycopg2.extras import NamedTupleCursor
from psycopg2 import IntegrityError as PGIntegrityError

from sqlalchemy.exc import IntegrityError

from models import Category, Product


# async def main():
    # async with aiofiles.open('products.csv', 'r', encoding='utf-8') as file:
    #     reader = DictReader(await file.readlines())
    #     for obj in reader:
    #         cat = await Category.all(name=obj.get('category'))
    #         cat = cat[0]
    #         obj['category_id'] = cat.id
    #         del obj['category']
    #         prod = Product(**obj)
    #         try:
    #             await prod.save()
    #         except IntegrityError:
    #             print(obj)

    # async with aiofiles.open('categories.csv', 'r', encoding='utf-8') as file:
    #     reader = DictReader(await file.readlines())
    #     for line in reader:
    #         cat = Category(**line)
    #         try:
    #             await cat.save()
    #         except IntegrityError:
    #             print(line)
    # print(await Category.all())
#     print(await Product.all())
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
conn = connect('postgresql://dev:password@localhost:5432/bhcorp')


def get_category(name: str) -> tuple:
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT id, name FROM category WHERE name = %s;
        ''', (name, ))
        return cursor.fetchone()


def save_product(product: list) -> None:
    with conn.cursor() as cursor:
        cursor.execute('''
            INSERT INTO product(name, price, category_id)
            VALUES(%s, %s, %s);
        ''', product)
        try:
            conn.commit()
        except PGIntegrityError:
            print(product)


def get_products():
    with conn.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM product;
        ''')
        print(cursor.fetchall())


def load_from_csv():
    with open('products.csv', 'r', encoding='utf-8') as file:
        file.readline()
        r = reader(file)
        for obj in r:
            obj[1] = float(obj[1])
            cat = get_category(obj[2])
            obj[2] = cat[0]
            save_product(obj)


class RAWBase:
    conn = connect('postgresql://dev:password@localhost:5432/bhcorp')


class CategoryRAW(RAWBase):

    @classmethod
    def get(cls, pk: int) -> tuple[int, str]:
        with CategoryRAW.conn.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute('''
                SELECT id, name FROM category
                WHERE id = %s;
            ''', (pk, ))
            return cursor.fetchone()

    @classmethod
    def create(cls, category: str) -> None:
        with CategoryRAW.conn.cursor() as cursor:
            cursor.execute('''
                INSERT INTO category(name)
                VALUES(%s);
            ''', (category, ))
            cls.conn.commit()


# print(CategoryRAW.get(11))
# if __name__ == '__main__':
#     get_products()

from requests import Session
from aiohttp import ClientSession


class AlfaBankAPI(object):

    # @classmethod
    # def get_public_rates(cls) -> dict:
    #     with Session() as session:
    #         response = session.get(
    #             url='https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates',
    #         )
    #         print(response.headers)
    #         print(response.cookies)
    #         print(response.url)
    #         print(response.status_code)
    #         print(response.text)
    #         print(response.json())

    @classmethod
    async def get_public_rates(cls):
        async with ClientSession(
            base_url='https://developerhub.alfabank.by:8273',
        ) as session:
            response = await session.get(
                url='/partner/1.0.1/public/rates'
            )
            print(response.status)
            print(response.headers)
            print(response.cookies)
            print(await response.text())
            print(await response.json())

    @classmethod
    async def wss(cls):
        async with ClientSession(base_url='wss://demo.piesocket.com') as session:
            async with session.ws_connect(
                    url='/v3/channel_123?api_key=VCXCEuvhGcBDP7XhiJJUDvR1e1D3eiVjgZ9VRiaV&notify_self'
            ) as response:
                async for msg in response:
                    print(msg.data)
                    # await response.send_json({'key': 'value'})

from bs4 import BeautifulSoup
class Sputnik:

    @classmethod
    def get_html(cls):
        with Session() as session:
            response = session.get(url='https://sputnik.by/economy/')
            if response.status_code == 200:
                return response.text

    @classmethod
    def get_posts(cls):
        html = cls.get_html()
        if html:
            soup = BeautifulSoup(html, 'lxml')
            tags_a = soup.find_all('a', class_='list__title')
            for tag_a in tags_a:
                print(tag_a['href'])
                print(tag_a.text)


# Sputnik.get_posts()
# AlfaBankAPI.get_public_rates()
# if __name__ == '__main__':
#     asyncio.run(AlfaBankAPI.wss())