from .base import CRUDBase
from gearboxdatamodel.models import TriggeredBy
from gearboxdatamodel.schemas import TriggeredByCreate, TriggeredBySearchResults


class CRUDTriggeredBy(
    CRUDBase[TriggeredBy, TriggeredByCreate, TriggeredBySearchResults]
): ...


triggered_by_crud = CRUDTriggeredBy(TriggeredBy)
