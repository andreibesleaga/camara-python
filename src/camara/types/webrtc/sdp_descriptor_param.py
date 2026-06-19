# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SdpDescriptorParam"]


class SdpDescriptorParam(TypedDict, total=False):
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

    sdp: str
    """
    An inlined session description in SDP format [RFC4566].If XML syntax is used,
    the content of this element SHALL be embedded in a CDATA section
    """
