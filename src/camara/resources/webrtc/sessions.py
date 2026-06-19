# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.webrtc import session_create_params, session_update_status_params
from ...types.webrtc.sdp_descriptor_param import SdpDescriptorParam
from ...types.webrtc.media_session_information import MediaSessionInformation
from ...types.webrtc.web_rtc_location_details_param import WebRtcLocationDetailsParam

__all__ = ["SessionsResource", "AsyncSessionsResource"]


class SessionsResource(SyncAPIResource):
    """WebRTC Call Handling"""

    @cached_property
    def with_raw_response(self) -> SessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return SessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return SessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        registration_id: str,
        answer: SdpDescriptorParam | Omit = omit,
        call_type: Literal["REGULAR", "EMERGENCY"] | Omit = omit,
        location_details: WebRtcLocationDetailsParam | Omit = omit,
        body_media_session_id: str | Omit = omit,
        offer: SdpDescriptorParam | Omit = omit,
        originator_address: str | Omit = omit,
        originator_name: str | Omit = omit,
        receiver_address: str | Omit = omit,
        receiver_name: str | Omit = omit,
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
        | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaSessionInformation:
        """
        Creates a voice and/or video session

        Args:
          answer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          call_type: Type of call. When set to EMERGENCY, the client MAY provide locationDetails. If
              omitted, treated as REGULAR.

          location_details: Details about the caller's location and related information. This object adheres
              to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for PIDF-LO compatibility.

          body_media_session_id: The media session ID created by the network. The mediaSessionId shall not be
              included in POST requests by the client, but must be included in the
              notifications from the network to the client device.

          offer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          originator_address: Subscriber address (Sender or Receiver)

          originator_name: Friendly name of the call originator

          receiver_address: Subscriber address (Sender or Receiver)

          receiver_name: Friendly name of the call terminator

          status: Provides the status of the media session. During the session creation, this
              attribute SHALL NOT be included in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "registrationId": registration_id,
                    "x-correlator": x_correlator,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/webrtc/sessions",
            body=maybe_transform(
                {
                    "answer": answer,
                    "call_type": call_type,
                    "location_details": location_details,
                    "body_media_session_id": body_media_session_id,
                    "offer": offer,
                    "originator_address": originator_address,
                    "originator_name": originator_name,
                    "receiver_address": receiver_address,
                    "receiver_name": receiver_name,
                    "status": status,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSessionInformation,
        )

    def retrieve(
        self,
        media_session_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaSessionInformation:
        """
        Get the media Session description based on `mediaSessionId`.

        ** The client shall construct the API path using the `mediaSessionId` supplied
        in the session creation response (origination) or in the invitation notification
        (termination). **

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_session_id:
            raise ValueError(f"Expected a non-empty value for `media_session_id` but received {media_session_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._get(
            path_template("/webrtc/sessions/{media_session_id}", media_session_id=media_session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSessionInformation,
        )

    def delete(
        self,
        media_session_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a 1-1 media session (as originator), Decline a 1-1 media session (as
        receiver), Terminate a 1-1 an ongoing media session ** The client shall
        construct the API path using the mediaSessionId supplied in the session creation
        response (origination) or in the invitation notification (termination). **'

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_session_id:
            raise ValueError(f"Expected a non-empty value for `media_session_id` but received {media_session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._delete(
            path_template("/webrtc/sessions/{media_session_id}", media_session_id=media_session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_status(
        self,
        media_session_id: str,
        *,
        answer: SdpDescriptorParam | Omit = omit,
        call_type: Literal["REGULAR", "EMERGENCY"] | Omit = omit,
        location_details: WebRtcLocationDetailsParam | Omit = omit,
        body_media_session_id: str | Omit = omit,
        offer: SdpDescriptorParam | Omit = omit,
        originator_address: str | Omit = omit,
        originator_name: str | Omit = omit,
        receiver_address: str | Omit = omit,
        receiver_name: str | Omit = omit,
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
        | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaSessionInformation:
        """
        Update the status of the media session, this may include updating SDP media

        The API consumer shall construct the API path using the `mediaSessionId`
        supplied in the session creation response (origination) or in the invitation
        notification (termination).

        Args:
          answer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          call_type: Type of call. When set to EMERGENCY, the client MAY provide locationDetails. If
              omitted, treated as REGULAR.

          location_details: Details about the caller's location and related information. This object adheres
              to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for PIDF-LO compatibility.

          body_media_session_id: The media session ID created by the network. The mediaSessionId shall not be
              included in POST requests by the client, but must be included in the
              notifications from the network to the client device.

          offer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          originator_address: Subscriber address (Sender or Receiver)

          originator_name: Friendly name of the call originator

          receiver_address: Subscriber address (Sender or Receiver)

          receiver_name: Friendly name of the call terminator

          status: Provides the status of the media session. During the session creation, this
              attribute SHALL NOT be included in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_session_id:
            raise ValueError(f"Expected a non-empty value for `media_session_id` but received {media_session_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._put(
            path_template("/webrtc/sessions/{media_session_id}/status", media_session_id=media_session_id),
            body=maybe_transform(
                {
                    "answer": answer,
                    "call_type": call_type,
                    "location_details": location_details,
                    "body_media_session_id": body_media_session_id,
                    "offer": offer,
                    "originator_address": originator_address,
                    "originator_name": originator_name,
                    "receiver_address": receiver_address,
                    "receiver_name": receiver_name,
                    "status": status,
                },
                session_update_status_params.SessionUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSessionInformation,
        )


class AsyncSessionsResource(AsyncAPIResource):
    """WebRTC Call Handling"""

    @cached_property
    def with_raw_response(self) -> AsyncSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        registration_id: str,
        answer: SdpDescriptorParam | Omit = omit,
        call_type: Literal["REGULAR", "EMERGENCY"] | Omit = omit,
        location_details: WebRtcLocationDetailsParam | Omit = omit,
        body_media_session_id: str | Omit = omit,
        offer: SdpDescriptorParam | Omit = omit,
        originator_address: str | Omit = omit,
        originator_name: str | Omit = omit,
        receiver_address: str | Omit = omit,
        receiver_name: str | Omit = omit,
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
        | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaSessionInformation:
        """
        Creates a voice and/or video session

        Args:
          answer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          call_type: Type of call. When set to EMERGENCY, the client MAY provide locationDetails. If
              omitted, treated as REGULAR.

          location_details: Details about the caller's location and related information. This object adheres
              to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for PIDF-LO compatibility.

          body_media_session_id: The media session ID created by the network. The mediaSessionId shall not be
              included in POST requests by the client, but must be included in the
              notifications from the network to the client device.

          offer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          originator_address: Subscriber address (Sender or Receiver)

          originator_name: Friendly name of the call originator

          receiver_address: Subscriber address (Sender or Receiver)

          receiver_name: Friendly name of the call terminator

          status: Provides the status of the media session. During the session creation, this
              attribute SHALL NOT be included in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "registrationId": registration_id,
                    "x-correlator": x_correlator,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/webrtc/sessions",
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "call_type": call_type,
                    "location_details": location_details,
                    "body_media_session_id": body_media_session_id,
                    "offer": offer,
                    "originator_address": originator_address,
                    "originator_name": originator_name,
                    "receiver_address": receiver_address,
                    "receiver_name": receiver_name,
                    "status": status,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSessionInformation,
        )

    async def retrieve(
        self,
        media_session_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaSessionInformation:
        """
        Get the media Session description based on `mediaSessionId`.

        ** The client shall construct the API path using the `mediaSessionId` supplied
        in the session creation response (origination) or in the invitation notification
        (termination). **

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_session_id:
            raise ValueError(f"Expected a non-empty value for `media_session_id` but received {media_session_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._get(
            path_template("/webrtc/sessions/{media_session_id}", media_session_id=media_session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSessionInformation,
        )

    async def delete(
        self,
        media_session_id: str,
        *,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Cancel a 1-1 media session (as originator), Decline a 1-1 media session (as
        receiver), Terminate a 1-1 an ongoing media session ** The client shall
        construct the API path using the mediaSessionId supplied in the session creation
        response (origination) or in the invitation notification (termination). **'

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_session_id:
            raise ValueError(f"Expected a non-empty value for `media_session_id` but received {media_session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._delete(
            path_template("/webrtc/sessions/{media_session_id}", media_session_id=media_session_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_status(
        self,
        media_session_id: str,
        *,
        answer: SdpDescriptorParam | Omit = omit,
        call_type: Literal["REGULAR", "EMERGENCY"] | Omit = omit,
        location_details: WebRtcLocationDetailsParam | Omit = omit,
        body_media_session_id: str | Omit = omit,
        offer: SdpDescriptorParam | Omit = omit,
        originator_address: str | Omit = omit,
        originator_name: str | Omit = omit,
        receiver_address: str | Omit = omit,
        receiver_name: str | Omit = omit,
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
        | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaSessionInformation:
        """
        Update the status of the media session, this may include updating SDP media

        The API consumer shall construct the API path using the `mediaSessionId`
        supplied in the session creation response (origination) or in the invitation
        notification (termination).

        Args:
          answer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          call_type: Type of call. When set to EMERGENCY, the client MAY provide locationDetails. If
              omitted, treated as REGULAR.

          location_details: Details about the caller's location and related information. This object adheres
              to 3GPP TS 24.229, RFC 4119, RFC 5139, and RFC 5491 for PIDF-LO compatibility.

          body_media_session_id: The media session ID created by the network. The mediaSessionId shall not be
              included in POST requests by the client, but must be included in the
              notifications from the network to the client device.

          offer: **OFFER**: An inlined session description in SDP format [RFC4566].If XML syntax
              is used, the content of this element SHALL be embedded in a CDATA section.

              **ANSWER**: This type represents an answer in WebRTC Signaling. This element is
              not present in case there is no answer yet, or the session invitation has been
              declined by the Terminating Participant.This element MUST NOT be present in a
              request from the application to the server to create a session.

          originator_address: Subscriber address (Sender or Receiver)

          originator_name: Friendly name of the call originator

          receiver_address: Subscriber address (Sender or Receiver)

          receiver_name: Friendly name of the call terminator

          status: Provides the status of the media session. During the session creation, this
              attribute SHALL NOT be included in the request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not media_session_id:
            raise ValueError(f"Expected a non-empty value for `media_session_id` but received {media_session_id!r}")
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._put(
            path_template("/webrtc/sessions/{media_session_id}/status", media_session_id=media_session_id),
            body=await async_maybe_transform(
                {
                    "answer": answer,
                    "call_type": call_type,
                    "location_details": location_details,
                    "body_media_session_id": body_media_session_id,
                    "offer": offer,
                    "originator_address": originator_address,
                    "originator_name": originator_name,
                    "receiver_address": receiver_address,
                    "receiver_name": receiver_name,
                    "status": status,
                },
                session_update_status_params.SessionUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaSessionInformation,
        )


class SessionsResourceWithRawResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            sessions.delete,
        )
        self.update_status = to_raw_response_wrapper(
            sessions.update_status,
        )


class AsyncSessionsResourceWithRawResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_raw_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sessions.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            sessions.delete,
        )
        self.update_status = async_to_raw_response_wrapper(
            sessions.update_status,
        )


class SessionsResourceWithStreamingResponse:
    def __init__(self, sessions: SessionsResource) -> None:
        self._sessions = sessions

        self.create = to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            sessions.delete,
        )
        self.update_status = to_streamed_response_wrapper(
            sessions.update_status,
        )


class AsyncSessionsResourceWithStreamingResponse:
    def __init__(self, sessions: AsyncSessionsResource) -> None:
        self._sessions = sessions

        self.create = async_to_streamed_response_wrapper(
            sessions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sessions.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            sessions.delete,
        )
        self.update_status = async_to_streamed_response_wrapper(
            sessions.update_status,
        )
