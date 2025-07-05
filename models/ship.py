from sqlalchemy.orm import Mapped

from database_connector import Base


class Ship(Base):
    __tablename__ = "ships"

    name: Mapped[str]
