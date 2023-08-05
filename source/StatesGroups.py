from aiogram.fsm.state import StatesGroup, State


class GameStatesGroups(StatesGroup):
    game_start = State()
    prompt = State()
    flag = State()


class ZhmyhStatesGroup(StatesGroup):
    zhmyh_start = State()
    zhmyh = State()
