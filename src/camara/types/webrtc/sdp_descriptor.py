# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SdpDescriptor"]


class SdpDescriptor(BaseModel):
    """
    **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
    is used, the content of this element SHALL be embedded in a CDATA
    section.

    **ANSWER**: This type represents an answer in WebRTC Signaling. This element is not
    present in case there is no answer yet, or the session invitation has
    been declined by the Terminating Participant.This element MUST NOT be
    present in a request from the application to the server to create a
    session.
    """

    sdp: Optional[str] = None
    """
    An inlined session description in SDP format [RFC4566].If XML syntax is used,
    the content of this element SHALL be embedded in a CDATA section
    """
