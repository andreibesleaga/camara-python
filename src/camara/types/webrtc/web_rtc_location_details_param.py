# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .web_rtc_circle_coordinates_param import WebRtcCircleCoordinatesParam
from .web_rtc_ellipsoid_coordinates_param import WebRtcEllipsoidCoordinatesParam

__all__ = ["WebRtcLocationDetailsParam", "Confidence", "Coordinates"]


class Confidence(TypedDict, total=False):
    """The confidence level of the location information."""

    pdf: Literal["normal", "uniform"]
    """The probability density function (PDF) associated with the confidence value."""

    value: float
    """The confidence value (percentage)."""


Coordinates: TypeAlias = Union[WebRtcCircleCoordinatesParam, WebRtcEllipsoidCoordinatesParam]


class WebRtcLocationDetailsParam(TypedDict, total=False):
    """Details about the caller's location and related information.

    This object adheres to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for PIDF-LO compatibility.
    """

    confidence: Confidence
    """The confidence level of the location information."""

    coordinates: Coordinates
    """The coordinates of the caller's location, specific to the chosen shape."""

    method: Literal["GPS", "DBH", "DBH_HELO", "Other"]
    """The method used to obtain the location information.

    - **GPS:** Global Positioning System (highly accurate)
    - **DBH:** Device-Based Hybrid
    - **DBH_HELO:** Device-Based Hybrid using Apple Hybridized Emergency Location
    - **Other:** Other methods (e.g., landmarks, IP Based etc.)
    """

    shape: Literal["Circle", "Ellipsoid"]
    """The shape representing the caller's location (Circle or Ellipsoid)."""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The timestamp (in ISO 8601 format) indicating when the location information was
    Calculated. \nThis is crucial for emergency services to assess the timeliness of
    the data. if not provided current timestamp will be used by default"
    """
