from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random
from pyrogram import Client
import logging
import os
import csv
from dotenv import load_dotenv
from pathlib import Path
import sqlite3

conn = sqlite3.connect("chat.sqlite")
cursor = conn.cursor()

dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message()
async def log(client, message):

    if message.from_user:
        if message.photo:
            file = await app.download_media(message)
            cwd = os.getcwd()
            patch = cwd + "/message/" + str(message.chat.id) + "/"

            name_file = file

            sqlite_insert_query = """INSERT INTO Private_message
                          (id, name, message, type, date)  VALUES  (NULL, ?, ?, ?, ?)"""

            count = cursor.execute(
                sqlite_insert_query,
                (message.from_user.username, "Фото", "1", message.date),
            )
            conn.commit()

            if os.path.exists(patch + "chat.csv"):
                with open(str(patch) + "chat.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (
                            message.date,
                            message.from_user.username,
                            "Фото(" + str(name_file) + ")",
                        )
                    )
            else:
                with open(str(patch) + "chat.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (
                            message.date,
                            message.from_user.username,
                            "Фото(" + str(name_file) + ")",
                        )
                    )

        else:
            # ЛС проверка
            messagetype = message.chat.type
            if str(messagetype) == "ChatType.PRIVATE":

                # Создание папки чата
                parent_dir = "message/"
                directory = str(str(message.chat.id))

                print(parent_dir + directory)

                if os.path.exists(parent_dir + directory):
                    print("Have Folder")
                else:
                    path = os.path.join(parent_dir, directory)
                    os.mkdir(path)

                # Эмоджи
                if message.sticker:

                    cwd = os.getcwd()
                    emoji = message.sticker.emoji

                    sqlite_insert_query = """INSERT INTO Private_message
                          (id, name, message, type, date)  VALUES  (NULL, ?, ?, ?, ?)"""

                    count = cursor.execute(
                        sqlite_insert_query,
                        (message.from_user.username, emoji, "2", message.date),
                    )
                    conn.commit()

                    patch = cwd + "/message/" + str(message.chat.id) + "/"
                    if os.path.exists(patch + "chat.csv"):
                        with open(str(patch) + "chat.csv", "a") as file:
                            writer = csv.writer(file)
                            writer.writerow(
                                (message.date, message.from_user.username, emoji)
                            )
                    else:
                        with open(str(patch) + "chat.csv", "w") as file:
                            writer = csv.writer(file)
                            writer.writerow(
                                (message.date, message.from_user.username, emoji)
                            )

                # Эмоджи казик
                if message.dice:
                    cwd = os.getcwd()
                    emoji = message.dice.emoji

                    sqlite_insert_query = """INSERT INTO Private_message
                          (id, name, message, type, date)  VALUES  (NULL, ?, ?, ?, ?)"""

                    count = cursor.execute(
                        sqlite_insert_query,
                        (message.from_user.username, emoji, "3", message.date),
                    )
                    conn.commit()

                    patch = cwd + "/message/" + str(message.chat.id) + "/"
                    if os.path.exists(patch + "chat.csv"):
                        with open(str(patch) + "chat.csv", "a") as file:
                            writer = csv.writer(file)
                            writer.writerow(
                                (message.date, message.from_user.username, emoji)
                            )
                    else:
                        with open(str(patch) + "chat.csv", "w") as file:
                            writer = csv.writer(file)
                            writer.writerow(
                                (message.date, message.from_user.username, emoji)
                            )

                # Сообщения Все
                else:
                    cwd = os.getcwd()
                    patch = cwd + "/message/" + str(message.chat.id) + "/"

                    sqlite_insert_query = """INSERT INTO Private_message
                          (id, name, message, type, date)  VALUES  (NULL, ?, ?, ?, ?)"""

                    count = cursor.execute(
                        sqlite_insert_query,
                        (message.from_user.username, message.text, "3", message.date),
                    )
                    conn.commit()

                    if os.path.exists(patch + "chat.csv"):
                        with open(str(patch) + "chat.csv", "a") as file:
                            writer = csv.writer(file)
                            writer.writerow(
                                (message.date, message.from_user.username, message.text)
                            )
                    else:
                        with open(str(patch) + "chat.csv", "w") as file:
                            writer = csv.writer(file)
                            writer.writerow(
                                (message.date, message.from_user.username, message.text)
                            )
    messagetype = message.chat.type
    if str(messagetype) == "ChatType.GROUP":

        # Создание папки чатов

        parent_dir = "message/"
        directory = str(str(message.chat.title))

        print(parent_dir + directory)

        if os.path.exists(parent_dir + directory):
            print("Have Folder")
        else:
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)

        if message.sticker:

            cwd = os.getcwd()
            emoji = message.sticker.emoji
            patch = cwd + "/message/" + str(message.chat.title) + "/"
            if os.path.exists(patch + "chat.csv"):
                with open(str(patch) + "chat.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow((message.date, message.from_user.username, emoji))
            else:
                with open(str(patch) + "chat.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerow((message.date, message.from_user.username, emoji))

        if message.dice:
            cwd = os.getcwd()
            emoji = message.dice.emoji
            patch = cwd + "/message/" + str(message.chat.title) + "/"
            if os.path.exists(patch + "chat.csv"):
                with open(str(patch) + "chat.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow((message.date, message.from_user.username, emoji))
            else:
                with open(str(patch) + "chat.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerow((message.date, message.from_user.username, emoji))

        # Обычные сообщения
        else:
            cwd = os.getcwd()
            patch = cwd + "/message/" + str(message.chat.title) + "/"
            if os.path.exists(patch + "chat.csv"):
                with open(str(patch) + "chat.csv", "a") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (message.date, message.from_user.username, message.text)
                    )
            else:
                with open(str(patch) + "chat.csv", "w") as file:
                    writer = csv.writer(file)
                    writer.writerow(
                        (message.date, message.from_user.username, message.text)
                    )
    else:
        print(message)


app.run()
