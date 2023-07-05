import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from routes import *

with open("SECRET_TOKEN.txt") as file:
    TOKEN = file.read()
bot = Bot(TOKEN, parse_mode="MarkDown")


async def set_default_commands():
    await bot.set_my_commands([
        types.BotCommand(command='start', description='Узнать возможности бота')
    ])


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)

    await set_default_commands()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
