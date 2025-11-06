from .base import CRUDBase
from gearboxdatamodel.models import Tag
from gearboxdatamodel.schemas import TagCreate, TagSearchResults


class CRUDTag(CRUDBase[Tag, TagCreate, TagSearchResults]): ...


tag_crud = CRUDTag(Tag)
