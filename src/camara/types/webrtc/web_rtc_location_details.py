# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .web_rtc_circle_coordinates import WebRtcCircleCoordinates
from .web_rtc_ellipsoid_coordinates import WebRtcEllipsoidCoordinates

__all__ = ["WebRtcLocationDetails", "Confidence", "Coordinates"]


class Confidence(BaseModel):
    """The confidence level of the location information."""

    pdf: Optional[Literal["normal", "uniform"]] = None
    """The probability density function (PDF) associated with the confidence value."""

    value: Optional[float] = None
    """The confidence value (percentage)."""


Coordinates: TypeAlias = Union[WebRtcCircleCoordinates, WebRtcEllipsoidCoordinates]


class WebRtcLocationDetails(BaseModel):
    """Details about the caller's location and related information.

    This object adheres to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for PIDF-LO compatibility.
    """

    confidence: Optional[Confidence] = None
    """The confidence level of the location information."""

    coordinates: Optional[Coordinates] = None
    """The coordinates of the caller's location, specific to the chosen shape."""

    method: Optional[Literal["GPS", "DBH", "DBH_HELO", "Other"]] = None
    """The method used to obtain the location information.

    - **GPS:** Global Positioning System (highly accurate)
    - **DBH:** Device-Based Hybrid
    - **DBH_HELO:** Device-Based Hybrid using Apple Hybridized Emergency Location
    - **Other:** Other methods (e.g., landmarks, IP Based etc.)
    """

    shape: Optional[Literal["Circle", "Ellipsoid"]] = None
    """The shape representing the caller's location (Circle or Ellipsoid)."""

    timestamp: Optional[datetime] = None
    """
    The timestamp (in ISO 8601 format) indicating when the location information was
    Calculated. \nThis is crucial for emergency services to assess the timeliness of
    the data. if not provided current timestamp will be used by default"
    """
