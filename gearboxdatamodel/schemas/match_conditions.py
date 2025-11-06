from pydantic import BaseModel
from typing import List, Union, Literal


class MatchAlgorithm(BaseModel):
    operator: Literal["AND", "OR"]
    criteria: List[Union[int, "MatchAlgorithm"]]


class MatchCondition(BaseModel):
    studyId: int
    algorithm: MatchAlgorithm
