from typing import Literal

from pydantic import BaseModel

type RoomType = Literal["палуба", "твиндек", "трюм"]


class Room(BaseModel):
    id: int
    type: RoomType

    layer_count: int
    line_count: int
    place_count: int

    max_weight_at_place: float


class Ship(BaseModel):
    id: int
    name: str
    rooms: list[Room]

    max_weight: float
