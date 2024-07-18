from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

from pathlib import Path

from .settings import BASE_DIR


class ConstantFromEnv(BaseSettings):
    model_config = SettingsConfigDict(env_file=Path(BASE_DIR / '.env'))

    owm_api_key: str = Field(alias='OPENWEATHERMAP_API_KEY')

