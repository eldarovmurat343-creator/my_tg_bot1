from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.state import StatesGroup, State


class App(StatesGroup):
    name = State()
    number = State()
    problem = State()
