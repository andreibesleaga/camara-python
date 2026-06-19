# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DeviceLocationArea"]


class DeviceLocationArea(BaseModel):
    """The geofencing area where the monitor is active.

    This area is specified by API consumers in the subscription request. The same area definition is included in event notifications without any modifications.
    """

    area_type: Literal["CIRCLE"] = FieldInfo(alias="areaType")
    """Type of this area. CIRCLE - The area is defined as a circle."""
