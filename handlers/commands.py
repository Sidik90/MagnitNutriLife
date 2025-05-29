from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config.config import config
from utils.logger import logger
from services.scheduler import schedule_consultation_invite

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        builder = InlineKeyboardBuilder()
        builder.row(
            types.InlineKeyboardButton(
                text="Подписаться на канал", url=config.channel_invite_link
            )
        )
        builder.row(
            types.InlineKeyboardButton(
                text="Я подписался ✅", callback_data="check_sub"
            )
        )

        await message.answer(config.welcome_message, reply_markup=builder.as_markup())

        # Запланировать приглашение на консультацию
        await schedule_consultation_invite(message.from_user.id)

        logger.info(f"Новый пользователь: {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка в обработчике start: {e}", exc_info=True)
        await message.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")
