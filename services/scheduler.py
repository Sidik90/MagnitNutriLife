import asyncio
from aiogram import Bot, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config.config import config
from utils.logger import logger


async def send_consultation_invite(bot: Bot, user_id: int):
    try:
        builder = InlineKeyboardBuilder()
        builder.row(
            types.InlineKeyboardButton(
                text="Записаться на консультацию", callback_data="signup_consultation"
            )
        )

        await bot.send_message(
            user_id, config.consultation_message, reply_markup=builder.as_markup()
        )
        logger.info(f"Отправлено приглашение пользователю {user_id}")
    except Exception as e:
        logger.error(f"Не удалось отправить приглашение {user_id}: {e}")


async def schedule_consultation_invite(user_id: int, bot: Bot):
    await asyncio.sleep(config.consultation_delay)
    await send_consultation_invite(bot, user_id)
