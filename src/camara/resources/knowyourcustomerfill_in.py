# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import knowyourcustomerfill_in_create_params
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
from ..types.knowyourcustomerfill_in_create_response import KnowyourcustomerfillInCreateResponse

__all__ = ["KnowyourcustomerfillInResource", "AsyncKnowyourcustomerfillInResource"]


class KnowyourcustomerfillInResource(SyncAPIResource):
    """Know Your Customer Fill-in"""

    @cached_property
    def with_raw_response(self) -> KnowyourcustomerfillInResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return KnowyourcustomerfillInResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowyourcustomerfillInResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return KnowyourcustomerfillInResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowyourcustomerfillInCreateResponse:
        """
        Providing information related to a customer identity stored the account data
        bound to the customer's phone number.

        Args:
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
            "/knowyourcustomerfill-in/fill-in",
            body=maybe_transform(
                {"phone_number": phone_number}, knowyourcustomerfill_in_create_params.KnowyourcustomerfillInCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowyourcustomerfillInCreateResponse,
        )


class AsyncKnowyourcustomerfillInResource(AsyncAPIResource):
    """Know Your Customer Fill-in"""

    @cached_property
    def with_raw_response(self) -> AsyncKnowyourcustomerfillInResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowyourcustomerfillInResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowyourcustomerfillInResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncKnowyourcustomerfillInResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_number: str | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KnowyourcustomerfillInCreateResponse:
        """
        Providing information related to a customer identity stored the account data
        bound to the customer's phone number.

        Args:
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
            "/knowyourcustomerfill-in/fill-in",
            body=await async_maybe_transform(
                {"phone_number": phone_number}, knowyourcustomerfill_in_create_params.KnowyourcustomerfillInCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowyourcustomerfillInCreateResponse,
        )


class KnowyourcustomerfillInResourceWithRawResponse:
    def __init__(self, knowyourcustomerfill_in: KnowyourcustomerfillInResource) -> None:
        self._knowyourcustomerfill_in = knowyourcustomerfill_in

        self.create = to_raw_response_wrapper(
            knowyourcustomerfill_in.create,
        )


class AsyncKnowyourcustomerfillInResourceWithRawResponse:
    def __init__(self, knowyourcustomerfill_in: AsyncKnowyourcustomerfillInResource) -> None:
        self._knowyourcustomerfill_in = knowyourcustomerfill_in

        self.create = async_to_raw_response_wrapper(
            knowyourcustomerfill_in.create,
        )


class KnowyourcustomerfillInResourceWithStreamingResponse:
    def __init__(self, knowyourcustomerfill_in: KnowyourcustomerfillInResource) -> None:
        self._knowyourcustomerfill_in = knowyourcustomerfill_in

        self.create = to_streamed_response_wrapper(
            knowyourcustomerfill_in.create,
        )


class AsyncKnowyourcustomerfillInResourceWithStreamingResponse:
    def __init__(self, knowyourcustomerfill_in: AsyncKnowyourcustomerfillInResource) -> None:
        self._knowyourcustomerfill_in = knowyourcustomerfill_in

        self.create = async_to_streamed_response_wrapper(
            knowyourcustomerfill_in.create,
        )
