from aiogram.fsm.state import StatesGroup, State


class OpenaiStatesGroup(StatesGroup):
    game_start = State()
    prompt = State()
    flag = State()
    image_generation = State()


class ZhmyhStatesGroup(StatesGroup):
    zhmyh_start = State()
    zhmyh = State()

