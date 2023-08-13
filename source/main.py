import asyncio
import logging

import pymysql
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

import config
from routes import *

bot = Bot(config.token)


async def set_default_commands():
    await bot.set_my_commands([
        types.BotCommand(command='help', description='Узнать возможности бота'),
        types.BotCommand(command='zhmyh', description='Жмыхнуть изображение'),
        types.BotCommand(command='game', description='Поиграть в игру с ChatGPT'),
        types.BotCommand(command='image', description='Сгенерировать изображение'),
        types.BotCommand(command='diffusion', description='Сгенерировать изображение в Stable Diffusion'),
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
                KeyboardButton(text="Поиграть в игру с ChatGPT"),
                # KeyboardButton(text="Сгенерировать изображение")
            ]
        ],
        resize_keyboard=True)
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
