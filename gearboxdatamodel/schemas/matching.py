from pydantic import BaseModel
from typing import List, Union, Optional, Literal, Any
from fastapi import HTTPException


ComparisonOperator = Literal["eq", "gt", "gte", "lt", "lte", "ne", "in"]


# class StudyAlgorithmEngine(BaseModel):
#     id: int
#     algorithm_logic: MatchAlgorithm


class MatchFormValues(dict):
    def __init__(self, data):
        super().__init__()
        for key, value in data.items():
            try:
                int_key = int(key)
                self[int_key] = value
            except ValueError:
                raise HTTPException(status_code=400, detail=f"{key} must be a number")

    def __setitem__(self, key, value):
        try:
            key = int(key)
        except ValueError:
            raise ValueError(f"Key '{key}' must be a valid integer.")
        super().__setitem__(key, value)


class MatchInfo(BaseModel):
    fieldName: str
    fieldValue: Any
    fieldValueLabel: Optional[Union[str, List[str]]] = None
    isMatched: Optional[bool] = None
    operator: ComparisonOperator


class MatchInfoAlgorithm(BaseModel):
    operator: Literal["AND", "OR"]
    criteria: List[Union[MatchInfo, "MatchInfoAlgorithm"]]
    isMatched: Optional[bool] = None


class MatchDetails(dict):
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Key must be a int")
        if not isinstance(value, MatchInfoAlgorithm):
            raise TypeError("Value must be an instance of CustomObject")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise KeyError("Key must be a int")
        return super().__getitem__(key)
