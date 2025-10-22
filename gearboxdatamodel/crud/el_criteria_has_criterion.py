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

    async def get_ec_ids(self, current_session: Session, ec_id: int) -> List[int]:
        return self.get(
            current_session,
            where=f"ElCriteriaHasCriterion.eligibility_criteria_id = {ec_id}",
            with_only_cols="ElCriteriaHasCriterion.id",
        )
        """
            stmt = select(ElCriteriaHasCriterion).where(ElCriteriaHasCriterion.eligibility_criteria_id == ec_id).load_only(ElCriteriaHasCriterion.id)
            try:
                result_db = await current_session.execute(stmt)
                result = result_db.unique().scalars().all()
                return result
            except exc.SQLAlchemyError as e:
                raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, f"SQL ERROR: {type(e)}: {e}")
            """


el_criteria_has_criterion_crud = CRUDElCriteriaHasCriterion(ElCriteriaHasCriterion)
