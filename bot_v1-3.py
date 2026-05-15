import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = 'ВАШ_ТОКЕН'


bot = Bot(API_TOKEN)
dp = Dispatcher()

def get_main_kb():
    buttons = [
        [KeyboardButton(text="📽️ YouTube"), KeyboardButton(text="💻 Gemini")],
        [KeyboardButton(text="📖 Yandex"), KeyboardButton(text="🎱 Biliard")],
        [KeyboardButton(text="🚗 Car Game"), KeyboardButton(text="🛃 Help")],
        [KeyboardButton(text="📫 Info")]
    ]
    # resize_keyboard=True делает кнопки маленькими и аккуратными
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# Commands
@dp.message(Command('start'))
async def start(message: Message):
    await message.answer('Привет! Я Python Бот. Выбери нужное приложение на клавиатуре ниже:', 
                         reply_markup=get_main_kb())

@dp.message(F.text == '🛃 Help')
async def help_handler(message: Message):
    # Используем многострочную строку для удобства редактирования
    help_text = (
        "<b>📂 Проводник по боту</b>\n\n"
        "<b>🤖 Команды:</b>\n"
        "<code>/start</code> — запуск бота\n"
        "<code>🛃 help</code> — помощь\n"
        "<code>📫 info</code> — данные\n\n"
        "<b>📱 Приложения (кнопки):</b>\n"
        "1️⃣ — <code>📽️ YouTube</code>\n"
        "2️⃣ — <code>💻 Gemini</code>\n"
        "3️⃣ — <code>📖 Yandex</code>\n"
        "4️⃣ — <code>🎱 Biliard</code>\n"
        "5️⃣ — <code>🚗 Car Game</code>"
    )
    
    await message.answer(
        help_text,
         parse_mode="HTML", # Включаем поддержку жирного шрифта и кода
        reply_markup=get_main_kb()
    )

@dp.message(F.text == '1.3 beta')
async def sors(message: Message):
    git_surs = (
        '📦 <b>Код программы:</b>\n\n'
        '🚀 Все версии будут публиковаться тут:\n'
        '🔹 <a href="https://github.com/vbs-hub/telegram-bot_version/blob/main">MY GITHUB</a>'
    )
    await message.answer(git_surs, parse_mode='HTML')

@dp.message(F.text == '📫 Info')
async def info(message: Message):
    info_text = (
        "<b>📂 Информация о системе</b>\n"
        "\n"
        f"👑 <b>Хозяин:</b> @OxFF_Dev (<code>1337</code>)\n"
        f"👤 <b>Пользователь:</b> {message.from_user.first_name}\n"
        "\n"
        f"🤖 <b>Версия бота:</b> <code>1.3 beta</code>\n"
        "⚙️ <b>Статус:</b> Работает стабильно"
    )
    await message.answer(info_text, parse_mode='HTML')

#Mini apps
@dp.message(F.text == '📽️ YouTube')
async def youtube(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/youtube">📽️ YouTube</a>', parse_mode="HTML")
@dp.message(F.text == '💻 Gemini')
async def gemini(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/gemini">💻 Gemini</a>', parse_mode="HTML")
@dp.message(F.text == '📖 Yandex')
async def yandex(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/yndex">📖 Yandex</a>', parse_mode="HTML")
@dp.message(F.text == '🎱 Biliard')
async def biliard(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/biliard">🎱 Biliard</a>', parse_mode="HTML")
@dp.message(F.text == '🚗 Car Game')
async def car_game(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/game7">🚗 Car Game</a>', parse_mode="HTML")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    print('Start...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
