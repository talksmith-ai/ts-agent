from pydantic import BaseModel
from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

from typing import ClassVar


class ApplicationSettings(BaseModel):
    name: str = Field(
        default="Agent Application",
        description="Name of the application"
    )

    version: str = Field(
        default="0.1.0",
        description="Version of the application"
    )

    deployment_environment: str = Field(
        default="development",
        description="Deployment environment of the application"
    )


class ServerSettings(BaseModel):
    host: str = Field(
        default="http://localhost:8000",
        description="Host URL for the agent server"
    )

    root_path: str = Field(
        default="/agent",
        description="Root path for the agent server"
    )


class Settings(BaseSettings):
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        env_parse_none_str="None",
        env_parse_enums=True,
        env_ignore_empty=True,
    )

    app: ApplicationSettings = ApplicationSettings()
    server: ServerSettings = ServerSettings()

settings = Settings()

__all__ = ["settings"]
