from enum import Enum
from typing import Tuple

from pydantic import BaseModel


class Model(str, Enum):
    tiny = "tiny"
    base = "base"
    small = "small"
    medium = "medium"
    large = "large"


class Settings(BaseModel):
    language: str | None = "pt"
    initial_prompt: str | None = None
    temperature: float | Tuple[float, ...] | None = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)


class Payload(BaseModel):
    url: str
    model: Model = Model.small
    settings: Settings | None = Settings()
