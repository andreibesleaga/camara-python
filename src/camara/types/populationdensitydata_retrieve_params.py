# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PopulationdensitydataRetrieveParams", "Area", "SinkCredential"]


class PopulationdensitydataRetrieveParams(TypedDict, total=False):
    area: Required[Area]
    """Base schema for all areas"""

    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]]
    """End date time.

    It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ (i.e. which
    allows 2023-07-03T14:27:08.312+02:00 or 2023-07-03T12:27:08.312Z) The maximum
    endTime allowed is 3 months from the time of the request.
    """

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]
    """Start date time.

    It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ
    """

    precision: int
    """Precision required of response cells.

    Precision defines a geohash level and corresponds to the length of the geohash
    for each cell. More information at
    [Geohash system](https://en.wikipedia.org/wiki/Geohash)" If not included the
    default precision level 7 is used by default. In case of using a not supported
    level by the MNO, the API returns the error response
    `POPULATION_DENSITY_DATA.UNSUPPORTED_PRECISION`.
    """

    sink: str
    """
    The address where the API response will be asynchronously delivered, using the
    HTTP protocol.
    """

    sink_credential: Annotated[SinkCredential, PropertyInfo(alias="sinkCredential")]
    """
    A sink credential provides authentication or authorization information necessary
    to enable delivery of events to a target.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]


class Area(TypedDict, total=False):
    """Base schema for all areas"""

    area_type: Required[Annotated[Literal["POLYGON"], PropertyInfo(alias="areaType")]]
    """Type of this area. POLYGON - The area is defined as a polygon."""


class SinkCredential(TypedDict, total=False):
    """
    A sink credential provides authentication or authorization information necessary to enable delivery of events to a target.
    """

    credential_type: Required[
        Annotated[Literal["PLAIN", "ACCESSTOKEN", "REFRESHTOKEN"], PropertyInfo(alias="credentialType")]
    ]
    """
    The type of the credential. Note: Type of the credential - MUST be set to
    ACCESSTOKEN for now
    """
