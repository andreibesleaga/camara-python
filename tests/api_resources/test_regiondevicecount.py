# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import RegiondevicecountGetCountResponse
from camara._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegiondevicecount:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_count(self, client: Camara) -> None:
        regiondevicecount = client.regiondevicecount.get_count()
        assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_count_with_all_params(self, client: Camara) -> None:
        regiondevicecount = client.regiondevicecount.get_count(
            area={"area_type": "CIRCLE"},
            endtime=parse_datetime("2023-07-04T14:27:08.312+02:00"),
            filter={
                "device_type": ["human device", "IoT device"],
                "roaming_status": ["roaming"],
            },
            sink="https://endpoint.example.com/sink",
            sink_credential={"credential_type": "ACCESSTOKEN"},
            starttime=parse_datetime("2023-07-03T14:27:08.312+02:00"),
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_count(self, client: Camara) -> None:
        response = client.regiondevicecount.with_raw_response.get_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regiondevicecount = response.parse()
        assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_count(self, client: Camara) -> None:
        with client.regiondevicecount.with_streaming_response.get_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regiondevicecount = response.parse()
            assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegiondevicecount:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_count(self, async_client: AsyncCamara) -> None:
        regiondevicecount = await async_client.regiondevicecount.get_count()
        assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_count_with_all_params(self, async_client: AsyncCamara) -> None:
        regiondevicecount = await async_client.regiondevicecount.get_count(
            area={"area_type": "CIRCLE"},
            endtime=parse_datetime("2023-07-04T14:27:08.312+02:00"),
            filter={
                "device_type": ["human device", "IoT device"],
                "roaming_status": ["roaming"],
            },
            sink="https://endpoint.example.com/sink",
            sink_credential={"credential_type": "ACCESSTOKEN"},
            starttime=parse_datetime("2023-07-03T14:27:08.312+02:00"),
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_count(self, async_client: AsyncCamara) -> None:
        response = await async_client.regiondevicecount.with_raw_response.get_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regiondevicecount = await response.parse()
        assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_count(self, async_client: AsyncCamara) -> None:
        async with async_client.regiondevicecount.with_streaming_response.get_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regiondevicecount = await response.parse()
            assert_matches_type(RegiondevicecountGetCountResponse, regiondevicecount, path=["response"])

        assert cast(Any, response.is_closed) is True
