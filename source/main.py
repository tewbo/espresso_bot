import asyncio
import logging

import pymysql
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from routes import *

bot = Bot(config.token)


async def set_default_commands():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Узнать возможности бота'),
        types.BotCommand(command='zhmyh', description='Жмыхнуть изображение'),
        types.BotCommand(command='game', description='Поиграть в игру с ChatGPT')
    ])


def db_connect():
    try:
        connection = pymysql.connect(
            host=config.host,
            port=config.port,
            user=config.user,
            password=config.password,
            database=config.db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Successfully connected to database!")
    except Exception as ex:
        print("Connection refused...")
        print(ex)
        exit(0)


def get_storage():
    return MemoryStorage()


def get_kb():
    reply = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Жмыхнуть изображение"),
                KeyboardButton(text="Поиграть в игру с ChatGPT")
            ]
        ],
        resize_keyboard=True)
    inline = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Жмыхнуть изображение", callback_data="zhmyh"),
                InlineKeyboardButton(text="Поиграть в игру с ChatGPT", callback_data="game")
            ],
            [
                InlineKeyboardButton(text="Посмотреть статистику", callback_data="stats")
            ]
        ]
    )
    return reply


async def main() -> None:
    # db_connect()
    storage = get_storage()
    dp = Dispatcher(storage=storage)
    dp.include_router(router)
    await set_default_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
