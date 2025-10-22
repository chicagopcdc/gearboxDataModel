from .base import CRUDBase
from gearboxdatamodel.models import OntologyCode
from ..schemas import OntologyCodeSearchResults, OntologyCodeCreate


class CRUDOntologyCode(
    CRUDBase[OntologyCode, OntologyCodeCreate, OntologyCodeSearchResults]
): ...


ontology_code_crud = CRUDOntologyCode(OntologyCode)
