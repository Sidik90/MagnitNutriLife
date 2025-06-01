import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))


import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from handlers import start, callbacks
from config.config import config


async def main():
    # Новый способ задания параметров бота
    bot = Bot(
        token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()

    # Регистрация обработчиков
    dp.include_router(start.router)
    dp.include_router(callbacks.router)

    await bot.delete_webhook()
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
