# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SimSwapConfigParam", "SubscriptionDetail"]


class SubscriptionDetail(TypedDict, total=False):
    """The detail of the requested event subscription"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """


class SimSwapConfigParam(TypedDict, total=False):
    """
    Implementation-specific configuration parameters needed by the subscription manager for acquiring events.
    In CAMARA we have predefined attributes like `subscriptionExpireTime` or `subscriptionMaxEvents` to limit subscription lifetime.
    Event type attributes must be defined in `subscriptionDetail`
    """

    subscription_detail: Required[Annotated[SubscriptionDetail, PropertyInfo(alias="subscriptionDetail")]]
    """The detail of the requested event subscription"""

    subscription_expire_time: Annotated[
        Union[str, datetime], PropertyInfo(alias="subscriptionExpireTime", format="iso8601")
    ]
    """
    The subscription expiration time (in date-time format) requested by the API
    consumer. It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    subscription_max_events: Annotated[int, PropertyInfo(alias="subscriptionMaxEvents")]
    """
    Identifies the maximum number of event reports to be generated (>=1) requested
    by the API consumer - Once this number is reached, the subscription ends.
    """
