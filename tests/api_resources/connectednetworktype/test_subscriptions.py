# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara._utils import parse_datetime
from camara.types.connectednetworktype import (
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
    ConnectedNetworkTypeSubscription,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.create(
            config={"subscription_detail": {}},
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.create(
            config={
                "subscription_detail": {
                    "device": {
                        "ipv4_address": {
                            "private_address": "84.125.93.10",
                            "public_address": "84.125.93.10",
                            "public_port": 59765,
                        },
                        "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                        "network_access_identifier": "123456789@example.com",
                        "phone_number": "+123456789",
                    }
                },
                "initial_event": True,
                "subscription_expire_time": parse_datetime("2023-01-17T13:18:23.682Z"),
                "subscription_max_events": 5,
            },
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
            sink_credential={"credential_type": "ACCESSTOKEN"},
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Camara) -> None:
        response = client.connectednetworktype.subscriptions.with_raw_response.create(
            config={"subscription_detail": {}},
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Camara) -> None:
        with client.connectednetworktype.subscriptions.with_streaming_response.create(
            config={"subscription_detail": {}},
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.retrieve(
            subscription_id="qs15-h556-rt89-1298",
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.retrieve(
            subscription_id="qs15-h556-rt89-1298",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Camara) -> None:
        response = client.connectednetworktype.subscriptions.with_raw_response.retrieve(
            subscription_id="qs15-h556-rt89-1298",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Camara) -> None:
        with client.connectednetworktype.subscriptions.with_streaming_response.retrieve(
            subscription_id="qs15-h556-rt89-1298",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Camara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.connectednetworktype.subscriptions.with_raw_response.retrieve(
                subscription_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.list()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.list(
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Camara) -> None:
        response = client.connectednetworktype.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Camara) -> None:
        with client.connectednetworktype.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.delete(
            subscription_id="qs15-h556-rt89-1298",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Camara) -> None:
        subscription = client.connectednetworktype.subscriptions.delete(
            subscription_id="qs15-h556-rt89-1298",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Camara) -> None:
        response = client.connectednetworktype.subscriptions.with_raw_response.delete(
            subscription_id="qs15-h556-rt89-1298",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Camara) -> None:
        with client.connectednetworktype.subscriptions.with_streaming_response.delete(
            subscription_id="qs15-h556-rt89-1298",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Camara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            client.connectednetworktype.subscriptions.with_raw_response.delete(
                subscription_id="",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.create(
            config={"subscription_detail": {}},
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.create(
            config={
                "subscription_detail": {
                    "device": {
                        "ipv4_address": {
                            "private_address": "84.125.93.10",
                            "public_address": "84.125.93.10",
                            "public_port": 59765,
                        },
                        "ipv6_address": "2001:db8:85a3:8d3:1319:8a2e:370:7344",
                        "network_access_identifier": "123456789@example.com",
                        "phone_number": "+123456789",
                    }
                },
                "initial_event": True,
                "subscription_expire_time": parse_datetime("2023-01-17T13:18:23.682Z"),
                "subscription_max_events": 5,
            },
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
            sink_credential={"credential_type": "ACCESSTOKEN"},
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCamara) -> None:
        response = await async_client.connectednetworktype.subscriptions.with_raw_response.create(
            config={"subscription_detail": {}},
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCamara) -> None:
        async with async_client.connectednetworktype.subscriptions.with_streaming_response.create(
            config={"subscription_detail": {}},
            protocol="HTTP",
            sink="https://endpoint.example.com/sink",
            types=["org.camaraproject.connected-network-type-subscriptions.v0.network-type-changed"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.retrieve(
            subscription_id="qs15-h556-rt89-1298",
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.retrieve(
            subscription_id="qs15-h556-rt89-1298",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCamara) -> None:
        response = await async_client.connectednetworktype.subscriptions.with_raw_response.retrieve(
            subscription_id="qs15-h556-rt89-1298",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCamara) -> None:
        async with async_client.connectednetworktype.subscriptions.with_streaming_response.retrieve(
            subscription_id="qs15-h556-rt89-1298",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(ConnectedNetworkTypeSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCamara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.connectednetworktype.subscriptions.with_raw_response.retrieve(
                subscription_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.list()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.list(
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCamara) -> None:
        response = await async_client.connectednetworktype.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCamara) -> None:
        async with async_client.connectednetworktype.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.delete(
            subscription_id="qs15-h556-rt89-1298",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCamara) -> None:
        subscription = await async_client.connectednetworktype.subscriptions.delete(
            subscription_id="qs15-h556-rt89-1298",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCamara) -> None:
        response = await async_client.connectednetworktype.subscriptions.with_raw_response.delete(
            subscription_id="qs15-h556-rt89-1298",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCamara) -> None:
        async with async_client.connectednetworktype.subscriptions.with_streaming_response.delete(
            subscription_id="qs15-h556-rt89-1298",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCamara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `subscription_id` but received ''"):
            await async_client.connectednetworktype.subscriptions.with_raw_response.delete(
                subscription_id="",
            )
