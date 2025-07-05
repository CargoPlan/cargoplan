from typing import Any, Coroutine, Sequence

from sqlalchemy import select

from models import Ship, RoomStructureRecord
from services._basic import Service


class ShipService(Service):
    async def create_ship(self, name: str, max_weight: float) -> Ship:
        ship = Ship(name=name, max_weight=max_weight)

        self.session.add(ship)
        await self.session.commit()
        await self.session.refresh(ship)

        return ship

    async def get_ship(self, ship_id: int) -> Ship | None:
        return await self.session.get(Ship, ship_id)

    async def get_room_structure(self, ship_id: int) -> Sequence[RoomStructureRecord]:
        query = select(RoomStructureRecord).where(RoomStructureRecord.ship_id == ship_id)
        return (await self.session.scalars(query)).all()
