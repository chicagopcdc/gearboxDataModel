from .base import CRUDBase
from gearboxdatamodel.models import StudyHasPatient
from gearboxdatamodel.schemas import StudyHasPatientCreate, StudyHasPatientSearchResults


class CRUDStudyHasPatient(
    CRUDBase[StudyHasPatient, StudyHasPatientCreate, StudyHasPatientSearchResults]
): ...


study_has_patient_crud = CRUDStudyHasPatient(StudyHasPatient)
