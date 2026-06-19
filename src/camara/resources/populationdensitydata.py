# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import populationdensitydata_retrieve_params
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
from ..types.populationdensitydata_retrieve_response import PopulationdensitydataRetrieveResponse

__all__ = ["PopulationdensitydataResource", "AsyncPopulationdensitydataResource"]


class PopulationdensitydataResource(SyncAPIResource):
    """Population Density Data"""

    @cached_property
    def with_raw_response(self) -> PopulationdensitydataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return PopulationdensitydataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PopulationdensitydataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return PopulationdensitydataResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        area: populationdensitydata_retrieve_params.Area,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        precision: int | Omit = omit,
        sink: str | Omit = omit,
        sink_credential: populationdensitydata_retrieve_params.SinkCredential | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PopulationdensitydataRetrieveResponse:
        """
        Retrieves population density estimation together with the estimation range
        related for a time slot for a given area (described as a polygon) as a data set
        consisting of a sequence of equally-sized objects covering the input polygon
        area.

        Args:
          area: Base schema for all areas

          end_time: End date time. It must follow
              [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
              have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ (i.e. which
              allows 2023-07-03T14:27:08.312+02:00 or 2023-07-03T12:27:08.312Z) The maximum
              endTime allowed is 3 months from the time of the request.

          start_time: Start date time. It must follow
              [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
              have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ

          precision: Precision required of response cells. Precision defines a geohash level and
              corresponds to the length of the geohash for each cell. More information at
              [Geohash system](https://en.wikipedia.org/wiki/Geohash)" If not included the
              default precision level 7 is used by default. In case of using a not supported
              level by the MNO, the API returns the error response
              `POPULATION_DENSITY_DATA.UNSUPPORTED_PRECISION`.

          sink: The address where the API response will be asynchronously delivered, using the
              HTTP protocol.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/populationdensitydata/retrieve",
            body=maybe_transform(
                {
                    "area": area,
                    "end_time": end_time,
                    "start_time": start_time,
                    "precision": precision,
                    "sink": sink,
                    "sink_credential": sink_credential,
                },
                populationdensitydata_retrieve_params.PopulationdensitydataRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PopulationdensitydataRetrieveResponse,
        )


class AsyncPopulationdensitydataResource(AsyncAPIResource):
    """Population Density Data"""

    @cached_property
    def with_raw_response(self) -> AsyncPopulationdensitydataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPopulationdensitydataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPopulationdensitydataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncPopulationdensitydataResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        area: populationdensitydata_retrieve_params.Area,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        precision: int | Omit = omit,
        sink: str | Omit = omit,
        sink_credential: populationdensitydata_retrieve_params.SinkCredential | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PopulationdensitydataRetrieveResponse:
        """
        Retrieves population density estimation together with the estimation range
        related for a time slot for a given area (described as a polygon) as a data set
        consisting of a sequence of equally-sized objects covering the input polygon
        area.

        Args:
          area: Base schema for all areas

          end_time: End date time. It must follow
              [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
              have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ (i.e. which
              allows 2023-07-03T14:27:08.312+02:00 or 2023-07-03T12:27:08.312Z) The maximum
              endTime allowed is 3 months from the time of the request.

          start_time: Start date time. It must follow
              [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
              have time zone. Recommended format is yyyy-MM-dd'T'HH:mm:ss.SSSZ

          precision: Precision required of response cells. Precision defines a geohash level and
              corresponds to the length of the geohash for each cell. More information at
              [Geohash system](https://en.wikipedia.org/wiki/Geohash)" If not included the
              default precision level 7 is used by default. In case of using a not supported
              level by the MNO, the API returns the error response
              `POPULATION_DENSITY_DATA.UNSUPPORTED_PRECISION`.

          sink: The address where the API response will be asynchronously delivered, using the
              HTTP protocol.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/populationdensitydata/retrieve",
            body=await async_maybe_transform(
                {
                    "area": area,
                    "end_time": end_time,
                    "start_time": start_time,
                    "precision": precision,
                    "sink": sink,
                    "sink_credential": sink_credential,
                },
                populationdensitydata_retrieve_params.PopulationdensitydataRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PopulationdensitydataRetrieveResponse,
        )


class PopulationdensitydataResourceWithRawResponse:
    def __init__(self, populationdensitydata: PopulationdensitydataResource) -> None:
        self._populationdensitydata = populationdensitydata

        self.retrieve = to_raw_response_wrapper(
            populationdensitydata.retrieve,
        )


class AsyncPopulationdensitydataResourceWithRawResponse:
    def __init__(self, populationdensitydata: AsyncPopulationdensitydataResource) -> None:
        self._populationdensitydata = populationdensitydata

        self.retrieve = async_to_raw_response_wrapper(
            populationdensitydata.retrieve,
        )


class PopulationdensitydataResourceWithStreamingResponse:
    def __init__(self, populationdensitydata: PopulationdensitydataResource) -> None:
        self._populationdensitydata = populationdensitydata

        self.retrieve = to_streamed_response_wrapper(
            populationdensitydata.retrieve,
        )


class AsyncPopulationdensitydataResourceWithStreamingResponse:
    def __init__(self, populationdensitydata: AsyncPopulationdensitydataResource) -> None:
        self._populationdensitydata = populationdensitydata

        self.retrieve = async_to_streamed_response_wrapper(
            populationdensitydata.retrieve,
        )
