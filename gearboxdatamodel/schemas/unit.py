from pydantic import BaseModel
from typing import Sequence


class UnitBase(BaseModel):
    name: str

    class Config:
        from_attributes = True


class Unit(UnitBase):
    id: int


class UnitCreate(UnitBase):
    pass


class UnitSearchResults(BaseModel):
    results: Sequence[Unit]
