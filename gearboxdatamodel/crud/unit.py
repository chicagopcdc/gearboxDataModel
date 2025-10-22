from .base import CRUDBase
from gearboxdatamodel.models import Unit
from gearboxdatamodel.schemas import UnitCreate, UnitSearchResults
from sqlalchemy.orm import Session
from sqlalchemy import select


class CRUDUnit(CRUDBase[Unit, UnitCreate, UnitSearchResults]):

    async def get_unit(self, current_session: Session, unit_name: str):
        stmt = select(Unit).where(Unit.name == unit_name)
        result = await current_session.execute(stmt)
        unit = result.unique().scalars().first()
        return unit


unit_crud = CRUDUnit(Unit)
