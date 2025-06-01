from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery
from ..keyboards.builders import gifts_keyboard
from ..services.subscription import check_subscription

router = Router()


@router.callback_query(F.data == "check_subscription")
async def on_check_subscription(callback: CallbackQuery, bot: Bot):
    await check_subscription(bot, callback.from_user.id)


@router.callback_query(F.data.startswith("gift_"))
async def on_gift_selected(callback: CallbackQuery):
    gift_id = callback.data.split("_")[1]
    gifts = {
        "1": (
            "🩺🔬Здоровье под Микроскопом: Погружение в Анализы",
            "https://disk.yandex.ru/i/I6wcu4XH8QWEvA",
        ),
        "2": (
            "🌊✨Легкость без Отека: Простые Шаги к Свободе",
            "https://disk.yandex.ru/i/GO-xgwqozYvz0Q",
        ),
        "3": (
            "⚡🍽️Ключ к Энергии: Управление Инсулином",
            "https://disk.yandex.ru/i/dwgGXFr-Bd1ZFQ",
        ),
    }
    title, url = gifts[gift_id]
    await callback.message.answer(
        f"🎁 Ваш подарок: <b>{title}</b>\n\n"
        f"Скачать: {url}\n\n"
        "Хотите получить персональные рекомендации, запишитесь на бесплатную консультацию?",
        reply_markup=gifts_keyboard(),
    )
