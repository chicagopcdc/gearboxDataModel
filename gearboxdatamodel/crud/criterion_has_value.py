from .base import CRUDBase
from gearboxdatamodel.models import CriterionHasValue
from gearboxdatamodel.schemas import (
    CriterionHasValueCreate,
    CriterionHasValueSearchResults,
)


class CRUDCriterionHasValue(
    CRUDBase[CriterionHasValue, CriterionHasValueCreate, CriterionHasValueSearchResults]
): ...


criterion_has_value_crud = CRUDCriterionHasValue(CriterionHasValue)
