from .base import CRUDBase
from gearboxdatamodel.models import Criterion, DisplayRules, Study, StudyVersion, ElCriteriaHasCriterion
from gearboxdatamodel.schemas import CriterionCreate, Criterion as CriterionSchema
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List


class CRUDCriterion(CRUDBase[Criterion, CriterionCreate, CriterionSchema]):

    async def get_criterion_id_by_code(self, db: Session, code: str) -> CriterionSchema:
        stmt = select(Criterion.id).where(Criterion.code == code)
        result = await db.execute(stmt)
        criterion_id = result.unique().scalars().first()
        return criterion_id

    async def get_criteria_not_exist_in_match_form(
        self, db: Session
    ) -> List[CriterionSchema]:
        subq = (
            select(DisplayRules.criterion_id).where(
                Criterion.id == DisplayRules.criterion_id
            )
        ).exists()
        stmt = select(Criterion).where(Criterion.active == True).where(~subq)
        result = await db.execute(stmt)
        criteria = result.unique().scalars().all()
        return criteria

    async def get_studies_for_criterion(
        self, db: Session, criterion_id: int
    ) -> List[Study]:
        """Get all studies that use this criterion in their eligibility criteria"""
        stmt = (
            select(Study)
            .distinct(Study.id)
            .join(StudyVersion, StudyVersion.study_id == Study.id)
            .join(ElCriteriaHasCriterion, StudyVersion.eligibility_criteria_id == ElCriteriaHasCriterion.eligibility_criteria_id)
            .where(ElCriteriaHasCriterion.criterion_id == criterion_id)
        )
        result = await db.execute(stmt)
        studies = result.unique().scalars().all()
        return studies


criterion_crud = CRUDCriterion(Criterion)
