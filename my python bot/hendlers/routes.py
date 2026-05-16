from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message, 
    CallbackQuery,
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    LinkPreviewOptions
)

HELP_TEXT = (
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

GIT_SURS = (
    '📦 <b>Код программы:</b>\n\n'
    '🚀 Все версии будут публиковаться тут'
)

INFO_TEXT = (
    "<b>📂 Информация о системе</b>\n"
    "\n"
    f"👑 <b>Хозяин:</b> @OxFF_Dev (<code>1337</code>)\n"
    "\n"
    f"🤖 <b>Версия бота:</b> <code>1.3 beta</code>\n"
    "⚙️ <b>Статус:</b> Работает стабильно"
)

router = Router()

# --- Клавиатуры ---

def get_main_inline_reply():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='🛃 Помощь', callback_data='help')],
            [InlineKeyboardButton(text='📫 Данные', callback_data='info')]
        ]
    )

def get_surs_inline_reply():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='📦 Исходный код', callback_data='surs')]
        ]
    )

def get_surs_2_inline():
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='🔹 Сылка на github 🔹', url='https://github.com/vbs-hub/telegram-bot_version/')]

            ]
        )

def get_main_kb():
    buttons = [
        [KeyboardButton(text="📽️ YouTube"), KeyboardButton(text="💻 Gemini")],
        [KeyboardButton(text="📖 Yandex"), KeyboardButton(text="🎱 Biliard")],
        [KeyboardButton(text="🚗 Car Game")],
        [KeyboardButton(text="📫 Info"), KeyboardButton(text="🛃 Help")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Commands & Messages ---

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(
        'Привет! Я Python Бот. Выбери нужное приложение на клавиатуре ниже:', 
        reply_markup=get_main_kb()
    )

@router.message(F.text == '🛃 Help')
async def help_handler(message: Message):
    await message.answer(
        HELP_TEXT,
        parse_mode="HTML",
        reply_markup=get_main_inline_reply()
    )

@router.callback_query(F.data == 'help')
async def help_inl(callback: CallbackQuery):
    await callback.answer()  # Гасим часики сразу
    await callback.message.edit_text(HELP_TEXT, parse_mode="HTML", reply_markup=get_main_inline_reply())

@router.message(F.text == '1.3 beta')
async def sors(message: Message):
    await message.answer(
        GIT_SURS, 
        parse_mode='HTML', 
        link_preview_options=LinkPreviewOptions(is_disabled=True),
        reply_markup=get_surs_2_inline()
    )

@router.callback_query(F.data == 'surs')
async def inline_surs(callback: CallbackQuery):
    await callback.answer()  # Гасим часики
    await callback.message.answer(
        GIT_SURS,
        parse_mode='HTML',
        link_preview_options=LinkPreviewOptions(is_disabled=True),
        reply_markup=get_surs_2_inline()  # <-- ДОБАВИЛИ ЭТУ СТРОКУ
    )

@router.callback_query(F.data == 'info')
async def lin_info(callback: CallbackQuery):
    await callback.answer()  # Гасим часики
    await callback.message.answer(
        INFO_TEXT,
        parse_mode="HTML",
        reply_markup=get_surs_inline_reply()
    )

@router.message(F.text == '📫 Info')
async def info(message: Message):
    # Исправлено: добавлена инлайн-клавиатура к сообщению
    await message.answer(
        INFO_TEXT, 
        parse_mode='HTML',
        reply_markup=get_surs_inline_reply()
    )

# --- Mini apps ---
@router.message(F.text == '📽️ YouTube')
async def youtube(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/youtube">📽️ YouTube</a>', parse_mode="HTML")

@router.message(F.text == '💻 Gemini')
async def gemini(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/gemini">💻 Gemini</a>', parse_mode="HTML")

@router.message(F.text == '📖 Yandex')
async def yandex(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/yndex">📖 Yandex</a>', parse_mode="HTML")

@router.message(F.text == '🎱 Biliard')
async def biliard(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/biliard">🎱 Biliard</a>', parse_mode="HTML")

@router.message(F.text == '🚗 Car Game')
async def car_game(message: Message):
    await message.answer('<a href="t.me/python_code_ny_bot/game7">🚗 Car Game</a>', parse_mode="HTML")