from pydantic import BaseModel

from typing import Sequence


class SourceBase(BaseModel):
    source: str
    priority: int

    class Config:
        from_attributes = True


class Source(SourceBase):
    id: int


class SourceCreate(SourceBase):
    pass


class SourceSearchResults(BaseModel):
    results: Sequence[Source]
