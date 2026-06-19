# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.customerinsights import scoring_retrieve_params
from ...types.customerinsights.scoring_retrieve_response import ScoringRetrieveResponse

__all__ = ["ScoringResource", "AsyncScoringResource"]


class ScoringResource(SyncAPIResource):
    """Customer Insights"""

    @cached_property
    def with_raw_response(self) -> ScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return ScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return ScoringResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        id_document: str | Omit = omit,
        phone_number: str | Omit = omit,
        scoring_type: Literal["gaugeMetric", "veritasIndex"] | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringRetrieveResponse:
        """
        Retrieves Scoring information, for the user associated with the provided
        `idDocument`, `phoneNumber` or the combination of both parameters. It also
        allows to select the type of the Scoring scale measurement.

        Args:
          id_document: Identification number associated to the official identity document in the
              country. It may contain alphanumeric characters.

          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          scoring_type: Scoring type, i.e.: scale. API Client may use this field to indicate the Scoring
              in one of the defined scales; if this field is not informed, the API will return
              the Scoring in the scale configured by default in the system.

              Allowed values are:

              - `gaugeMetric`: ranges from index 850 (lowest risk) to index 300 (highest risk)
              - `veritasIndex`: ranges from index 0 (lowest risk) to index 19 (highest risk)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/customerinsights/scoring/retrieve",
            body=maybe_transform(
                {
                    "id_document": id_document,
                    "phone_number": phone_number,
                    "scoring_type": scoring_type,
                },
                scoring_retrieve_params.ScoringRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringRetrieveResponse,
        )


class AsyncScoringResource(AsyncAPIResource):
    """Customer Insights"""

    @cached_property
    def with_raw_response(self) -> AsyncScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncScoringResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        id_document: str | Omit = omit,
        phone_number: str | Omit = omit,
        scoring_type: Literal["gaugeMetric", "veritasIndex"] | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScoringRetrieveResponse:
        """
        Retrieves Scoring information, for the user associated with the provided
        `idDocument`, `phoneNumber` or the combination of both parameters. It also
        allows to select the type of the Scoring scale measurement.

        Args:
          id_document: Identification number associated to the official identity document in the
              country. It may contain alphanumeric characters.

          phone_number: A public identifier addressing a telephone subscription. In mobile networks it
              corresponds to the MSISDN (Mobile Station International Subscriber Directory
              Number). In order to be globally unique it has to be formatted in international
              format, according to E.164 standard, prefixed with '+'.

          scoring_type: Scoring type, i.e.: scale. API Client may use this field to indicate the Scoring
              in one of the defined scales; if this field is not informed, the API will return
              the Scoring in the scale configured by default in the system.

              Allowed values are:

              - `gaugeMetric`: ranges from index 850 (lowest risk) to index 300 (highest risk)
              - `veritasIndex`: ranges from index 0 (lowest risk) to index 19 (highest risk)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/customerinsights/scoring/retrieve",
            body=await async_maybe_transform(
                {
                    "id_document": id_document,
                    "phone_number": phone_number,
                    "scoring_type": scoring_type,
                },
                scoring_retrieve_params.ScoringRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringRetrieveResponse,
        )


class ScoringResourceWithRawResponse:
    def __init__(self, scoring: ScoringResource) -> None:
        self._scoring = scoring

        self.retrieve = to_raw_response_wrapper(
            scoring.retrieve,
        )


class AsyncScoringResourceWithRawResponse:
    def __init__(self, scoring: AsyncScoringResource) -> None:
        self._scoring = scoring

        self.retrieve = async_to_raw_response_wrapper(
            scoring.retrieve,
        )


class ScoringResourceWithStreamingResponse:
    def __init__(self, scoring: ScoringResource) -> None:
        self._scoring = scoring

        self.retrieve = to_streamed_response_wrapper(
            scoring.retrieve,
        )


class AsyncScoringResourceWithStreamingResponse:
    def __init__(self, scoring: AsyncScoringResource) -> None:
        self._scoring = scoring

        self.retrieve = async_to_streamed_response_wrapper(
            scoring.retrieve,
        )
