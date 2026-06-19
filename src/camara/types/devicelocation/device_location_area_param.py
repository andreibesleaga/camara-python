# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DeviceLocationAreaParam"]


class DeviceLocationAreaParam(TypedDict, total=False):
    """The geofencing area where the monitor is active.

    This area is specified by API consumers in the subscription request. The same area definition is included in event notifications without any modifications.
    """

    area_type: Required[Annotated[Literal["CIRCLE"], PropertyInfo(alias="areaType")]]
    """Type of this area. CIRCLE - The area is defined as a circle."""
