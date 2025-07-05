import enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from database_connector import Base


class RoomType(enum.Enum):
    deck = "палуба"
    tweendeck = "твиндек"
    hold = "трюм"


class Room(Base):
    __tablename__ = "rooms"

    type: Mapped[RoomType]
    name: Mapped[str | None]

    layer_count: Mapped[int | None]
    line_count: Mapped[int | None]
    place_count: Mapped[int | None]

    max_weight_at_place: Mapped[float | None]

    ship_id: Mapped[int] = mapped_column(ForeignKey("ships.id"))
    ship: Mapped["Ship"] = relationship(back_populates="rooms")


class Ship(Base):
    __tablename__ = "ships"

    name: Mapped[str]
    max_weight: Mapped[float | None]

    rooms: Mapped[set["Room"]] = relationship(back_populates="ship")


class RoomStructureRecord(Base):
    __tablename__ = "room_structures"

    ship_id: Mapped[int] = mapped_column(ForeignKey("ships.id"))
    over_room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    under_room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))

    ship: Mapped["Ship"] = relationship()
    over_room: Mapped["Room"] = relationship()
    under_room: Mapped["Room"] = relationship()
