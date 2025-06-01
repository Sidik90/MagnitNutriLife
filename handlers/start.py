from aiogram import Router, F, Bot
from aiogram.types import Message
from keyboards.builders import welcome_keyboard
from services.subscription import check_subscription

router = Router()


@router.message(F.text == "/start")
async def cmd_start(message: Message, bot: Bot):
    welcome_text = """
🌟 <b>Добро пожаловать в "НутриЛайф"!</b> 🌟
"НутриЛайф" — это больше, чем просто канал о нутрициологии 🌟. Это ваше вдохновение на пути к здоровому образу жизни 🏃‍♂️🌿

Подпишитесь на наш канал, чтобы получить подарок! 👇
"""
    await message.answer(
        welcome_text,
        reply_markup=welcome_keyboard(),
    )
    await check_subscription(bot, message.from_user.id)
