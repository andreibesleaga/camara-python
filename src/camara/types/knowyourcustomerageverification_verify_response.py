# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["KnowyourcustomerageverificationVerifyResponse"]


class KnowyourcustomerageverificationVerifyResponse(BaseModel):
    """Response to an age verification request"""

    age_check: Literal["true", "false", "not_available"] = FieldInfo(alias="ageCheck")
    """
    Indicate `"true"` when the age of the user is the same age or older than the age
    threshold (age >= age threshold), and `"false"` if not (age < age threshold). If
    the API Provider doesn't have enough information to perform the validation, a
    `not_available` can be returned.
    """

    content_lock: Optional[Literal["true", "false", "not_available"]] = FieldInfo(alias="contentLock", default=None)
    """
    Indicate `"true"` if the subscription associated with the phone number has any
    kind of content lock (i.e certain web content blocked) and `"false"` if not. If
    the information is not available the value `not_available` can be returned.
    """

    identity_match_score: Optional[int] = FieldInfo(alias="identityMatchScore", default=None)
    """
    The overall score of identity information available in the API Provider,
    information either provided in the request body comparing it to the one that the
    API Provider holds or directly using internal API Provider's information. It is
    optional for the API Provider to return the Identity match score.
    """

    parental_control: Optional[Literal["true", "false", "not_available"]] = FieldInfo(
        alias="parentalControl", default=None
    )
    """
    Indicate `"true"` if the subscription associated with the phone number has any
    kind of parental control activated and `"false"` if not. If the information is
    not available the value `not_available` can be returned.
    """

    verified_status: Optional[bool] = FieldInfo(alias="verifiedStatus", default=None)
    """
    Indicate `true` if the information provided has been compared against
    information based on an identification document legally accepted as an age
    verification document (Note), otherwise indicate `false`. Note: Depending on the
    country, credit-check or other mechanism can be used instead of official
    identification for Age Verification. For details, please contact API Provider.
    """
