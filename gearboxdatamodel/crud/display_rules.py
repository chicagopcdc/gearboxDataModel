from .base import CRUDBase
from gearboxdatamodel.models import DisplayRules
from gearboxdatamodel.schemas import (
    DisplayRulesCreate,
    DisplayRules as DisplayRulesSchema,
)


class CRUDDisplayRules(
    CRUDBase[DisplayRules, DisplayRulesCreate, DisplayRulesSchema]
): ...


display_rules_crud = CRUDDisplayRules(DisplayRules)
