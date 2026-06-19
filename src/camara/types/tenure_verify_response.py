# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TenureVerifyResponse"]


class TenureVerifyResponse(BaseModel):
    tenure_date_check: bool = FieldInfo(alias="tenureDateCheck")
    """
    `true` when the identified mobile subscription has had valid tenure since
    `tenureDate`, otherwise `false`
    """

    contract_type: Optional[Literal["PAYG", "PAYM", "Business"]] = FieldInfo(alias="contractType", default=None)
    """If exists, populated with:

    - `PAYG` - prepaid (pay-as-you-go) account
    - `PAYM` - contract account
    - `Business` - Business (enterprise) account

    This attribute may be omitted from the response set if the information is not
    available
    """
