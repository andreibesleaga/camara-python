# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["KnowyourcustomerageverificationVerifyParams"]


class KnowyourcustomerageverificationVerifyParams(TypedDict, total=False):
    age_threshold: Required[Annotated[int, PropertyInfo(alias="ageThreshold")]]
    """The age to be verified.

    The indicated range is a global definition of maximum and minimum values allowed
    to be requested. It is important to note that this range might be more
    restrictive in some implementations due to local regulations of a country i.e. A
    country does not allow to request for an age under 18. This limitation must be
    informed during the onboarding process.
    """

    birthdate: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    The birthdate of the customer, in RFC 3339 / ISO 8601 calendar date format
    (YYYY-MM-DD).
    """

    email: str
    """Email address of the customer in the RFC specified format (local-part@domain)."""

    family_name: Annotated[str, PropertyInfo(alias="familyName")]
    """Last name, family name, or surname of the customer."""

    family_name_at_birth: Annotated[str, PropertyInfo(alias="familyNameAtBirth")]
    """Last/family/sur- name at birth of the customer."""

    given_name: Annotated[str, PropertyInfo(alias="givenName")]
    """First/given name or compound first/given name of the customer."""

    id_document: Annotated[str, PropertyInfo(alias="idDocument")]
    """Id number associated to the official identity document in the country.

    It may contain alphanumeric characters.
    """

    include_content_lock: Annotated[bool, PropertyInfo(alias="includeContentLock")]
    """
    If this parameter is included in the request with value `true`, the response
    property `contentLock` will be returned. If it is not included or its value is
    `false`, the response property will not be returned.
    """

    include_parental_control: Annotated[bool, PropertyInfo(alias="includeParentalControl")]
    """
    If this parameter is included in the request with value `true`, the response
    property `parentalControl` will be returned. If it is not included or its value
    is `false`, the response property will not be returned.
    """

    middle_names: Annotated[str, PropertyInfo(alias="middleNames")]
    """Middle name/s of the customer."""

    name: str
    """
    Complete name of the customer, usually composed of first/given name and
    last/family/sur- name in a country. Depending on the country, the order of
    first/give name and last/family/sur- name varies, and middle name could be
    included. It can use givenName, middleNames, familyName and/or
    familyNameAtBirth. For example, in ESP, name+familyName; in NLD, it can be
    name+middleNames+familyName or name+middleNames+familyNameAtBirth, etc.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
