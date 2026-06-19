# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OtpvalidationValidateCodeParams"]


class OtpvalidationValidateCodeParams(TypedDict, total=False):
    authentication_id: Required[Annotated[str, PropertyInfo(alias="authenticationId")]]
    """unique id of the verification attempt the code belongs to."""

    code: Required[str]
    """temporal, short code to be validated"""

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
