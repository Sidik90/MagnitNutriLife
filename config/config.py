from pydantic_settings import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str
    CHANNEL_ID: int = -1002616457281  # ID вашего канала
    ADMIN_ID: int  # Ваш ID для ошибок
    CONSULTATION_LINK: str = "https://t.me/K_Marina_KMV"
    WEBSITE_LINK: str = "https://taplink.cc/marina_kv"

    class Config:
        env_file = ".env"


config = Config()
