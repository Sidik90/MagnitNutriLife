from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config.config import config
from utils.logger import logger

router = Router()


@router.callback_query(F.data == "check_sub")
async def check_subscription(callback: types.CallbackQuery):
    try:
        member = await callback.bot.get_chat_member(
            chat_id=config.channel_id, user_id=callback.from_user.id
        )

        if member.status in ["member", "administrator", "creator"]:
            builder = InlineKeyboardBuilder()
            builder.row(
                types.InlineKeyboardButton(
                    text="Записаться на консультацию",
                    callback_data="signup_consultation",
                )
            )

            await callback.message.edit_text(
                config.lead_magnet, reply_markup=builder.as_markup()
            )
            await callback.answer("Спасибо за подписку!")
            logger.info(f"Пользователь {callback.from_user.id} подписан на канал")
        else:
            await callback.answer("Вы ещё не подписались на канал!", show_alert=True)
    except TelegramBadRequest as e:
        logger.error(f"Ошибка проверки подписки: {e}")
        await callback.answer("Произошла ошибка. Попробуйте позже.", show_alert=True)
