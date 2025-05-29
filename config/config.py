import os
import toml
from pathlib import Path
from dotenv import load_dotenv


class Config:
    def __init__(self):
        # Загружаем .env файл
        load_dotenv()

        # Загружаем toml конфиг
        self.config_path = Path(__file__).parent / "settings.toml"
        self._config = self._load_config()

        # Проверяем обязательные переменные
        if not os.getenv("BOT_TOKEN"):
            raise ValueError("BOT_TOKEN не установлен в .env файле")
        if not os.getenv("ADMIN_ID"):
            raise ValueError("ADMIN_ID не установлен в .env файле")

    def _load_config(self):
        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                return toml.load(f)
        except FileNotFoundError:
            raise Exception("Конфигурационный файл не найден")
        except toml.TomlDecodeError:
            raise Exception("Ошибка в формате конфигурационного файла")

    @property
    def bot_token(self):
        return os.getenv("BOT_TOKEN")

    @property
    def admin_id(self):
        return int(os.getenv("ADMIN_ID"))

    @property
    def bot_username(self):
        return self._config["bot"]["username"]

    @property
    def channel_id(self):
        return self._config["channel"]["id"]

    @property
    def channel_username(self):
        return self._config["channel"]["username"]

    @property
    def channel_name(self):
        return self._config["channel"]["name"]

    @property
    def channel_invite_link(self):
        return self._config["channel"]["invite_link"]

    @property
    def welcome_message(self):
        return self._config["messages"]["welcome"]

    @property
    def lead_magnet(self):
        return self._config["messages"]["lead_magnet"]

    @property
    def consultation_message(self):
        return self._config["messages"]["consultation"]

    @property
    def consultation_delay(self):
        return self._config["timing"]["consultation_delay"]


# Создаем экземпляр конфигурации
config = Config()
