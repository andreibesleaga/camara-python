# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TenureVerifyParams"]


class TenureVerifyParams(TypedDict, total=False):
    tenure_date: Required[Annotated[Union[str, date], PropertyInfo(alias="tenureDate", format="iso8601")]]
    """
    The date, in RFC 3339 / ISO 8601 compliant format "YYYY-MM-DD", from which
    continuous tenure of the identified network subscriber is required to be
    confirmed
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
