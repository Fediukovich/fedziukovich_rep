# # from sqlite3 import connect
# #
# #
# # conn = connect('db.sqlite3')
# # cur = conn.cursor()
# #
# # cur.execute('''
# #     CREATE TABLE IF NOT EXISTS categories(
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         name VARCHAR(64) UNIQUE NOT NULL
# #     );
# # ''')
# # conn.commit()
# #
# # # cur.executemany('''
# # #     INSERT INTO categories(name) VALUES(?);
# # # ''', (('Coffee', ), ('Sandwich', )))
# # # conn.commit()
# #
# # cur.execute('''
# #     SELECT * FROM categories;
# # ''')
# # print(cur.fetchall())
# from psycopg2 import connect
# from psycopg2.extras import NamedTupleCursor
#
# DB_URL = 'postgresql://dev:password@localhost:5432/bhcorp'
# # conn = connect(name='dev', password='password', host='localhost', dbname='bhcorp')
# conn = connect(DB_URL)
# # cur = conn.cursor()
#
# # with conn.cursor() as cur:
# #     cur.execute('''
# #         CREATE TABLE IF NOT EXISTS categories(
# #             id SERIAL PRIMARY KEY,
# #             name VARCHAR(64) UNIQUE NOT NULL
# #         );
# #     ''')
# #     conn.commit()
#
# # with conn.cursor() as cur:
# #     cur.execute('''
# #         INSERT INTO categories(name) VALUES(%s);
# #     ''', ('Coffee', ))
# #     conn.commit()
#
# with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
#     cur.execute('''
#         SELECT * FROM categories;
#     ''')
#     data = cur.fetchall()
#     # print(data[0].name)