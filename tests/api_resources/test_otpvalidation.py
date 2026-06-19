# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara.types import (
    OtpvalidationSendCodeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOtpvalidation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_code(self, client: Camara) -> None:
        otpvalidation = client.otpvalidation.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
        )
        assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_code_with_all_params(self, client: Camara) -> None:
        otpvalidation = client.otpvalidation.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_code(self, client: Camara) -> None:
        response = client.otpvalidation.with_raw_response.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        otpvalidation = response.parse()
        assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_code(self, client: Camara) -> None:
        with client.otpvalidation.with_streaming_response.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            otpvalidation = response.parse()
            assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_code(self, client: Camara) -> None:
        otpvalidation = client.otpvalidation.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
        )
        assert otpvalidation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_code_with_all_params(self, client: Camara) -> None:
        otpvalidation = client.otpvalidation.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert otpvalidation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_code(self, client: Camara) -> None:
        response = client.otpvalidation.with_raw_response.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        otpvalidation = response.parse()
        assert otpvalidation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_code(self, client: Camara) -> None:
        with client.otpvalidation.with_streaming_response.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            otpvalidation = response.parse()
            assert otpvalidation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncOtpvalidation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_code(self, async_client: AsyncCamara) -> None:
        otpvalidation = await async_client.otpvalidation.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
        )
        assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_code_with_all_params(self, async_client: AsyncCamara) -> None:
        otpvalidation = await async_client.otpvalidation.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_code(self, async_client: AsyncCamara) -> None:
        response = await async_client.otpvalidation.with_raw_response.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        otpvalidation = await response.parse()
        assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_code(self, async_client: AsyncCamara) -> None:
        async with async_client.otpvalidation.with_streaming_response.send_code(
            message="{{code}} is your short code to authenticate with Cool App via SMS",
            phone_number="+346661113334",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            otpvalidation = await response.parse()
            assert_matches_type(OtpvalidationSendCodeResponse, otpvalidation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_code(self, async_client: AsyncCamara) -> None:
        otpvalidation = await async_client.otpvalidation.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
        )
        assert otpvalidation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_code_with_all_params(self, async_client: AsyncCamara) -> None:
        otpvalidation = await async_client.otpvalidation.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert otpvalidation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_code(self, async_client: AsyncCamara) -> None:
        response = await async_client.otpvalidation.with_raw_response.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        otpvalidation = await response.parse()
        assert otpvalidation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_code(self, async_client: AsyncCamara) -> None:
        async with async_client.otpvalidation.with_streaming_response.validate_code(
            authentication_id="ea0840f3-3663-4149-bd10-c7c6b8912105",
            code="AJY3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            otpvalidation = await response.parse()
            assert otpvalidation is None

        assert cast(Any, response.is_closed) is True
