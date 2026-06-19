# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DeviceIdentifierDeviceIpv4AddrParam"]


class DeviceIdentifierDeviceIpv4AddrParam(TypedDict, total=False):
    """
    The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers).

    If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then  the same address should be specified for both publicAddress and privateAddress.

    If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object)

    In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone.
    """

    private_address: Annotated[str, PropertyInfo(alias="privateAddress")]
    """A single IPv4 address with no subnet mask"""

    public_address: Annotated[str, PropertyInfo(alias="publicAddress")]
    """A single IPv4 address with no subnet mask"""

    public_port: Annotated[int, PropertyInfo(alias="publicPort")]
    """TCP or UDP port number"""
