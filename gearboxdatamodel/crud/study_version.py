from .base import CRUDBase
from gearboxdatamodel.models import StudyVersion
from gearboxdatamodel.schemas import (
    StudyVersionCreate,
    StudyVersion as StudyVersionSchema,
)
from sqlalchemy.orm import Session
from sqlalchemy import func, select, exc, or_
from gearboxdatamodel.util.types import StudyVersionStatus
from fastapi import HTTPException
from gearboxdatamodel.util import status


class CRUDStudyVersion(CRUDBase[StudyVersion, StudyVersionSchema, StudyVersionCreate]):

    async def get_study_versions_for_adjudication(self, current_session: Session):

        stmt = (
            select(StudyVersion)
            .where(
                (
                    or_(
                        StudyVersion.status == StudyVersionStatus.IN_PROCESS,
                        StudyVersion.status == StudyVersionStatus.NEW,
                    )
                )
            )
            .where(
                (
                        StudyVersion.study.active == True 
                )
            )
            .order_by(StudyVersion.id)
        )

        result = await current_session.execute(stmt)
        study_versions = result.unique().scalars().all()
        return study_versions

    async def get_study_version_ec_id(
        self, current_session: Session, eligibility_criteria_id: int
    ):

        stmt = select(StudyVersion).where(
            StudyVersion.eligibility_criteria_id == eligibility_criteria_id
        )

        result = await current_session.execute(stmt)
        study_version = result.unique().scalars().first()
        return study_version

    async def get_latest_study_version(
        self, current_session: Session, study_id: int
    ) -> StudyVersionSchema:

        study_version = None
        try:
            max_ver_subq = select(func.max(StudyVersion.study_version_num)).where(
                StudyVersion.study_id == study_id
            )
            stmt = (
                select(StudyVersion)
                .where(StudyVersion.study_id == study_id)
                .where(StudyVersion.study_version_num == max_ver_subq)
            )
            result = await current_session.execute(stmt)
            study_version = result.unique().scalars().first()
        except exc.SQLAlchemyError as e:
            raise HTTPException(
                status.HTTP_500_INTERNAL_SERVER_ERROR, f"SQL ERROR: {type(e)}: {e}"
            )

        return study_version


study_version_crud = CRUDStudyVersion(StudyVersion)
