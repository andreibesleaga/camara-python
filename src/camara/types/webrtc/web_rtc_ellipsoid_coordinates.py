# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebRtcEllipsoidCoordinates"]


class WebRtcEllipsoidCoordinates(BaseModel):
    latitude: float
    """Latitude in the WGS 84 geocentric coordinate system."""

    longitude: float
    """Longitude in the WGS 84 geocentric coordinate system."""

    orientation: float
    """Orientation of the ellipsoid in degrees."""

    semi_major_axis: float = FieldInfo(alias="semiMajorAxis")
    """Length of the semi-major axis of the ellipsoid in meters."""

    semi_minor_axis: float = FieldInfo(alias="semiMinorAxis")
    """Length of the semi-minor axis of the ellipsoid in meters."""

    vertical_axis: float = FieldInfo(alias="verticalAxis")
    """Length of the vertical axis of the ellipsoid in meters."""

    z_axis: float = FieldInfo(alias="zAxis")
    """Altitude (optional) in the WGS 84 geocentric coordinate system."""
