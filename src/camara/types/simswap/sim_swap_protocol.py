# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["SimSwapProtocol"]

SimSwapProtocol: TypeAlias = Literal["HTTP", "MQTT3", "MQTT5", "AMQP", "NATS", "KAFKA"]
