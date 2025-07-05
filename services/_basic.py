from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database_connector import get_session


class Service:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session: AsyncSession = session
