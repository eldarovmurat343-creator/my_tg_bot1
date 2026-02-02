from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from app.states import App
import app.keyboards as kb
from config import ADMIN_ID


router = Router()


@router.message(CommandStart())
async def cmd_str(message: Message):
    await message.answer(
        '\nПривет, здесь вы можете подать заявку!\n'
        f'Просто нажмите кнопку "✍🏼 Оставить заявку"',
        reply_markup=kb.main_kb()
)
    
@router.message(F.photo)
async def photo_hd(message: Message):
    await message.answer('Красивое фото! Но для заявки мне нужен текст.')


@router.message(F.text == "✍🏼 Оставить заявку")
async def start_order(message: Message, state: FSMContext):
    await state.set_state(App.name) 
    await message.answer("Отлично! Как вас зовут?", reply_markup=kb.cancel_kb())


@router.message(App.number, F.text == "❌ Отмена")
async def cancel_at_number_step(message: Message, state: FSMContext):
    await state.clear()

    await message.answer("Заявка отменена.", reply_markup=kb.main_kb())


@router.message(App.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(App.number)
    await message.answer('Нажмите на кнопку ниже, чтобы отправить номер', 
                         reply_markup=kb.get_number_kb())
    
    
@router.message(App.number, F.contact)
async def get_number(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    await state.set_state(App.problem)
    await message.answer(
        'Теперь опишите вашу проблему пожалуйста',
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer('Используйте кнопку ниже, если передумали', 
                         reply_markup=kb.cancel_kb()
)


@router.message(App.problem)
async def get_problem(message: Message, state: FSMContext):
    await state.update_data(problem=message.text)
    data = await state.get_data()
    
    admin_text = (
        f"🚨 **Новая заявка!**\n\n"
        f"👤 Имя: {data['name']}\n"
        f"📞 Номер: {data['number']}\n"
        f"❓ Проблема: {data['problem']}"
    )
    
   
    await message.bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="Markdown")
    
    
    await message.answer("✅ Ваша заявка отправлена администратору! Мы скоро свяжемся с вами."
                          )
    
    await state.clear()


@router.callback_query(F.data == 'cancel_order')
async def cancel_handler(callback: CallbackQuery, state: FSMContext):
    
    await state.clear()

    await callback.message.delete()
    
    await callback.message.answer(
        'Действие отменено. Вы вернулись в главное меню.',
        reply_markup=kb.main_kb()
    )
    
    await callback.answer()

