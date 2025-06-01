from aiogram.utils.keyboard import InlineKeyboardBuilder
from config.config import config


def welcome_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔔 Подписаться", url=f"https://t.me/NutriLaive")
    builder.button(text="✅ Я подписан", callback_data="check_subscription")
    builder.adjust(1, 1)
    return builder.as_markup()


def gifts_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="🩺🔬Здоровье под Микроскопом: Погружение в Анализы",
        callback_data="gift_1",
    )
    builder.button(
        text="🌊✨Легкость без Отека: Простые Шаги к Свободе", callback_data="gift_2"
    )
    builder.button(
        text="⚡🍽️Ключ к Энергии: Управление Инсулином", callback_data="gift_3"
    )
    builder.button(text="💬 Хочу бесплатную консультацию", url=config.CONSULTATION_LINK)
    builder.button(text="🌐 Наш сайт", url=config.WEBSITE_LINK)
    builder.adjust(1, 1, 1, 1, 1)  # Группировка кнопок
    return builder.as_markup()
