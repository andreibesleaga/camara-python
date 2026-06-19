# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    deviceidentifier_retrieve_ppid_params,
    deviceidentifier_retrieve_type_params,
    deviceidentifier_retrieve_identifier_params,
)
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
from ..types.device_identifier_device_param import DeviceIdentifierDeviceParam
from ..types.deviceidentifier_retrieve_ppid_response import DeviceidentifierRetrievePpidResponse
from ..types.deviceidentifier_retrieve_type_response import DeviceidentifierRetrieveTypeResponse
from ..types.deviceidentifier_retrieve_identifier_response import DeviceidentifierRetrieveIdentifierResponse

__all__ = ["DeviceidentifierResource", "AsyncDeviceidentifierResource"]


class DeviceidentifierResource(SyncAPIResource):
    """Device Identifier"""

    @cached_property
    def with_raw_response(self) -> DeviceidentifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return DeviceidentifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeviceidentifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return DeviceidentifierResourceWithStreamingResponse(self)

    def retrieve_identifier(
        self,
        *,
        device: DeviceIdentifierDeviceParam | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceidentifierRetrieveIdentifierResponse:
        """
        Get details about the specific device being used by a given mobile subscriber

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators. The developer can choose to
              provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber`
              - `networkAccessIdentifier` NOTE 1: The MNO might support only a subset of these
                options. The API invoker can provide multiple identifiers to be compatible
                across different MNOs. In this case the identifiers MUST belong to the same
                device. NOTE 2: For the current Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/deviceidentifier/retrieve-identifier",
            body=maybe_transform(
                {"device": device}, deviceidentifier_retrieve_identifier_params.DeviceidentifierRetrieveIdentifierParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceidentifierRetrieveIdentifierResponse,
        )

    def retrieve_ppid(
        self,
        *,
        device: DeviceIdentifierDeviceParam | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceidentifierRetrievePpidResponse:
        """
        Get a pseudonymous identifier for device being used by a given mobile subscriber

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators. The developer can choose to
              provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber`
              - `networkAccessIdentifier` NOTE 1: The MNO might support only a subset of these
                options. The API invoker can provide multiple identifiers to be compatible
                across different MNOs. In this case the identifiers MUST belong to the same
                device. NOTE 2: For the current Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/deviceidentifier/retrieve-ppid",
            body=maybe_transform(
                {"device": device}, deviceidentifier_retrieve_ppid_params.DeviceidentifierRetrievePpidParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceidentifierRetrievePpidResponse,
        )

    def retrieve_type(
        self,
        *,
        device: DeviceIdentifierDeviceParam | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceidentifierRetrieveTypeResponse:
        """
        Get details about the type of device being used by a given mobile subscriber

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators. The developer can choose to
              provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber`
              - `networkAccessIdentifier` NOTE 1: The MNO might support only a subset of these
                options. The API invoker can provide multiple identifiers to be compatible
                across different MNOs. In this case the identifiers MUST belong to the same
                device. NOTE 2: For the current Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return self._post(
            "/deviceidentifier/retrieve-type",
            body=maybe_transform(
                {"device": device}, deviceidentifier_retrieve_type_params.DeviceidentifierRetrieveTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceidentifierRetrieveTypeResponse,
        )


class AsyncDeviceidentifierResource(AsyncAPIResource):
    """Device Identifier"""

    @cached_property
    def with_raw_response(self) -> AsyncDeviceidentifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/camara-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDeviceidentifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeviceidentifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/camara-python#with_streaming_response
        """
        return AsyncDeviceidentifierResourceWithStreamingResponse(self)

    async def retrieve_identifier(
        self,
        *,
        device: DeviceIdentifierDeviceParam | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceidentifierRetrieveIdentifierResponse:
        """
        Get details about the specific device being used by a given mobile subscriber

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators. The developer can choose to
              provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber`
              - `networkAccessIdentifier` NOTE 1: The MNO might support only a subset of these
                options. The API invoker can provide multiple identifiers to be compatible
                across different MNOs. In this case the identifiers MUST belong to the same
                device. NOTE 2: For the current Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/deviceidentifier/retrieve-identifier",
            body=await async_maybe_transform(
                {"device": device}, deviceidentifier_retrieve_identifier_params.DeviceidentifierRetrieveIdentifierParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceidentifierRetrieveIdentifierResponse,
        )

    async def retrieve_ppid(
        self,
        *,
        device: DeviceIdentifierDeviceParam | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceidentifierRetrievePpidResponse:
        """
        Get a pseudonymous identifier for device being used by a given mobile subscriber

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators. The developer can choose to
              provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber`
              - `networkAccessIdentifier` NOTE 1: The MNO might support only a subset of these
                options. The API invoker can provide multiple identifiers to be compatible
                across different MNOs. In this case the identifiers MUST belong to the same
                device. NOTE 2: For the current Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/deviceidentifier/retrieve-ppid",
            body=await async_maybe_transform(
                {"device": device}, deviceidentifier_retrieve_ppid_params.DeviceidentifierRetrievePpidParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceidentifierRetrievePpidResponse,
        )

    async def retrieve_type(
        self,
        *,
        device: DeviceIdentifierDeviceParam | Omit = omit,
        x_correlator: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceidentifierRetrieveTypeResponse:
        """
        Get details about the type of device being used by a given mobile subscriber

        Args:
          device: End-user equipment able to connect to a mobile network. Examples of devices
              include smartphones or IoT sensors/actuators. The developer can choose to
              provide the below specified device identifiers:

              - `ipv4Address`
              - `ipv6Address`
              - `phoneNumber`
              - `networkAccessIdentifier` NOTE 1: The MNO might support only a subset of these
                options. The API invoker can provide multiple identifiers to be compatible
                across different MNOs. In this case the identifiers MUST belong to the same
                device. NOTE 2: For the current Commonalities release, we are enforcing that
                the networkAccessIdentifier is only part of the schema for future-proofing,
                and CAMARA does not currently allow its use. After the CAMARA meta-release
                work is concluded and the relevant issues are resolved, its use will need to
                be explicitly documented in the guidelines.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-correlator": x_correlator}), **(extra_headers or {})}
        return await self._post(
            "/deviceidentifier/retrieve-type",
            body=await async_maybe_transform(
                {"device": device}, deviceidentifier_retrieve_type_params.DeviceidentifierRetrieveTypeParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceidentifierRetrieveTypeResponse,
        )


class DeviceidentifierResourceWithRawResponse:
    def __init__(self, deviceidentifier: DeviceidentifierResource) -> None:
        self._deviceidentifier = deviceidentifier

        self.retrieve_identifier = to_raw_response_wrapper(
            deviceidentifier.retrieve_identifier,
        )
        self.retrieve_ppid = to_raw_response_wrapper(
            deviceidentifier.retrieve_ppid,
        )
        self.retrieve_type = to_raw_response_wrapper(
            deviceidentifier.retrieve_type,
        )


class AsyncDeviceidentifierResourceWithRawResponse:
    def __init__(self, deviceidentifier: AsyncDeviceidentifierResource) -> None:
        self._deviceidentifier = deviceidentifier

        self.retrieve_identifier = async_to_raw_response_wrapper(
            deviceidentifier.retrieve_identifier,
        )
        self.retrieve_ppid = async_to_raw_response_wrapper(
            deviceidentifier.retrieve_ppid,
        )
        self.retrieve_type = async_to_raw_response_wrapper(
            deviceidentifier.retrieve_type,
        )


class DeviceidentifierResourceWithStreamingResponse:
    def __init__(self, deviceidentifier: DeviceidentifierResource) -> None:
        self._deviceidentifier = deviceidentifier

        self.retrieve_identifier = to_streamed_response_wrapper(
            deviceidentifier.retrieve_identifier,
        )
        self.retrieve_ppid = to_streamed_response_wrapper(
            deviceidentifier.retrieve_ppid,
        )
        self.retrieve_type = to_streamed_response_wrapper(
            deviceidentifier.retrieve_type,
        )


class AsyncDeviceidentifierResourceWithStreamingResponse:
    def __init__(self, deviceidentifier: AsyncDeviceidentifierResource) -> None:
        self._deviceidentifier = deviceidentifier

        self.retrieve_identifier = async_to_streamed_response_wrapper(
            deviceidentifier.retrieve_identifier,
        )
        self.retrieve_ppid = async_to_streamed_response_wrapper(
            deviceidentifier.retrieve_ppid,
        )
        self.retrieve_type = async_to_streamed_response_wrapper(
            deviceidentifier.retrieve_type,
        )
