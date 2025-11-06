from pydantic import BaseModel
from typing import Sequence, Any


class StudyHasPatientBase(BaseModel):
    study_id: int
    patient_id: str
    data: Any
    source_id: str

    class Config:
        from_attributes = True


class StudyHasPatient(StudyHasPatientBase):
    pass


class StudyHasPatientCreate(BaseModel):
    shps: Sequence[StudyHasPatientBase]


class StudyHasPatientSearchResults(StudyHasPatientBase):
    results: Sequence[StudyHasPatient]
