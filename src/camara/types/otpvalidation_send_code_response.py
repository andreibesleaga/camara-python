# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OtpvalidationSendCodeResponse"]


class OtpvalidationSendCodeResponse(BaseModel):
    """Structure to provide authentication identifier"""

    authentication_id: str = FieldInfo(alias="authenticationId")
    """unique id of the verification attempt the code belongs to."""
