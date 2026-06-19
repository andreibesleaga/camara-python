# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SimSwapConfig", "SubscriptionDetail"]


class SubscriptionDetail(BaseModel):
    """The detail of the requested event subscription"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """


class SimSwapConfig(BaseModel):
    """
    Implementation-specific configuration parameters needed by the subscription manager for acquiring events.
    In CAMARA we have predefined attributes like `subscriptionExpireTime` or `subscriptionMaxEvents` to limit subscription lifetime.
    Event type attributes must be defined in `subscriptionDetail`
    """

    subscription_detail: SubscriptionDetail = FieldInfo(alias="subscriptionDetail")
    """The detail of the requested event subscription"""

    subscription_expire_time: Optional[datetime] = FieldInfo(alias="subscriptionExpireTime", default=None)
    """
    The subscription expiration time (in date-time format) requested by the API
    consumer. It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    subscription_max_events: Optional[int] = FieldInfo(alias="subscriptionMaxEvents", default=None)
    """
    Identifies the maximum number of event reports to be generated (>=1) requested
    by the API consumer - Once this number is reached, the subscription ends.
    """
