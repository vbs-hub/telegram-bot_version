import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, LinkPreviewOptions
from hendlers.routes import router

API_TOKEN = 'ВАШ_ТОКЕН'


bot = Bot(API_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print('Start...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
