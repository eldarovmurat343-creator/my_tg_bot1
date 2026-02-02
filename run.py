import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import TOKEN
from app.handlers import router



async def main():
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    
    
    dp.include_router(router)
    
    print('Роутер подключен.')
    
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен.')
