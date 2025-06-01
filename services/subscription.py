from aiogram import Bot
from ..config.config import config

from MagnitNutriLife.keyboards.builders import gifts_keyboard, welcome_keyboard


async def check_subscription(bot: Bot, user_id: int):
    try:
        member = await bot.get_chat_member(chat_id=config.CHANNEL_ID, user_id=user_id)
        if member.status in ["member", "administrator", "creator"]:
            await bot.send_message(
                user_id,
                "🎉 Спасибо за подписку! Выберите подарок:",
                reply_markup=gifts_keyboard(),
            )
        else:
            await bot.send_message(
                user_id,
                "📢 Подпишитесь на канал, чтобы получить доступ к материалам!",
                reply_markup=welcome_keyboard(),
            )
    except Exception as e:
        await bot.send_message(config.ADMIN_ID, f"Ошибка проверки подписки: {e}")
