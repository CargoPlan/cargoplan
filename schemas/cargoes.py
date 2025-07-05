from typing import Literal

from pydantic import BaseModel

type CargoType = Literal["20ft", "40ft"]


class Cargo(BaseModel):
    id: int
    name: str | None
    description: str | None
    type: CargoType
    weight: float
