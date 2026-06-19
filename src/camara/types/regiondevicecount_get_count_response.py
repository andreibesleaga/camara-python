# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RegiondevicecountGetCountResponse"]


class RegiondevicecountGetCountResponse(BaseModel):
    """RegionDeviceCount result"""

    count: Optional[float] = None
    """Device Count"""

    status: Optional[
        Literal[
            "SUPPORTED_AREA",
            "PART_OF_AREA_NOT_SUPPORTED",
            "AREA_NOT_SUPPORTED",
            "DENSITY_BELOW_PRIVACY_THRESHOLD",
            "TIME_INTERVAL_NO_DATA_FOUND",
        ]
    ] = None
    """
    SUPPORTED_AREA: The whole requested area is supported Region Device Count for
    the entire requested area is returned - Telco Coverage = 100 %

    PART_OF_AREA_NOT_SUPPORTED: Part of the requested area is outside the MNOs
    coverage area, the area outside the coverage area are not returned - 100% >Telco
    Coverage >=50%

    AREA_NOT_SUPPORTED: The whole requested area is outside the MNO coverage area No
    data will be returned- Telco Coverage <50%

    DENSITY_BELOW_PRIVACY_THRESHOLD: The number of connected devices is below
    privacy threshold of local regulation

    TIME_INTERVAL_NO_DATA_FOUND: Unable to find device count data within the
    requested time interval
    """
