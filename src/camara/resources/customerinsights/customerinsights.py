# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .scoring import (
    ScoringResource,
    AsyncScoringResource,
    ScoringResourceWithRawResponse,
    AsyncScoringResourceWithRawResponse,
    ScoringResourceWithStreamingResponse,
    AsyncScoringResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CustomerinsightsResource", "AsyncCustomerinsightsResource"]


class CustomerinsightsResource(SyncAPIResource):
    @cached_property
    def scoring(self) -> ScoringResource:
        """Customer Insights"""
        return ScoringResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomerinsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return CustomerinsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomerinsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return CustomerinsightsResourceWithStreamingResponse(self)


class AsyncCustomerinsightsResource(AsyncAPIResource):
    @cached_property
    def scoring(self) -> AsyncScoringResource:
        """Customer Insights"""
        return AsyncScoringResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomerinsightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomerinsightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomerinsightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncCustomerinsightsResourceWithStreamingResponse(self)


class CustomerinsightsResourceWithRawResponse:
    def __init__(self, customerinsights: CustomerinsightsResource) -> None:
        self._customerinsights = customerinsights

    @cached_property
    def scoring(self) -> ScoringResourceWithRawResponse:
        """Customer Insights"""
        return ScoringResourceWithRawResponse(self._customerinsights.scoring)


class AsyncCustomerinsightsResourceWithRawResponse:
    def __init__(self, customerinsights: AsyncCustomerinsightsResource) -> None:
        self._customerinsights = customerinsights

    @cached_property
    def scoring(self) -> AsyncScoringResourceWithRawResponse:
        """Customer Insights"""
        return AsyncScoringResourceWithRawResponse(self._customerinsights.scoring)


class CustomerinsightsResourceWithStreamingResponse:
    def __init__(self, customerinsights: CustomerinsightsResource) -> None:
        self._customerinsights = customerinsights

    @cached_property
    def scoring(self) -> ScoringResourceWithStreamingResponse:
        """Customer Insights"""
        return ScoringResourceWithStreamingResponse(self._customerinsights.scoring)


class AsyncCustomerinsightsResourceWithStreamingResponse:
    def __init__(self, customerinsights: AsyncCustomerinsightsResource) -> None:
        self._customerinsights = customerinsights

    @cached_property
    def scoring(self) -> AsyncScoringResourceWithStreamingResponse:
        """Customer Insights"""
        return AsyncScoringResourceWithStreamingResponse(self._customerinsights.scoring)
