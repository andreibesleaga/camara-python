# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .device_identifier_device_ipv4_addr_param import DeviceIdentifierDeviceIpv4AddrParam

__all__ = ["DeviceIdentifierDeviceParam"]


class DeviceIdentifierDeviceParam(TypedDict, total=False):
    """End-user equipment able to connect to a mobile network.

    Examples of devices include smartphones or IoT sensors/actuators.
    The developer can choose to provide the below specified device identifiers:
    * `ipv4Address`
    * `ipv6Address`
    * `phoneNumber`
    * `networkAccessIdentifier`
    NOTE 1: The MNO might support only a subset of these options. The API invoker can provide multiple identifiers to be compatible across different MNOs. In this case the identifiers MUST belong to the same device.
    NOTE 2: For the current Commonalities release, we are enforcing that the networkAccessIdentifier is only part of the schema for future-proofing, and CAMARA does not currently allow its use. After the CAMARA meta-release work is concluded and the relevant issues are resolved, its use will need to be explicitly documented in the guidelines.
    """

    ipv4_address: Annotated[DeviceIdentifierDeviceIpv4AddrParam, PropertyInfo(alias="ipv4Address")]
    """
    The device should be identified by either the public (observed) IP address and
    port as seen by the application server, or the private (local) and any public
    (observed) IP addresses in use by the device (this information can be obtained
    by various means, for example from some DNS servers).

    If the allocated and observed IP addresses are the same (i.e. NAT is not in use)
    then the same address should be specified for both publicAddress and
    privateAddress.

    If NAT64 is in use, the device should be identified by its publicAddress and
    publicPort, or separately by its allocated IPv6 address (field ipv6Address of
    the Device object)

    In all cases, publicAddress must be specified, along with at least one of either
    privateAddress or publicPort, dependent upon which is known. In general, mobile
    devices cannot be identified by their public IPv4 address alone.
    """

    ipv6_address: Annotated[str, PropertyInfo(alias="ipv6Address")]
    """
    The device should be identified by the observed IPv6 address, or by any single
    IPv6 address from within the subnet allocated to the device (e.g. adding ::0 to
    the /64 prefix).
    """

    network_access_identifier: Annotated[str, PropertyInfo(alias="networkAccessIdentifier")]
    """A public identifier addressing a subscription in a mobile network.

    In 3GPP terminology, it corresponds to the GPSI formatted with the External
    Identifier ({Local Identifier}@{Domain Identifier}). Unlike the telephone
    number, the network access identifier is not subjected to portability ruling in
    force, and is individually managed by each operator.
    """

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """A public identifier addressing a telephone subscription.

    In mobile networks it corresponds to the MSISDN (Mobile Station International
    Subscriber Directory Number). In order to be globally unique it has to be
    formatted in international format, according to E.164 standard, prefixed with
    '+'.
    """
