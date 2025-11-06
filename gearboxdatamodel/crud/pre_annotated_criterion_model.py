from .base import CRUDBase
from gearboxdatamodel.models import PreAnnotatedCriterionModel
from gearboxdatamodel.schemas import (
    PreAnnotatedCriterionModelCreate,
    PreAnnotatedCriterionModelSearchResults,
)


class CRUDPreAnnotatedCriterionModel(
    CRUDBase[
        PreAnnotatedCriterionModel,
        PreAnnotatedCriterionModelCreate,
        PreAnnotatedCriterionModelSearchResults,
    ]
): ...


pre_annotated_criterion_model_crud = CRUDPreAnnotatedCriterionModel(
    PreAnnotatedCriterionModel
)
