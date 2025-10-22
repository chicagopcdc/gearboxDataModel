from sqlalchemy import select, exc
from sqlalchemy.orm import Session, joinedload
from gearboxdatamodel.models import ElCriteriaHasCriterion, Criterion

from fastapi import HTTPException
from gearboxdatamodel.util import status

from .base import CRUDBase
from gearboxdatamodel.models import EligibilityCriteria
from gearboxdatamodel.schemas import (
    EligibilityCriteriaSearchResults,
    EligibilityCriteriaCreate,
)


class CRUDEligibilityCriteria(
    CRUDBase[
        EligibilityCriteria, EligibilityCriteriaCreate, EligibilityCriteriaSearchResults
    ]
):

    async def get_eligibility_criteria_set(
        self, current_session: Session, ec_id: int = None
    ):

        stmt = (
            select(ElCriteriaHasCriterion)
            .options(
                joinedload(ElCriteriaHasCriterion.criterion).options(
                    joinedload(Criterion.input_type)
                ),
                joinedload(ElCriteriaHasCriterion.value),
            )
            .order_by(ElCriteriaHasCriterion.id)
        )

        if ec_id:
            stmt = stmt.where(ElCriteriaHasCriterion.eligibility_criteria_id == ec_id)

        stmt = stmt.order_by(ElCriteriaHasCriterion.id)
        try:
            result = await current_session.execute(stmt)
            ec = result.unique().scalars().all()
            return ec
        except exc.SQLAlchemyError as e:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, f"SQL ERROR: {type(e)}: {e}"
            )


eligibility_criteria_crud = CRUDEligibilityCriteria(EligibilityCriteria)
