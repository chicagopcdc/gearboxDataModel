from .base import CRUDBase
from gearboxdatamodel.models import CriterionHasTag
from gearboxdatamodel.schemas import CriterionHasTagCreate, CriterionHasTagSearchResults


class CRUDCriterionHasTag(
    CRUDBase[CriterionHasTag, CriterionHasTagCreate, CriterionHasTagSearchResults]
): ...


criterion_has_tag_crud = CRUDCriterionHasTag(CriterionHasTag)
