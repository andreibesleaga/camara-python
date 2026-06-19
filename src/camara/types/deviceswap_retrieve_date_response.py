# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DeviceswapRetrieveDateResponse"]


class DeviceswapRetrieveDateResponse(BaseModel):
    latest_device_change: Optional[datetime] = FieldInfo(alias="latestDeviceChange", default=None)
    """Timestamp of latest device swap performed.

    It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    monitored_period: Optional[int] = FieldInfo(alias="monitoredPeriod", default=None)
    """Timeframe in days for device change supervision for the phone number.

    It could be valued in the response if the latest Device swap occurred before
    this monitored period.
    """
