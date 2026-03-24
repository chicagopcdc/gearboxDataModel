from typing import List

from sqlalchemy.orm import Session
from .base import CRUDBase
from gearboxdatamodel.models import ElCriteriaHasCriterion
from gearboxdatamodel.schemas import (
    ElCriteriaHasCriterionSearchResults,
    ElCriteriaHasCriterionCreate,
)


class CRUDElCriteriaHasCriterion(
    CRUDBase[
        ElCriteriaHasCriterion,
        ElCriteriaHasCriterionCreate,
        ElCriteriaHasCriterionSearchResults,
    ]
):

    async def get_echc_by_ec_id(self, current_session: Session, ec_id: int) -> List[ElCriteriaHasCriterion]:
        return await self.get_multi(
            current_session,
            where=f"ElCriteriaHasCriterion.eligibility_criteria_id = {ec_id}",
        )

el_criteria_has_criterion_crud = CRUDElCriteriaHasCriterion(ElCriteriaHasCriterion)
