# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .sdp_descriptor import SdpDescriptor
from .web_rtc_location_details import WebRtcLocationDetails

__all__ = ["MediaSessionInformation"]


class MediaSessionInformation(BaseModel):
    answer: Optional[SdpDescriptor] = None
    """
    **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
    is used, the content of this element SHALL be embedded in a CDATA section.

    **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
    not present in case there is no answer yet, or the session invitation has been
    declined by the Terminating Participant.This element MUST NOT be present in a
    request from the application to the server to create a session.
    """

    call_type: Optional[Literal["REGULAR", "EMERGENCY"]] = FieldInfo(alias="callType", default=None)
    """Type of call.

    When set to EMERGENCY, the client MAY provide locationDetails. If omitted,
    treated as REGULAR.
    """

    location_details: Optional[WebRtcLocationDetails] = FieldInfo(alias="locationDetails", default=None)
    """Details about the caller's location and related information.

    This object adheres to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for
    PIDF-LO compatibility.
    """

    media_session_id: Optional[str] = FieldInfo(alias="mediaSessionId", default=None)
    """The media session ID created by the network.

    The mediaSessionId shall not be included in POST requests by the client, but
    must be included in the notifications from the network to the client device.
    """

    offer: Optional[SdpDescriptor] = None
    """
    **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
    is used, the content of this element SHALL be embedded in a CDATA section.

    **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
    not present in case there is no answer yet, or the session invitation has been
    declined by the Terminating Participant.This element MUST NOT be present in a
    request from the application to the server to create a session.
    """

    originator_address: Optional[str] = FieldInfo(alias="originatorAddress", default=None)
    """Subscriber address (Sender or Receiver)"""

    originator_name: Optional[str] = FieldInfo(alias="originatorName", default=None)
    """Friendly name of the call originator"""

    receiver_address: Optional[str] = FieldInfo(alias="receiverAddress", default=None)
    """Subscriber address (Sender or Receiver)"""

    receiver_name: Optional[str] = FieldInfo(alias="receiverName", default=None)
    """Friendly name of the call terminator"""

    status: Optional[
        Literal[
            "Initial",
            "InProgress",
            "Ringing",
            "Proceeding",
            "Connected",
            "Terminated",
            "Hold",
            "Resume",
            "SessionCancelled",
            "Declined",
            "Failed",
            "Waiting",
            "NoAnswer",
            "NotReachable",
            "Busy",
        ]
    ] = None
    """Provides the status of the media session.

    During the session creation, this attribute SHALL NOT be included in the
    request.
    """
