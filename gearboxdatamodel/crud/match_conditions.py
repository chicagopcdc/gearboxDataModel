from sqlalchemy import select
from typing import List

from sqlalchemy.orm import Session
from gearboxdatamodel.models import StudyVersion

from cdislogging import get_logger

logger = get_logger(__name__)


async def get_study_versions(session: Session) -> List[StudyVersion]:

    stmt = select(StudyVersion).where(StudyVersion.active == True)
    result = await session.execute(stmt)
    ae = result.unique().scalars().all()

    return ae
