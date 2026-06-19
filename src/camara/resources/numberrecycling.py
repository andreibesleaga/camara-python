# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import numberrecycling_check_subscriber_change_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.numberrecycling_check_subscriber_change_response import NumberrecyclingCheckSubscriberChangeResponse

__all__ = ["NumberrecyclingResource", "AsyncNumberrecyclingResource"]


class NumberrecyclingResource(SyncAPIResource):
    """Number Recycling"""

    @cached_property
    def with_raw_response(self) -> NumberrecyclingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return NumberrecyclingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberrecyclingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return NumberrecyclingResourceWithStreamingResponse(self)

    def check_subscriber_change(
        self,
        *,
        specified_date: Union[str, date],
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberrecyclingCheckSubscriberChangeResponse:
        """
        Check whether the subscriber of the phone number has changed.

        Args:
          specified_date: Specified date to check whether there has been a change in the subscriber
              associated with the specific phone number, in RFC 3339 calendar date format
              (YYYY-MM-DD).

          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/numberrecycling/check",
            body=maybe_transform(
                {
                    "specified_date": specified_date,
                    "phone_number": phone_number,
                },
                numberrecycling_check_subscriber_change_params.NumberrecyclingCheckSubscriberChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberrecyclingCheckSubscriberChangeResponse,
        )


class AsyncNumberrecyclingResource(AsyncAPIResource):
    """Number Recycling"""

    @cached_property
    def with_raw_response(self) -> AsyncNumberrecyclingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberrecyclingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberrecyclingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncNumberrecyclingResourceWithStreamingResponse(self)

    async def check_subscriber_change(
        self,
        *,
        specified_date: Union[str, date],
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberrecyclingCheckSubscriberChangeResponse:
        """
        Check whether the subscriber of the phone number has changed.

        Args:
          specified_date: Specified date to check whether there has been a change in the subscriber
              associated with the specific phone number, in RFC 3339 calendar date format
              (YYYY-MM-DD).

          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/numberrecycling/check",
            body=await async_maybe_transform(
                {
                    "specified_date": specified_date,
                    "phone_number": phone_number,
                },
                numberrecycling_check_subscriber_change_params.NumberrecyclingCheckSubscriberChangeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NumberrecyclingCheckSubscriberChangeResponse,
        )


class NumberrecyclingResourceWithRawResponse:
    def __init__(self, numberrecycling: NumberrecyclingResource) -> None:
        self._numberrecycling = numberrecycling

        self.check_subscriber_change = to_raw_response_wrapper(
            numberrecycling.check_subscriber_change,
        )


class AsyncNumberrecyclingResourceWithRawResponse:
    def __init__(self, numberrecycling: AsyncNumberrecyclingResource) -> None:
        self._numberrecycling = numberrecycling

        self.check_subscriber_change = async_to_raw_response_wrapper(
            numberrecycling.check_subscriber_change,
        )


class NumberrecyclingResourceWithStreamingResponse:
    def __init__(self, numberrecycling: NumberrecyclingResource) -> None:
        self._numberrecycling = numberrecycling

        self.check_subscriber_change = to_streamed_response_wrapper(
            numberrecycling.check_subscriber_change,
        )


class AsyncNumberrecyclingResourceWithStreamingResponse:
    def __init__(self, numberrecycling: AsyncNumberrecyclingResource) -> None:
        self._numberrecycling = numberrecycling

        self.check_subscriber_change = async_to_streamed_response_wrapper(
            numberrecycling.check_subscriber_change,
        )
