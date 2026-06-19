# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import (
    DeviceidentifierRetrievePpidResponse,
    DeviceidentifierRetrieveTypeResponse,
    DeviceidentifierRetrieveIdentifierResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeviceidentifier:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_identifier(self, client: Camara) -> None:
        deviceidentifier = client.deviceidentifier.retrieve_identifier()
        assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_identifier_with_all_params(self, client: Camara) -> None:
        deviceidentifier = client.deviceidentifier.retrieve_identifier(
            device={
                "ipv4_address": {
                    "private_address": "84.125.93.10",
                    "public_address": "84.125.93.10",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@example.com",
                "phone_number": "+123456789",
            },
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_identifier(self, client: Camara) -> None:
        response = client.deviceidentifier.with_raw_response.retrieve_identifier()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceidentifier = response.parse()
        assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_identifier(self, client: Camara) -> None:
        with client.deviceidentifier.with_streaming_response.retrieve_identifier() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceidentifier = response.parse()
            assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_ppid(self, client: Camara) -> None:
        deviceidentifier = client.deviceidentifier.retrieve_ppid()
        assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_ppid_with_all_params(self, client: Camara) -> None:
        deviceidentifier = client.deviceidentifier.retrieve_ppid(
            device={
                "ipv4_address": {
                    "private_address": "84.125.93.10",
                    "public_address": "84.125.93.10",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@example.com",
                "phone_number": "+123456789",
            },
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_ppid(self, client: Camara) -> None:
        response = client.deviceidentifier.with_raw_response.retrieve_ppid()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceidentifier = response.parse()
        assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_ppid(self, client: Camara) -> None:
        with client.deviceidentifier.with_streaming_response.retrieve_ppid() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceidentifier = response.parse()
            assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_type(self, client: Camara) -> None:
        deviceidentifier = client.deviceidentifier.retrieve_type()
        assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_type_with_all_params(self, client: Camara) -> None:
        deviceidentifier = client.deviceidentifier.retrieve_type(
            device={
                "ipv4_address": {
                    "private_address": "84.125.93.10",
                    "public_address": "84.125.93.10",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@example.com",
                "phone_number": "+123456789",
            },
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_type(self, client: Camara) -> None:
        response = client.deviceidentifier.with_raw_response.retrieve_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceidentifier = response.parse()
        assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_type(self, client: Camara) -> None:
        with client.deviceidentifier.with_streaming_response.retrieve_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceidentifier = response.parse()
            assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDeviceidentifier:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_identifier(self, async_client: AsyncCamara) -> None:
        deviceidentifier = await async_client.deviceidentifier.retrieve_identifier()
        assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_identifier_with_all_params(self, async_client: AsyncCamara) -> None:
        deviceidentifier = await async_client.deviceidentifier.retrieve_identifier(
            device={
                "ipv4_address": {
                    "private_address": "84.125.93.10",
                    "public_address": "84.125.93.10",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@example.com",
                "phone_number": "+123456789",
            },
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_identifier(self, async_client: AsyncCamara) -> None:
        response = await async_client.deviceidentifier.with_raw_response.retrieve_identifier()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceidentifier = await response.parse()
        assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_identifier(self, async_client: AsyncCamara) -> None:
        async with async_client.deviceidentifier.with_streaming_response.retrieve_identifier() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceidentifier = await response.parse()
            assert_matches_type(DeviceidentifierRetrieveIdentifierResponse, deviceidentifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_ppid(self, async_client: AsyncCamara) -> None:
        deviceidentifier = await async_client.deviceidentifier.retrieve_ppid()
        assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_ppid_with_all_params(self, async_client: AsyncCamara) -> None:
        deviceidentifier = await async_client.deviceidentifier.retrieve_ppid(
            device={
                "ipv4_address": {
                    "private_address": "84.125.93.10",
                    "public_address": "84.125.93.10",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@example.com",
                "phone_number": "+123456789",
            },
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_ppid(self, async_client: AsyncCamara) -> None:
        response = await async_client.deviceidentifier.with_raw_response.retrieve_ppid()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceidentifier = await response.parse()
        assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_ppid(self, async_client: AsyncCamara) -> None:
        async with async_client.deviceidentifier.with_streaming_response.retrieve_ppid() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceidentifier = await response.parse()
            assert_matches_type(DeviceidentifierRetrievePpidResponse, deviceidentifier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_type(self, async_client: AsyncCamara) -> None:
        deviceidentifier = await async_client.deviceidentifier.retrieve_type()
        assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_type_with_all_params(self, async_client: AsyncCamara) -> None:
        deviceidentifier = await async_client.deviceidentifier.retrieve_type(
            device={
                "ipv4_address": {
                    "private_address": "84.125.93.10",
                    "public_address": "84.125.93.10",
                    "public_port": 59765,
                },
                "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                "network_access_identifier": "123456789@example.com",
                "phone_number": "+123456789",
            },
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_type(self, async_client: AsyncCamara) -> None:
        response = await async_client.deviceidentifier.with_raw_response.retrieve_type()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        deviceidentifier = await response.parse()
        assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_type(self, async_client: AsyncCamara) -> None:
        async with async_client.deviceidentifier.with_streaming_response.retrieve_type() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            deviceidentifier = await response.parse()
            assert_matches_type(DeviceidentifierRetrieveTypeResponse, deviceidentifier, path=["response"])

        assert cast(Any, response.is_closed) is True
