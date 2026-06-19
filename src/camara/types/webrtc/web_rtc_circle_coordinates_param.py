# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebRtcCircleCoordinatesParam"]


class WebRtcCircleCoordinatesParam(TypedDict, total=False):
    latitude: Required[float]
    """Latitude of the center point in decimal degrees (WGS84)."""

    longitude: Required[float]
    """Longitude of the center point in decimal degrees (WGS84)."""

    radius: Required[float]
    """Radius of the circle in meters, indicating the uncertainty."""
