# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .device_identifier_device import DeviceIdentifierDevice

__all__ = ["DeviceidentifierRetrieveIdentifierResponse", "Device"]


class Device(DeviceIdentifierDevice):
    """
    The device subscription identifier that was used to identify the device whose identifier is being returned. If this property is not present, then the device subscription identifier specified in the request was used.
    """

    pass


class DeviceidentifierRetrieveIdentifierResponse(BaseModel):
    device: Optional[Device] = None
    """
    The device subscription identifier that was used to identify the device whose
    identifier is being returned. If this property is not present, then the device
    subscription identifier specified in the request was used.
    """

    imei: Optional[str] = None
    """IMEI of the device"""

    imeisv: Optional[str] = None
    """IMEISV of the device"""

    last_checked: Optional[datetime] = FieldInfo(alias="lastChecked", default=None)
    """
    Date and time that the information was last confirmed by the mobile operator to
    be correct. It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    manufacturer: Optional[str] = None
    """Manufacturer of the device"""

    model: Optional[str] = None
    """Model of the device"""

    tac: Optional[str] = None
    """IMEI TAC of the device"""
