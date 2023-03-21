# def read_file():
#     with (
#         open('log.log', 'r', encoding='utf-8') as file,
#         open('out6.log', 'a', encoding='utf-8') as outfile
#     ):
#         for log in file:
#             outfile.write(log)
#
#
# read_file()
#
# # with open('log.log', 'a', encoding='utf-8') as file:
# #     while True:
# #         file.write('[12:24]Файл отправлен\n')
# #
# #
# #
# #
# # import aiofiles
# # from asyncio import Queue, run, create_task
# #
# # q = Queue()
# # #
# # #
# # async def write_log():
# #     async with aiofiles.open('out5.log', 'a', encoding='utf-8') as file:
# #         while True:
# #             log = q.get()
# #             await file.write(log)
# #
# #
# # async def read_file():
# #     async with aiofiles.open('log.log', 'r', encoding='utf-8') as file:
# #         async for log in file:
# #             if 'Файл отправлен' in log:
# #                 await q.put(log)
# #
# #
# # async def main():
# #     tasks = [create_task(read_file()), create_task(write_log())]
# #     for task in tasks:
# #         await task
# #
# #
# # if __name__ == '__main__':
# #     run(main())
import json

import aiofiles
from aiohttp import ClientSession

# async def get_response():
#     async with ClientSession() as session:
#         async with aiofiles.open('yandex_mail.json', 'r', encoding='utf-8') as file:
#             data = json.loads(await file.read())
#         response = await session.post(
#             url='https://mail.yandex.ru/web-api/models/liza1?_m=folders%2Clabels%2Cmessages%2Cstickers%2Ctabs',
#             **data
#             )
#         data = await response.json()
#         print(data.get('models')[0].get('data').get('folder')[0].get('count'))
#
#
import asyncio


# asyncio.run(get_response())


async def get_renault_captur():
    async with ClientSession() as session:
        response = await session.get(url='https://cars.av.by/renault/captur')
        print(await response.text())


# asyncio.run(get_renault_captur())

# rzsiyjkqknkanjvy


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'pratayeu@yandex.ru'
msg['To'] = 'pratayeu.a@gmail.com'
msg['Subject'] = 'Тест скрипта SMTP'
message = 'Это тестовое сообщение и отвечать на него не нужно'
msg.attach(MIMEText(message))
mailserver = smtplib.SMTP('smtp.yandex.ru', 587)
mailserver.ehlo()
mailserver.starttls()
mailserver.ehlo()
mailserver.login('pratayeu@yandex.ru', 'app_password')
mailserver.sendmail('pratayeu@yandex.ru', 'pratayeu.a@gmail.com', msg.as_string())