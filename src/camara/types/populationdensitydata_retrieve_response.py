# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PopulationdensitydataRetrieveResponse",
    "TimedPopulationDensityData",
    "TimedPopulationDensityDataCellPopulationDensityData",
]


class TimedPopulationDensityDataCellPopulationDensityData(BaseModel):
    """Population density data of a cell in a concrete time range.

    In case of insufficient data, to guarantee an anonymized prediction due to the k-anonymity within a specific cell and time range, no population density data is returned and the property `dataType` value is "LOW_DENSITY". In case of a cell not supported `dataType` value is "NO_DATA"
    """

    data_type: Literal["NO_DATA", "LOW_DENSITY", "DENSITY_ESTIMATION"] = FieldInfo(alias="dataType")

    geohash: str
    """
    Coordinates of the cell represented as a string using the
    [Geohash system](https://en.wikipedia.org/wiki/Geohash). Encoding a geographic
    location into a short string. The value length, and thus, the cell granularity,
    is determined by the request body property `precision`.
    """


class TimedPopulationDensityData(BaseModel):
    cell_population_density_data: List[TimedPopulationDensityDataCellPopulationDensityData] = FieldInfo(
        alias="cellPopulationDensityData"
    )
    """Population density data for the different cells in a concrete time range."""

    end_time: datetime = FieldInfo(alias="endTime")
    """Interval end time.

    It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ (i.e. which
    allows 2023-07-03T14:27:08.312+02:00 or 2023-07-03T12:27:08.312Z)
    """

    start_time: datetime = FieldInfo(alias="startTime")
    """Interval start time.

    It must follow
    [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
    have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ (i.e. which
    allows 2023-07-03T14:27:08.312+02:00 or 2023-07-03T12:27:08.312Z)
    """


class PopulationdensitydataRetrieveResponse(BaseModel):
    """
    Population density values is represented in time intervals for different cells of the requested area. Each element in `timedPopulationDensityData` array corresponds to a time interval, containing population density data for the grid cells. The intervals are 1 hour long.
    """

    status: Literal["SUPPORTED_AREA", "PART_OF_AREA_NOT_SUPPORTED", "AREA_NOT_SUPPORTED", "OPERATION_NOT_COMPLETED"]
    """
    Represents the state of the response for the input polygon defined in the
    request, the possible values are:

    - `SUPPORTED_AREA`: The whole request area is supported. Population density data
      for the entire requested area is returned.
    - `PART_OF_AREA_NOT_SUPPORTED`: Part of the requested area is outside the MNOs
      coverage area, the cells outside the coverage area will have property
      `dataType` with value `NO_DATA`.
    - `AREA_NOT_SUPPORTED`: The whole requested area is outside the MNOs coverage
      area. No data will be returned.
    - `OPERATION_NOT_COMPLETED`: An error happened during asynchronous processing of
      the request. This status will only be returned in case the asynchronous API
      behaviour is used.
    """

    timed_population_density_data: List[TimedPopulationDensityData] = FieldInfo(alias="timedPopulationDensityData")
    """
    Time ranges along with the population density data for the cells within it. The
    request startTime or the request endTime have to be fully covered by the
    intervals. For example, if the intervals are 1-hour long and the input date
    range were [2024-01-03T11:25:00Z to 2024-01-03T12:45:00Z] it would contain 2
    intervals (Interval from 2024-01-03T11:00:00Z to 2024-01-03T12:00:00Z and
    interval from 2024-01-03T12:00:00Z to 2024-01-03T13:00:00Z).
    """

    status_info: Optional[str] = FieldInfo(alias="statusInfo", default=None)
    """
    Information about the status, mandatory when property `status` is
    `OPERATION_NOT_COMPLETED` for adding extra information about the error.
    """
