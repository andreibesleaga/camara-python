# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import (
    DeviceswapCheckResponse,
    DeviceswapRetrieveDateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeviceswap:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check(self, client: Camara) -> None:
        deviceswap = client.deviceswap.check()
        assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_with_all_params(self, client: Camara) -> None:
        deviceswap = client.deviceswap.check(
            max_age=120,
            phone_number="+34666111333",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check(self, client: Camara) -> None:
        response = client.deviceswap.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceswap = response.parse()
        assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check(self, client: Camara) -> None:
        with client.deviceswap.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceswap = response.parse()
            assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_date(self, client: Camara) -> None:
        deviceswap = client.deviceswap.retrieve_date()
        assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_date_with_all_params(self, client: Camara) -> None:
        deviceswap = client.deviceswap.retrieve_date(
            phone_number="+34666111333",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_date(self, client: Camara) -> None:
        response = client.deviceswap.with_raw_response.retrieve_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceswap = response.parse()
        assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_date(self, client: Camara) -> None:
        with client.deviceswap.with_streaming_response.retrieve_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceswap = response.parse()
            assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeviceswap:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check(self, async_client: AsyncCamara) -> None:
        deviceswap = await async_client.deviceswap.check()
        assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncCamara) -> None:
        deviceswap = await async_client.deviceswap.check(
            max_age=120,
            phone_number="+34666111333",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncCamara) -> None:
        response = await async_client.deviceswap.with_raw_response.check()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceswap = await response.parse()
        assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncCamara) -> None:
        async with async_client.deviceswap.with_streaming_response.check() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceswap = await response.parse()
            assert_matches_type(DeviceswapCheckResponse, deviceswap, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_date(self, async_client: AsyncCamara) -> None:
        deviceswap = await async_client.deviceswap.retrieve_date()
        assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_date_with_all_params(self, async_client: AsyncCamara) -> None:
        deviceswap = await async_client.deviceswap.retrieve_date(
            phone_number="+34666111333",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_date(self, async_client: AsyncCamara) -> None:
        response = await async_client.deviceswap.with_raw_response.retrieve_date()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceswap = await response.parse()
        assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_date(self, async_client: AsyncCamara) -> None:
        async with async_client.deviceswap.with_streaming_response.retrieve_date() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceswap = await response.parse()
            assert_matches_type(DeviceswapRetrieveDateResponse, deviceswap, path=["response"])

        assert cast(Any, response.is_closed) is True
