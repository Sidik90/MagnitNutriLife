import logging
import sys
from pathlib import Path

# Настройка логгера
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger("telegram_bot")


def setup_logging():
    """Дополнительная настройка логирования при необходимости"""
    pass
