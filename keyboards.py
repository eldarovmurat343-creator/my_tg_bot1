from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton,
                          )

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



def main_kb():
    kb = ReplyKeyboardBuilder()
    kb.button(text="✍🏼 Оставить заявку")
    return kb.as_markup(resize_keyboard=True) 


def cancel_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="❌ Отмена", callback_data="cancel_order")
    return builder.as_markup()


def get_app_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='✍🏼 Оставить заявку')]
        ],
        resize_keyboard=True,
        input_field_placeholder='Напишите вашу заявку...',
        one_time_keyboard=True
    
        
    )


def get_number_kb():
    kb = ReplyKeyboardBuilder()
    
    kb.button(text="📱 Отправить номер", request_contact=True)
  
    kb.button(text="❌ Отмена")
    kb.adjust(1) 
    return kb.as_markup(resize_keyboard=True)

