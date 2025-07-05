from pydantic import BaseModel


class CargoPlanRecord(BaseModel):
    room_id: int
    layer: int
    line: int
    place: int

    cargo_id: int


class CargoPlan(BaseModel):
    ship_id: int
    records: list[CargoPlanRecord]