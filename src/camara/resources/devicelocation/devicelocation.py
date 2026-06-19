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

__all__ = ["DevicelocationResource", "AsyncDevicelocationResource"]


class DevicelocationResource(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        """Device Geofencing Subscriptions"""
        return SubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevicelocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return DevicelocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicelocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return DevicelocationResourceWithStreamingResponse(self)


class AsyncDevicelocationResource(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        """Device Geofencing Subscriptions"""
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevicelocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevicelocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicelocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncDevicelocationResourceWithStreamingResponse(self)


class DevicelocationResourceWithRawResponse:
    def __init__(self, devicelocation: DevicelocationResource) -> None:
        self._devicelocation = devicelocation

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        """Device Geofencing Subscriptions"""
        return SubscriptionsResourceWithRawResponse(self._devicelocation.subscriptions)


class AsyncDevicelocationResourceWithRawResponse:
    def __init__(self, devicelocation: AsyncDevicelocationResource) -> None:
        self._devicelocation = devicelocation

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """Device Geofencing Subscriptions"""
        return AsyncSubscriptionsResourceWithRawResponse(self._devicelocation.subscriptions)


class DevicelocationResourceWithStreamingResponse:
    def __init__(self, devicelocation: DevicelocationResource) -> None:
        self._devicelocation = devicelocation

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        """Device Geofencing Subscriptions"""
        return SubscriptionsResourceWithStreamingResponse(self._devicelocation.subscriptions)


class AsyncDevicelocationResourceWithStreamingResponse:
    def __init__(self, devicelocation: AsyncDevicelocationResource) -> None:
        self._devicelocation = devicelocation

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """Device Geofencing Subscriptions"""
        return AsyncSubscriptionsResourceWithStreamingResponse(self._devicelocation.subscriptions)
