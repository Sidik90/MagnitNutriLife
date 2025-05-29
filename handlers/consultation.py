from aiogram import Router, types
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config.config import config
from utils.logger import logger

router = Router()


@router.callback_query(F.data == "signup_consultation")
async def signup_consultation(callback: types.CallbackQuery):
    try:
        builder = InlineKeyboardBuilder()
        builder.row(
            types.InlineKeyboardButton(
                text="Написать в Telegram",
                url=f"https://t.me/K_Marina_KMV",
            )
        )
        builder.row(
            types.InlineKeyboardButton(
                text="Наш сайт", url="https://taplink.cc/marina_kv"
            )
        )

        await callback.message.answer(
            "Отлично! Выбери удобный способ связи:", reply_markup=builder.as_markup()
        )
        await callback.answer()

        # Уведомление админу
        await callback.bot.send_message(
            config.admin_id,
            f"Новая заявка на консультацию от @{callback.from_user.username} ({callback.from_user.id})",
        )
        logger.info(f"Новая заявка от {callback.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка при записи на консультацию: {e}", exc_info=True)
        await callback.answer("Произошла ошибка. Пожалуйста, попробуйте позже.")
