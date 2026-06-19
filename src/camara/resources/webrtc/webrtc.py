# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .sessions import (
    SessionsResource,
    AsyncSessionsResource,
    SessionsResourceWithRawResponse,
    AsyncSessionsResourceWithRawResponse,
    SessionsResourceWithStreamingResponse,
    AsyncSessionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["WebrtcResource", "AsyncWebrtcResource"]


class WebrtcResource(SyncAPIResource):
    @cached_property
    def sessions(self) -> SessionsResource:
        """WebRTC Call Handling"""
        return SessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebrtcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return WebrtcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebrtcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return WebrtcResourceWithStreamingResponse(self)


class AsyncWebrtcResource(AsyncAPIResource):
    @cached_property
    def sessions(self) -> AsyncSessionsResource:
        """WebRTC Call Handling"""
        return AsyncSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebrtcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWebrtcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebrtcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncWebrtcResourceWithStreamingResponse(self)


class WebrtcResourceWithRawResponse:
    def __init__(self, webrtc: WebrtcResource) -> None:
        self._webrtc = webrtc

    @cached_property
    def sessions(self) -> SessionsResourceWithRawResponse:
        """WebRTC Call Handling"""
        return SessionsResourceWithRawResponse(self._webrtc.sessions)


class AsyncWebrtcResourceWithRawResponse:
    def __init__(self, webrtc: AsyncWebrtcResource) -> None:
        self._webrtc = webrtc

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithRawResponse:
        """WebRTC Call Handling"""
        return AsyncSessionsResourceWithRawResponse(self._webrtc.sessions)


class WebrtcResourceWithStreamingResponse:
    def __init__(self, webrtc: WebrtcResource) -> None:
        self._webrtc = webrtc

    @cached_property
    def sessions(self) -> SessionsResourceWithStreamingResponse:
        """WebRTC Call Handling"""
        return SessionsResourceWithStreamingResponse(self._webrtc.sessions)


class AsyncWebrtcResourceWithStreamingResponse:
    def __init__(self, webrtc: AsyncWebrtcResource) -> None:
        self._webrtc = webrtc

    @cached_property
    def sessions(self) -> AsyncSessionsResourceWithStreamingResponse:
        """WebRTC Call Handling"""
        return AsyncSessionsResourceWithStreamingResponse(self._webrtc.sessions)
