from datetime import datetime, timezone
from typing import Optional

from pydantic import field_serializer, field_validator
from sqlmodel import Field, SQLModel


def _validate_titulo(value: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise ValueError("titulo cannot be empty")
    return stripped


class TaskBase(SQLModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False


class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    criada_em: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False,
    )


class TaskCreate(SQLModel):
    titulo: str
    descricao: Optional[str] = None
    concluida: bool = False

    @field_validator("titulo")
    @classmethod
    def validate_titulo(cls, value: str) -> str:
        return _validate_titulo(value)


class TaskUpdate(SQLModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    concluida: Optional[bool] = None

    @field_validator("titulo")
    @classmethod
    def validate_titulo(cls, value: Optional[str]) -> Optional[str]:
        if value is None:
            return value
        return _validate_titulo(value)


class TaskRead(SQLModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    concluida: bool
    criada_em: datetime

    @field_serializer("criada_em")
    def serialize_criada_em(self, value: datetime) -> str:
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
