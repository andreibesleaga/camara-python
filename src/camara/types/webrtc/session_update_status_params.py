# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from .sdp_descriptor_param import SdpDescriptorParam
from .web_rtc_location_details_param import WebRtcLocationDetailsParam

__all__ = ["SessionUpdateStatusParams"]


class SessionUpdateStatusParams(TypedDict, total=False):
    answer: SdpDescriptorParam
    """
    **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
    is used, the content of this element SHALL be embedded in a CDATA section.

    **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
    not present in case there is no answer yet, or the session invitation has been
    declined by the Terminating Participant.This element MUST NOT be present in a
    request from the application to the server to create a session.
    """

    call_type: Annotated[Literal["REGULAR", "EMERGENCY"], PropertyInfo(alias="callType")]
    """Type of call.

    When set to EMERGENCY, the client MAY provide locationDetails. If omitted,
    treated as REGULAR.
    """

    location_details: Annotated[WebRtcLocationDetailsParam, PropertyInfo(alias="locationDetails")]
    """Details about the caller's location and related information.

    This object adheres to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for
    PIDF-LO compatibility.
    """

    body_media_session_id: Annotated[str, PropertyInfo(alias="mediaSessionId")]
    """The media session ID created by the network.

    The mediaSessionId shall not be included in POST requests by the client, but
    must be included in the notifications from the network to the client device.
    """

    offer: SdpDescriptorParam
    """
    **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
    is used, the content of this element SHALL be embedded in a CDATA section.

    **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
    not present in case there is no answer yet, or the session invitation has been
    declined by the Terminating Participant.This element MUST NOT be present in a
    request from the application to the server to create a session.
    """

    originator_address: Annotated[str, PropertyInfo(alias="originatorAddress")]
    """Subscriber address (Sender or Receiver)"""

    originator_name: Annotated[str, PropertyInfo(alias="originatorName")]
    """Friendly name of the call originator"""

    receiver_address: Annotated[str, PropertyInfo(alias="receiverAddress")]
    """Subscriber address (Sender or Receiver)"""

    receiver_name: Annotated[str, PropertyInfo(alias="receiverName")]
    """Friendly name of the call terminator"""

    status: Literal[
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
    """Provides the status of the media session.

    During the session creation, this attribute SHALL NOT be included in the
    request.
    """

    x_correlator: Annotated[str, PropertyInfo(alias="x-correlator")]
