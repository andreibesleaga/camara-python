# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .device_identifier_device_param import DeviceIdentifierDeviceParam

__all__ = ["DeviceidentifierRetrieveTypeParams"]


class DeviceidentifierRetrieveTypeParams(TypedDict, total=False):
    device: DeviceIdentifierDeviceParam
    """End-user equipment able to connect to a mobile network.

    Examples of devices include smartphones or IoT sensors/actuators. The developer
    can choose to provide the below specified device identifiers:

    - `ipv4Address`
    - `ipv6Address`
    - `phoneNumber`
    - `networkAccessIdentifier` NOTE 1: The MNO might support only a subset of these
      options. The API invoker can provide multiple identifiers to be compatible
      across different MNOs. In this case the identifiers MUST belong to the same
      device. NOTE 2: For the current Commonalities release, we are enforcing that
      the networkAccessIdentifier is only part of the schema for future-proofing,
      and CAMARA does not currently allow its use. After the CAMARA meta-release
      work is concluded and the relevant issues are resolved, its use will need to
      be explicitly documented in the guidelines.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
