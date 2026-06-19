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

__all__ = ["ConnectivityinsightsResource", "AsyncConnectivityinsightsResource"]


class ConnectivityinsightsResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Connectivity Insights Subscriptions"""
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConnectivityinsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return ConnectivityinsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConnectivityinsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return ConnectivityinsightsResourceWithStreamingResponse(self)


class AsyncConnectivityinsightsResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Connectivity Insights Subscriptions"""
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConnectivityinsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConnectivityinsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConnectivityinsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncConnectivityinsightsResourceWithStreamingResponse(self)


class ConnectivityinsightsResourceWithRawResponse:
    def __init__(self, connectivityinsights: ConnectivityinsightsResource) -> None:
        self._connectivityinsights = connectivityinsights

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Connectivity Insights Subscriptions"""
        return SubscriptionsResourceWithRawResponse(self._connectivityinsights.subscriptions)


class AsyncConnectivityinsightsResourceWithRawResponse:
    def __init__(self, connectivityinsights: AsyncConnectivityinsightsResource) -> None:
        self._connectivityinsights = connectivityinsights

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Connectivity Insights Subscriptions"""
        return AsyncSubscriptionsResourceWithRawResponse(self._connectivityinsights.subscriptions)


class ConnectivityinsightsResourceWithStreamingResponse:
    def __init__(self, connectivityinsights: ConnectivityinsightsResource) -> None:
        self._connectivityinsights = connectivityinsights

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Connectivity Insights Subscriptions"""
        return SubscriptionsResourceWithStreamingResponse(self._connectivityinsights.subscriptions)


class AsyncConnectivityinsightsResourceWithStreamingResponse:
    def __init__(self, connectivityinsights: AsyncConnectivityinsightsResource) -> None:
        self._connectivityinsights = connectivityinsights

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Connectivity Insights Subscriptions"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._connectivityinsights.subscriptions)
