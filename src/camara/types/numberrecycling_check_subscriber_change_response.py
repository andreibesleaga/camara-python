# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NumberrecyclingCheckSubscriberChangeResponse"]


class NumberrecyclingCheckSubscriberChangeResponse(BaseModel):
    phone_number_recycled: bool = FieldInfo(alias="phoneNumberRecycled")
    """
    Set to true (Boolean, not string) when there has been a change in the subscriber
    associated with the specific phone number after “specifiedDate”.
    """
