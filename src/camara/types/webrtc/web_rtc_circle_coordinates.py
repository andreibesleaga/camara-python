# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WebRtcCircleCoordinates"]


class WebRtcCircleCoordinates(BaseModel):
    latitude: float
    """Latitude of the center point in decimal degrees (WGS84)."""

    longitude: float
    """Longitude of the center point in decimal degrees (WGS84)."""

    radius: float
    """Radius of the circle in meters, indicating the uncertainty."""
