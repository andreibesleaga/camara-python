# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import KnowyourcustomerfillInCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowyourcustomerfillIn:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Camara) -> None:
        knowyourcustomerfill_in = client.knowyourcustomerfill_in.create()
        assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Camara) -> None:
        knowyourcustomerfill_in = client.knowyourcustomerfill_in.create(
            phone_number="+34629255833",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Camara) -> None:
        response = client.knowyourcustomerfill_in.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowyourcustomerfill_in = response.parse()
        assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Camara) -> None:
        with client.knowyourcustomerfill_in.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowyourcustomerfill_in = response.parse()
            assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKnowyourcustomerfillIn:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCamara) -> None:
        knowyourcustomerfill_in = await async_client.knowyourcustomerfill_in.create()
        assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCamara) -> None:
        knowyourcustomerfill_in = await async_client.knowyourcustomerfill_in.create(
            phone_number="+34629255833",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCamara) -> None:
        response = await async_client.knowyourcustomerfill_in.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowyourcustomerfill_in = await response.parse()
        assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCamara) -> None:
        async with async_client.knowyourcustomerfill_in.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowyourcustomerfill_in = await response.parse()
            assert_matches_type(KnowyourcustomerfillInCreateResponse, knowyourcustomerfill_in, path=["response"])

        assert cast(Any, response.is_closed) is True
