from sqlalchemy.orm import Mapped

from database_connector import Base


class Cargo(Base):
    name: Mapped[str | None]
    description: Mapped[str | None]
