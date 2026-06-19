# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DeviceIdentifierDeviceIpv4Addr"]


class DeviceIdentifierDeviceIpv4Addr(BaseModel):
    """
    The device should be identified by either the public (observed) IP address and port as seen by the application server, or the private (local) and any public (observed) IP addresses in use by the device (this information can be obtained by various means, for example from some DNS servers).

    If the allocated and observed IP addresses are the same (i.e. NAT is not in use) then  the same address should be specified for both publicAddress and privateAddress.

    If NAT64 is in use, the device should be identified by its publicAddress and publicPort, or separately by its allocated IPv6 address (field ipv6Address of the Device object)

    In all cases, publicAddress must be specified, along with at least one of either privateAddress or publicPort, dependent upon which is known. In general, mobile devices cannot be identified by their public IPv4 address alone.
    """

    private_address: Optional[str] = FieldInfo(alias="privateAddress", default=None)
    """A single IPv4 address with no subnet mask"""

    public_address: Optional[str] = FieldInfo(alias="publicAddress", default=None)
    """A single IPv4 address with no subnet mask"""

    public_port: Optional[int] = FieldInfo(alias="publicPort", default=None)
    """TCP or UDP port number"""
