from pydantic import BaseModel, HttpUrl, AfterValidator, ValidationError
from decimal import Decimal
from datetime import datetime
from typing import Annotated, TypeAlias

def check_presigned_url_validity(url: HttpUrl) -> HttpUrl:
    if "X-Amz-Signature" not in url.query:
        raise ValueError("Matching files URL is missing signature")
    return url

PresignedUrl: TypeAlias = Annotated[HttpUrl, AfterValidator(check_presigned_url_validity)]

class MatchingFilesUrls(BaseModel):
    mc_url: PresignedUrl
    mf_url: PresignedUrl
    ec_url: PresignedUrl
