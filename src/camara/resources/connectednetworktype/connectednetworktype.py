# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["ConnectednetworktypeResource", "AsyncConnectednetworktypeResource"]


class ConnectednetworktypeResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Connected Network Type Subscriptions"""
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectednetworktypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return ConnectednetworktypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectednetworktypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return ConnectednetworktypeResourceWithStreamingResponse(self)


class AsyncConnectednetworktypeResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Connected Network Type Subscriptions"""
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectednetworktypeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectednetworktypeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectednetworktypeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncConnectednetworktypeResourceWithStreamingResponse(self)


class ConnectednetworktypeResourceWithRawResponse:
    def __init__(self, connectednetworktype: ConnectednetworktypeResource) -> None:
        self._connectednetworktype = connectednetworktype

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Connected Network Type Subscriptions"""
        return SubscriptionsResourceWithRawResponse(self._connectednetworktype.subscriptions)


class AsyncConnectednetworktypeResourceWithRawResponse:
    def __init__(self, connectednetworktype: AsyncConnectednetworktypeResource) -> None:
        self._connectednetworktype = connectednetworktype

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Connected Network Type Subscriptions"""
        return AsyncSubscriptionsResourceWithRawResponse(self._connectednetworktype.subscriptions)


class ConnectednetworktypeResourceWithStreamingResponse:
    def __init__(self, connectednetworktype: ConnectednetworktypeResource) -> None:
        self._connectednetworktype = connectednetworktype

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Connected Network Type Subscriptions"""
        return SubscriptionsResourceWithStreamingResponse(self._connectednetworktype.subscriptions)


class AsyncConnectednetworktypeResourceWithStreamingResponse:
    def __init__(self, connectednetworktype: AsyncConnectednetworktypeResource) -> None:
        self._connectednetworktype = connectednetworktype

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Connected Network Type Subscriptions"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._connectednetworktype.subscriptions)
