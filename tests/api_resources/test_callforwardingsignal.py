# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import (
    CallforwardingsignalCheckActiveForwardingsResponse,
    CallforwardingsignalCheckUnconditionalForwardingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallforwardingsignal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_active_forwardings(self, client: Camara) -> None:
        callforwardingsignal = client.callforwardingsignal.check_active_forwardings()
        assert_matches_type(CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_active_forwardings_with_all_params(self, client: Camara) -> None:
        callforwardingsignal = client.callforwardingsignal.check_active_forwardings(
            phone_number="+123456789",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_active_forwardings(self, client: Camara) -> None:
        response = client.callforwardingsignal.with_raw_response.check_active_forwardings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callforwardingsignal = response.parse()
        assert_matches_type(CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_active_forwardings(self, client: Camara) -> None:
        with client.callforwardingsignal.with_streaming_response.check_active_forwardings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callforwardingsignal = response.parse()
            assert_matches_type(
                CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_unconditional_forwarding(self, client: Camara) -> None:
        callforwardingsignal = client.callforwardingsignal.check_unconditional_forwarding()
        assert_matches_type(
            CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_unconditional_forwarding_with_all_params(self, client: Camara) -> None:
        callforwardingsignal = client.callforwardingsignal.check_unconditional_forwarding(
            phone_number="+123456789",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(
            CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_unconditional_forwarding(self, client: Camara) -> None:
        response = client.callforwardingsignal.with_raw_response.check_unconditional_forwarding()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callforwardingsignal = response.parse()
        assert_matches_type(
            CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_unconditional_forwarding(self, client: Camara) -> None:
        with client.callforwardingsignal.with_streaming_response.check_unconditional_forwarding() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callforwardingsignal = response.parse()
            assert_matches_type(
                CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncCallforwardingsignal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_active_forwardings(self, async_client: AsyncCamara) -> None:
        callforwardingsignal = await async_client.callforwardingsignal.check_active_forwardings()
        assert_matches_type(CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_active_forwardings_with_all_params(self, async_client: AsyncCamara) -> None:
        callforwardingsignal = await async_client.callforwardingsignal.check_active_forwardings(
            phone_number="+123456789",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_active_forwardings(self, async_client: AsyncCamara) -> None:
        response = await async_client.callforwardingsignal.with_raw_response.check_active_forwardings()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callforwardingsignal = await response.parse()
        assert_matches_type(CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_active_forwardings(self, async_client: AsyncCamara) -> None:
        async with async_client.callforwardingsignal.with_streaming_response.check_active_forwardings() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callforwardingsignal = await response.parse()
            assert_matches_type(
                CallforwardingsignalCheckActiveForwardingsResponse, callforwardingsignal, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_unconditional_forwarding(self, async_client: AsyncCamara) -> None:
        callforwardingsignal = await async_client.callforwardingsignal.check_unconditional_forwarding()
        assert_matches_type(
            CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_unconditional_forwarding_with_all_params(self, async_client: AsyncCamara) -> None:
        callforwardingsignal = await async_client.callforwardingsignal.check_unconditional_forwarding(
            phone_number="+123456789",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(
            CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_unconditional_forwarding(self, async_client: AsyncCamara) -> None:
        response = await async_client.callforwardingsignal.with_raw_response.check_unconditional_forwarding()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        callforwardingsignal = await response.parse()
        assert_matches_type(
            CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_unconditional_forwarding(self, async_client: AsyncCamara) -> None:
        async with (
            async_client.callforwardingsignal.with_streaming_response.check_unconditional_forwarding()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            callforwardingsignal = await response.parse()
            assert_matches_type(
                CallforwardingsignalCheckUnconditionalForwardingResponse, callforwardingsignal, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
