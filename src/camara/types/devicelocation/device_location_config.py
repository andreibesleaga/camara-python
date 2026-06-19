# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeviceLocationConfig"]


class DeviceLocationConfig(BaseModel):
    """
    Implementation-specific configuration parameters are needed by the subscription manager for acquiring events.
    In CAMARA we have predefined attributes like `subscriptionExpireTime`, `subscriptionMaxEvents`, `initialEvent`.
    """

    initial_event: Optional[bool] = FieldInfo(alias="initialEvent", default=None)
    """
    Set to `true` by API consumer if consumer wants to get an event as soon as the
    subscription is created and current situation reflects event request. Example:
    Consumer request area entered event. If consumer sets initialEvent to true and
    device is already in the geofence, an event is triggered.
    """

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
    by the API consumer - Once this number is reached, the subscription ends. Note
    on combined usage of `initialEvent` and `subscriptionMaxEvents`: If an event is
    triggered following `initialEvent` set to `true`, this event will be counted
    towards `subscriptionMaxEvents`.
    """
