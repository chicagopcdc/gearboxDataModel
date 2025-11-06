from pydantic import BaseModel

from typing import Sequence, Optional


class PreAnnotatedCriterionModelBase(BaseModel):
    id: int
    pre_annotated_criterion_id: int
    model: Optional[str]

    class Config:
        from_attributes = True


class PreAnnotatedCriterionModel(PreAnnotatedCriterionModelBase):
    pass


class PreAnnotatedCriterionModelCreate(BaseModel):
    pre_annotated_criterion_id: int
    model: Optional[str]


class PreAnnotatedCriterionModelSearchResults(BaseModel):
    results: Sequence[PreAnnotatedCriterionModel]
