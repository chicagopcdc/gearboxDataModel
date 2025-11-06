from pydantic import BaseModel
from typing import Optional, Sequence


class OntologyCodeBase(BaseModel):
    ontology_url: Optional[str]
    name: Optional[str]
    code: Optional[str]
    value: Optional[str]
    version: Optional[bool]

    class Config:
        from_attributes = True


class OntologyCode(OntologyCodeBase):
    id: int


class OntologyCodeCreate(OntologyCodeBase):
    pass


class OntologyCodeUpdate(BaseModel):
    pass


class OntologyCodeSearchResults(BaseModel):
    results: Sequence[OntologyCode]
