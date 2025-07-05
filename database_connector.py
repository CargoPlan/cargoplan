from typing import Annotated
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, sessionmaker, declared_attr, declarative_base, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession, AsyncAttrs, create_async_engine

from config import settings

DeclarativeBase = declarative_base()

int_pk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int_pk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id!r})'


def load_models():
    from models import Ship, Room, RoomStructureRecord


engine = create_async_engine(settings.DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

load_models()


async def init_models():
    async with engine.begin() as session:
        await session.run_sync(Base.metadata.drop_all)
        await session.run_sync(Base.metadata.create_all)


async def get_session():
    async with async_session() as session:
        yield session
