# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from camara import Camara, AsyncCamara
from tests.utils import assert_matches_type
from camara._utils import parse_datetime
from camara.types.webrtc import (
    MediaSessionInformation,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Camara) -> None:
        session = client.webrtc.sessions.create(
            registration_id="registrationId",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Camara) -> None:
        session = client.webrtc.sessions.create(
            registration_id="registrationId",
            answer={"sdp": "sdp"},
            call_type="REGULAR",
            location_details={
                "confidence": {
                    "pdf": "normal",
                    "value": 0,
                },
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0,
                    "radius": 0,
                },
                "method": "GPS",
                "shape": "Circle",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            body_media_session_id="0AEE1B58BAEEDA3EABA42B32EBB3DFE07E9CFF402EAF9EED8EF",
            offer={
                "sdp": "v=0\r\no=- 8066321617929821805 2 IN IP4 127.0.0.1\r\ns=-\r\nt=0 0\r\nm=audio 42988 RTP/SAVPF 102 113\r\nc=IN IP6 2001:e0:410:2448:7a05:9b11:66f2:c9e\r\nb=AS:64\r\na=rtcp:9 IN IP4 0.0.0.0\r\na=candidate:1645903805 1 udp 2122262783 2001:e0:410:2448:7a05:9b11:66f2:c9e 42988 typ host generation 0 network-id 3 network-cost 900\r\na=ice-ufrag:4eKp\r\na=ice-pwd:D4sF5Pv9vx9ggaqxBlHbAFMx\r\na=ice-options:trickle renomination\r\na=mid:audio\r\na=extmap:2 http://www.ietf.org/id/draft-holmer-rmcat-transport-wide-cc-extensions-01\r\na=sendrecv\r\na=rtcp-mux\r\na=crypto:1 AES_CM_128_HMAC_SHA1_80 inline:Xm3YciqVIWFNSwy19e9MvfZ2YOdAZil7oT/tHjdf\r\na=rtpmap:102 AMR-WB/16000\r\na=fmtp:102 octet-align=0; mode-set=0,1,2; mode-change-capability=2\r\na=rtpmap:113 telephone-event/16000\r\n"
            },
            originator_address="tel:+17085852753",
            originator_name="tel:+17085852753",
            receiver_address="tel:+17085854000",
            receiver_name="tel:+17085854000",
            status="Ringing",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Camara) -> None:
        response = client.webrtc.sessions.with_raw_response.create(
            registration_id="registrationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Camara) -> None:
        with client.webrtc.sessions.with_streaming_response.create(
            registration_id="registrationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(MediaSessionInformation, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Camara) -> None:
        session = client.webrtc.sessions.retrieve(
            media_session_id="mediaSessionId",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Camara) -> None:
        session = client.webrtc.sessions.retrieve(
            media_session_id="mediaSessionId",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Camara) -> None:
        response = client.webrtc.sessions.with_raw_response.retrieve(
            media_session_id="mediaSessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Camara) -> None:
        with client.webrtc.sessions.with_streaming_response.retrieve(
            media_session_id="mediaSessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(MediaSessionInformation, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Camara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_session_id` but received ''"):
            client.webrtc.sessions.with_raw_response.retrieve(
                media_session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Camara) -> None:
        session = client.webrtc.sessions.delete(
            media_session_id="mediaSessionId",
        )
        assert session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Camara) -> None:
        session = client.webrtc.sessions.delete(
            media_session_id="mediaSessionId",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Camara) -> None:
        response = client.webrtc.sessions.with_raw_response.delete(
            media_session_id="mediaSessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Camara) -> None:
        with client.webrtc.sessions.with_streaming_response.delete(
            media_session_id="mediaSessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Camara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_session_id` but received ''"):
            client.webrtc.sessions.with_raw_response.delete(
                media_session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_status(self, client: Camara) -> None:
        session = client.webrtc.sessions.update_status(
            media_session_id="mediaSessionId",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_status_with_all_params(self, client: Camara) -> None:
        session = client.webrtc.sessions.update_status(
            media_session_id="mediaSessionId",
            answer={"sdp": "sdp"},
            call_type="REGULAR",
            location_details={
                "confidence": {
                    "pdf": "normal",
                    "value": 0,
                },
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0,
                    "radius": 0,
                },
                "method": "GPS",
                "shape": "Circle",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            body_media_session_id="0AEE1B58BAEEDA3EABA42B32EBB3DFE07E9CFF402EAF9EED8EF",
            offer={"sdp": "sdp"},
            originator_address="tel:+11234567899",
            originator_name="Alice",
            receiver_address="tel:+11234567899",
            receiver_name="Bob",
            status="Ringing",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_status(self, client: Camara) -> None:
        response = client.webrtc.sessions.with_raw_response.update_status(
            media_session_id="mediaSessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_status(self, client: Camara) -> None:
        with client.webrtc.sessions.with_streaming_response.update_status(
            media_session_id="mediaSessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(MediaSessionInformation, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_status(self, client: Camara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_session_id` but received ''"):
            client.webrtc.sessions.with_raw_response.update_status(
                media_session_id="",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.create(
            registration_id="registrationId",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.create(
            registration_id="registrationId",
            answer={"sdp": "sdp"},
            call_type="REGULAR",
            location_details={
                "confidence": {
                    "pdf": "normal",
                    "value": 0,
                },
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0,
                    "radius": 0,
                },
                "method": "GPS",
                "shape": "Circle",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            body_media_session_id="0AEE1B58BAEEDA3EABA42B32EBB3DFE07E9CFF402EAF9EED8EF",
            offer={
                "sdp": "v=0\r\no=- 8066321617929821805 2 IN IP4 127.0.0.1\r\ns=-\r\nt=0 0\r\nm=audio 42988 RTP/SAVPF 102 113\r\nc=IN IP6 2001:e0:410:2448:7a05:9b11:66f2:c9e\r\nb=AS:64\r\na=rtcp:9 IN IP4 0.0.0.0\r\na=candidate:1645903805 1 udp 2122262783 2001:e0:410:2448:7a05:9b11:66f2:c9e 42988 typ host generation 0 network-id 3 network-cost 900\r\na=ice-ufrag:4eKp\r\na=ice-pwd:D4sF5Pv9vx9ggaqxBlHbAFMx\r\na=ice-options:trickle renomination\r\na=mid:audio\r\na=extmap:2 http://www.ietf.org/id/draft-holmer-rmcat-transport-wide-cc-extensions-01\r\na=sendrecv\r\na=rtcp-mux\r\na=crypto:1 AES_CM_128_HMAC_SHA1_80 inline:Xm3YciqVIWFNSwy19e9MvfZ2YOdAZil7oT/tHjdf\r\na=rtpmap:102 AMR-WB/16000\r\na=fmtp:102 octet-align=0; mode-set=0,1,2; mode-change-capability=2\r\na=rtpmap:113 telephone-event/16000\r\n"
            },
            originator_address="tel:+17085852753",
            originator_name="tel:+17085852753",
            receiver_address="tel:+17085854000",
            receiver_name="tel:+17085854000",
            status="Ringing",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCamara) -> None:
        response = await async_client.webrtc.sessions.with_raw_response.create(
            registration_id="registrationId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCamara) -> None:
        async with async_client.webrtc.sessions.with_streaming_response.create(
            registration_id="registrationId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(MediaSessionInformation, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.retrieve(
            media_session_id="mediaSessionId",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.retrieve(
            media_session_id="mediaSessionId",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCamara) -> None:
        response = await async_client.webrtc.sessions.with_raw_response.retrieve(
            media_session_id="mediaSessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCamara) -> None:
        async with async_client.webrtc.sessions.with_streaming_response.retrieve(
            media_session_id="mediaSessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(MediaSessionInformation, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCamara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_session_id` but received ''"):
            await async_client.webrtc.sessions.with_raw_response.retrieve(
                media_session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.delete(
            media_session_id="mediaSessionId",
        )
        assert session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.delete(
            media_session_id="mediaSessionId",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCamara) -> None:
        response = await async_client.webrtc.sessions.with_raw_response.delete(
            media_session_id="mediaSessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCamara) -> None:
        async with async_client.webrtc.sessions.with_streaming_response.delete(
            media_session_id="mediaSessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCamara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_session_id` but received ''"):
            await async_client.webrtc.sessions.with_raw_response.delete(
                media_session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_status(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.update_status(
            media_session_id="mediaSessionId",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncCamara) -> None:
        session = await async_client.webrtc.sessions.update_status(
            media_session_id="mediaSessionId",
            answer={"sdp": "sdp"},
            call_type="REGULAR",
            location_details={
                "confidence": {
                    "pdf": "normal",
                    "value": 0,
                },
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0,
                    "radius": 0,
                },
                "method": "GPS",
                "shape": "Circle",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            body_media_session_id="0AEE1B58BAEEDA3EABA42B32EBB3DFE07E9CFF402EAF9EED8EF",
            offer={"sdp": "sdp"},
            originator_address="tel:+11234567899",
            originator_name="Alice",
            receiver_address="tel:+11234567899",
            receiver_name="Bob",
            status="Ringing",
            x_correlator="b4333c46-49c0-4f62-80d7-f0ef930f1c46",
        )
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncCamara) -> None:
        response = await async_client.webrtc.sessions.with_raw_response.update_status(
            media_session_id="mediaSessionId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(MediaSessionInformation, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncCamara) -> None:
        async with async_client.webrtc.sessions.with_streaming_response.update_status(
            media_session_id="mediaSessionId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(MediaSessionInformation, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncCamara) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `media_session_id` but received ''"):
            await async_client.webrtc.sessions.with_raw_response.update_status(
                media_session_id="",
            )
