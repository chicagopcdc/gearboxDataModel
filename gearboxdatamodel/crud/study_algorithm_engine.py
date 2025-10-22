from .base import CRUDBase
from gearboxdatamodel.models import StudyAlgorithmEngine
from gearboxdatamodel.schemas import (
    StudyAlgorithmEngineCreate,
    StudyAlgorithmEngineSearchResults,
)


class CRUDStudyAlgorithmEngine(
    CRUDBase[
        StudyAlgorithmEngine,
        StudyAlgorithmEngineCreate,
        StudyAlgorithmEngineSearchResults,
    ]
): ...


study_algorithm_engine_crud = CRUDStudyAlgorithmEngine(StudyAlgorithmEngine)
