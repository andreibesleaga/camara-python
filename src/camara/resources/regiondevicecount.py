# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import regiondevicecount_get_count_params
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
from ..types.regiondevicecount_get_count_response import RegiondevicecountGetCountResponse

__all__ = ["RegiondevicecountResource", "AsyncRegiondevicecountResource"]


class RegiondevicecountResource(SyncAPIResource):
    """Region Device Count"""

    @cached_property
    def with_raw_response(self) -> RegiondevicecountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return RegiondevicecountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegiondevicecountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return RegiondevicecountResourceWithStreamingResponse(self)

    def get_count(
        self,
        *,
        area: regiondevicecount_get_count_params.Area | Omit = omit,
        endtime: Union[str, datetime, None] | Omit = omit,
        filter: regiondevicecount_get_count_params.Filter | Omit = omit,
        sink: str | Omit = omit,
        sink_credential: regiondevicecount_get_count_params.SinkCredential | Omit = omit,
        starttime: Union[str, datetime, None] | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegiondevicecountGetCountResponse:
        """
        Get the number of devices in the specified area during a certain time interval.

        - The query area can be a circle or a polygon composed of longitude and latitude
          points.
        - If the areaType is circle, the circleCenter and circleRadius must be provided;
          if the area is a polygon, the point list must be provided.
        - If starttime and endtime are not passed in,this api should return the current
          number of devices in the area.
        - If the device appears in the specified area at least once during the certain
          time interval, it should be counted.

        Args:
          endtime: Ending timestamp for counting the number of devices in the area. It must follow
              [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
              have time zone.

          filter: This parameter is used to filter devices. Currently, two filtering criteria are
              defined, `roamingStatus` and `deviceType`, which can be expanded in the future.
              `IN` logic is used used for multiple filtering items within a single filtering
              criterion, `AND` logic is used between multiple filtering criteria.

              - If a filtering critera is not provided, it means that there is no need to
                filter this item.
              - At least one of the criteria must be provided,a filter without any criteria is
                not allowed.
              - If no filtering is required, this parameter does not need to be provided. For
                example
                ,`"filter":{"roamingStatus": ["roaming"],"deviceType": ["human device","IoT device"]}`
                means the API need to return the count of human network devices and IoT
                devices that are in roaming mode.`"filter":{"roamingStatus": ["non-roaming"]}`
                means that the API need to return the count of all devices that are not in
                roaming mode.

          sink: The URL where the API response will be asynchronously delivered, using the HTTP
              protocol.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          starttime: Starting timestamp for counting the number of devices in the area. It must
              follow [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and
              must have time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/regiondevicecount/count",
            body=maybe_transform(
                {
                    "area": area,
                    "endtime": endtime,
                    "filter": filter,
                    "sink": sink,
                    "sink_credential": sink_credential,
                    "starttime": starttime,
                },
                regiondevicecount_get_count_params.RegiondevicecountGetCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegiondevicecountGetCountResponse,
        )


class AsyncRegiondevicecountResource(AsyncAPIResource):
    """Region Device Count"""

    @cached_property
    def with_raw_response(self) -> AsyncRegiondevicecountResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/andreibesleaga/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegiondevicecountResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegiondevicecountResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/andreibesleaga/camara-python#with_streaming_response
        """
        return AsyncRegiondevicecountResourceWithStreamingResponse(self)

    async def get_count(
        self,
        *,
        area: regiondevicecount_get_count_params.Area | Omit = omit,
        endtime: Union[str, datetime, None] | Omit = omit,
        filter: regiondevicecount_get_count_params.Filter | Omit = omit,
        sink: str | Omit = omit,
        sink_credential: regiondevicecount_get_count_params.SinkCredential | Omit = omit,
        starttime: Union[str, datetime, None] | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RegiondevicecountGetCountResponse:
        """
        Get the number of devices in the specified area during a certain time interval.

        - The query area can be a circle or a polygon composed of longitude and latitude
          points.
        - If the areaType is circle, the circleCenter and circleRadius must be provided;
          if the area is a polygon, the point list must be provided.
        - If starttime and endtime are not passed in,this api should return the current
          number of devices in the area.
        - If the device appears in the specified area at least once during the certain
          time interval, it should be counted.

        Args:
          endtime: Ending timestamp for counting the number of devices in the area. It must follow
              [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and must
              have time zone.

          filter: This parameter is used to filter devices. Currently, two filtering criteria are
              defined, `roamingStatus` and `deviceType`, which can be expanded in the future.
              `IN` logic is used used for multiple filtering items within a single filtering
              criterion, `AND` logic is used between multiple filtering criteria.

              - If a filtering critera is not provided, it means that there is no need to
                filter this item.
              - At least one of the criteria must be provided,a filter without any criteria is
                not allowed.
              - If no filtering is required, this parameter does not need to be provided. For
                example
                ,`"filter":{"roamingStatus": ["roaming"],"deviceType": ["human device","IoT device"]}`
                means the API need to return the count of human network devices and IoT
                devices that are in roaming mode.`"filter":{"roamingStatus": ["non-roaming"]}`
                means that the API need to return the count of all devices that are not in
                roaming mode.

          sink: The URL where the API response will be asynchronously delivered, using the HTTP
              protocol.

          sink_credential: A sink credential provides authentication or authorization information necessary
              to enable delivery of events to a target.

          starttime: Starting timestamp for counting the number of devices in the area. It must
              follow [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) and
              must have time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/regiondevicecount/count",
            body=await async_maybe_transform(
                {
                    "area": area,
                    "endtime": endtime,
                    "filter": filter,
                    "sink": sink,
                    "sink_credential": sink_credential,
                    "starttime": starttime,
                },
                regiondevicecount_get_count_params.RegiondevicecountGetCountParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegiondevicecountGetCountResponse,
        )


class RegiondevicecountResourceWithRawResponse:
    def __init__(self, regiondevicecount: RegiondevicecountResource) -> None:
        self._regiondevicecount = regiondevicecount

        self.get_count = to_raw_response_wrapper(
            regiondevicecount.get_count,
        )


class AsyncRegiondevicecountResourceWithRawResponse:
    def __init__(self, regiondevicecount: AsyncRegiondevicecountResource) -> None:
        self._regiondevicecount = regiondevicecount

        self.get_count = async_to_raw_response_wrapper(
            regiondevicecount.get_count,
        )


class RegiondevicecountResourceWithStreamingResponse:
    def __init__(self, regiondevicecount: RegiondevicecountResource) -> None:
        self._regiondevicecount = regiondevicecount

        self.get_count = to_streamed_response_wrapper(
            regiondevicecount.get_count,
        )


class AsyncRegiondevicecountResourceWithStreamingResponse:
    def __init__(self, regiondevicecount: AsyncRegiondevicecountResource) -> None:
        self._regiondevicecount = regiondevicecount

        self.get_count = async_to_streamed_response_wrapper(
            regiondevicecount.get_count,
        )
