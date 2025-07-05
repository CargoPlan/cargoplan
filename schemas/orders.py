from pydantic import BaseModel

from schemas.cargoes import Cargo


class Order(BaseModel):
    cargoes: list[Cargo]
    destination_port: str
