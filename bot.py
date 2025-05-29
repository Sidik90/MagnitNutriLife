import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

from config.config import config
from utils.logger import logger
from handlers import commands, subscription, consultation


async def main():
    # Инициализация бота с новым синтаксисом
    bot = Bot(
        token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Регистрация обработчиков
    dp.include_router(commands.router)
    dp.include_router(subscription.router)
    dp.include_router(consultation.router)

    # Уведомление админу о запуске
    try:
        await bot.send_message(config.admin_id, "🤖 Бот успешно запущен!")
    except Exception as e:
        logger.error(f"Не удалось отправить уведомление админу: {e}")

    # Запуск бота
    try:
        logger.info("Запуск бота...")
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f"Ошибка в работе бота: {e}", exc_info=True)
    finally:
        logger.info("Остановка бота...")
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
