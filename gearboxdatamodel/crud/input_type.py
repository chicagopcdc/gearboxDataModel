from .base import CRUDBase
from gearboxdatamodel.models import InputType
from gearboxdatamodel.schemas import InputTypeSearchResults, InputTypeCreate

class CRUDInputType(CRUDBase [InputType, InputTypeCreate, InputTypeSearchResults]):
    ...
input_type_crud = CRUDInputType(InputType)