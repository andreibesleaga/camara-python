# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OtpvalidationSendCodeParams"]


class OtpvalidationSendCodeParams(TypedDict, total=False):
    message: Required[str]
    """Message template used to compose the content of the SMS sent to the phone
    number.

    It must include the following label indicating where to include the short code
    `{{code}}`
    """

    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
