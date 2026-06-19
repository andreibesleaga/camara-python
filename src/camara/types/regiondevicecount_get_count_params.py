# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RegiondevicecountGetCountParams", "Area", "Filter", "SinkCredential"]


class RegiondevicecountGetCountParams(TypedDict, total=False):
    area: Area

    endtime: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Ending timestamp for counting the number of devices in the area.

    It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    filter: Filter
    """This parameter is used to filter devices.

    Currently, two filtering criteria are defined, `roamingStatus` and `deviceType`,
    which can be expanded in the future. `IN` logic is used used for multiple
    filtering items within a single filtering criterion, `AND` logic is used between
    multiple filtering criteria.

    - If a filtering critera is not provided, it means that there is no need to
      filter this item.
    - At least one of the criteria must be provided,a filter without any criteria is
      not allowed.
    - If no filtering is required, this parameter does not need to be provided. For
      example
      ,`"filter":{"roamingStatus": ["roaming"],"deviceType": ["human device","IoT device"]}`
      means the API need to return the count of human network devices and IoT
      devices that are in roaming mode.`"filter":{"roamingStatus": ["non-roaming"]}`
      means that the API need to return the count of all devices that are not in
      roaming mode.
    """

    sink: str
    """
    The URL where the API response will be asynchronously delivered, using the HTTP
    protocol.
    """

    sink_credential: Annotated[SinkCredential, PropertyInfo(alias="sinkCredential")]
    """
    A sink credential provides authentication or authorization information necessary
    to enable delivery of events to a target.
    """

    starttime: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Starting timestamp for counting the number of devices in the area.

    It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]


class Area(TypedDict, total=False):
    area_type: Required[Annotated[Literal["CIRCLE", "POLYGON"], PropertyInfo(alias="areaType")]]
    """
    Type of this area. CIRCLE - The area is defined as a circle. POLYGON - The area
    is defined as a polygon.
    """


class Filter(TypedDict, total=False):
    """This parameter is used to filter devices.

    Currently, two filtering criteria are defined, `roamingStatus` and `deviceType`, which can be expanded in the future. `IN` logic is used used for multiple filtering items within a single filtering criterion, `AND` logic is used between multiple filtering criteria.
    - If a filtering critera is not provided, it means that there is no need to filter this item.
    - At least one of the criteria must be provided,a filter without any criteria is not allowed.
    - If no filtering is required, this parameter does not need to be provided.
    For example ,`"filter":{"roamingStatus": ["roaming"],"deviceType": ["human device","IoT device"]}` means the API need to return the count of human network devices and IoT devices that are in roaming mode.`"filter":{"roamingStatus": ["non-roaming"]}` means that the API need to return the count of all devices that are not in roaming mode.
    """

    device_type: Annotated[List[Literal["human device", "IoT device", "other"]], PropertyInfo(alias="deviceType")]
    """
    Filtering by device type, 'human device' represents the need to filter for human
    network devices, 'IoT device' represents the need to filter for IoT devices, and
    'other' represents the need to filter for other types of devices.
    """

    roaming_status: Annotated[List[Literal["roaming", "non-roaming"]], PropertyInfo(alias="roamingStatus")]
    """
    Filter whether the device is in roaming mode,'roaming' represents the need to
    filter devices that are in roaming mode,'non-roaming' represents the need to
    filter devices that are not roaming.
    """


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
