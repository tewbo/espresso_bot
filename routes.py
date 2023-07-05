import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.types import FSInputFile
from main import bot
from carving import make_carving
from PIL import Image

router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, *{message.from_user.full_name}*!\n"
                         f"Этот бот умеет жмыхать изображения.\n"
                         f"Просто пришли изображение, которое нужно жмыхнуть.")


@router.message(F.photo)
async def picture_handler(message: types.Message) -> None:
    picture_name = "file.jpg"
    await bot.download(message.photo[-1], f"images/{picture_name}")
    await message.answer("Ваше изображение жмыхается...")
    try:
        make_carving(picture_name)
        carved_picture = FSInputFile(f"result/{picture_name}")
        await bot.send_photo(chat_id=message.chat.id, photo=carved_picture)
    except ValueError as e:
        await message.answer(e.args[0])


@router.message()
async def text_message_handler(message: types.Message) -> None:
    await message.answer("Пожалуйста, пришлите картинку.")
