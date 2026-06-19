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

__all__ = ["SimswapResource", "AsyncSimswapResource"]


class SimswapResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Sim Swap Subscriptions"""
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SimswapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return SimswapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimswapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return SimswapResourceWithStreamingResponse(self)


class AsyncSimswapResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Sim Swap Subscriptions"""
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSimswapResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimswapResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimswapResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncSimswapResourceWithStreamingResponse(self)


class SimswapResourceWithRawResponse:
    def __init__(self, simswap: SimswapResource) -> None:
        self._simswap = simswap

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Sim Swap Subscriptions"""
        return SubscriptionsResourceWithRawResponse(self._simswap.subscriptions)


class AsyncSimswapResourceWithRawResponse:
    def __init__(self, simswap: AsyncSimswapResource) -> None:
        self._simswap = simswap

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Sim Swap Subscriptions"""
        return AsyncSubscriptionsResourceWithRawResponse(self._simswap.subscriptions)


class SimswapResourceWithStreamingResponse:
    def __init__(self, simswap: SimswapResource) -> None:
        self._simswap = simswap

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Sim Swap Subscriptions"""
        return SubscriptionsResourceWithStreamingResponse(self._simswap.subscriptions)


class AsyncSimswapResourceWithStreamingResponse:
    def __init__(self, simswap: AsyncSimswapResource) -> None:
        self._simswap = simswap

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Sim Swap Subscriptions"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._simswap.subscriptions)
