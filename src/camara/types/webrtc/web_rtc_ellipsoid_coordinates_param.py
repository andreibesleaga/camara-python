# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebRtcEllipsoidCoordinatesParam"]


class WebRtcEllipsoidCoordinatesParam(TypedDict, total=False):
    latitude: Required[float]
    """Latitude in the WGS 84 geocentric coordinate system."""

    longitude: Required[float]
    """Longitude in the WGS 84 geocentric coordinate system."""

    orientation: Required[float]
    """Orientation of the ellipsoid in degrees."""

    semi_major_axis: Required[Annotated[float, PropertyInfo(alias="semiMajorAxis")]]
    """Length of the semi-major axis of the ellipsoid in meters."""

    semi_minor_axis: Required[Annotated[float, PropertyInfo(alias="semiMinorAxis")]]
    """Length of the semi-minor axis of the ellipsoid in meters."""

    vertical_axis: Required[Annotated[float, PropertyInfo(alias="verticalAxis")]]
    """Length of the vertical axis of the ellipsoid in meters."""

    z_axis: Required[Annotated[float, PropertyInfo(alias="zAxis")]]
    """Altitude (optional) in the WGS 84 geocentric coordinate system."""
