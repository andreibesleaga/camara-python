# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .rate import Rate
from .._models import BaseModel
from .duration import Duration
from .qos_profile_status import QosProfileStatus

__all__ = ["QosProfile", "CountryAvailability"]


class CountryAvailability(BaseModel):
    country_name: str = FieldInfo(alias="countryName")
    """
    The two letter ISO 3166-2 country code for the country in which the QoS profile
    is available in at least one network
    """

    networks: Optional[List[str]] = None
    """
    A list of networks within the country for which the QoS profile is available
    from the API provider
    """


class QosProfile(BaseModel):
    """Data type with attributes of a QosProfile"""

    name: str
    """
    A unique name for identifying a specific QoS profile. This may follow different
    formats depending on the service providers implementation. Some options
    addresses:

    - A UUID style string
    - Support for predefined profile names like `QOS_E`, `QOS_S`, `QOS_M`, and
      `QOS_L`
    - A searchable descriptive name
    """

    status: QosProfileStatus
    """The current status of the QoS Profile

    - `ACTIVE`- QoS Profile is available to be used
    - `INACTIVE`- QoS Profile is not currently available to be deployed
    - `DEPRECATED`- QoS profile is actively being used in a QoD session, but can not
      be deployed in new QoD sessions
    """

    country_availability: Optional[List[CountryAvailability]] = FieldInfo(alias="countryAvailability", default=None)
    """
    A list of countries, and optionally networks, for which the API provider makes
    the profile available
    """

    description: Optional[str] = None
    """A description of the QoS profile."""

    jitter: Optional[Duration] = None
    """Specification of duration"""

    l4s_queue_type: Optional[Literal["non-l4s-queue", "l4s-queue", "mixed-queue"]] = FieldInfo(
        alias="l4sQueueType", default=None
    )
    """
    **NOTE**: l4sQueueType is experimental and could change or be removed in a
    future release.

    Specifies the type of queue for L4S (Low Latency, Low Loss, Scalable Throughput)
    traffic management. L4S is an advanced queue management approach designed to
    provide ultra-low latency and high throughput for internet traffic, particularly
    beneficial for interactive applications such as gaming, video conferencing, and
    virtual reality.

    **Queue Type Descriptions:**

    - **non-l4s-queue**: A traditional queue used for legacy internet traffic that
      does not utilize L4S enhancements. It provides standard latency and throughput
      levels.

    - **l4s-queue**: A dedicated queue optimized for L4S traffic, delivering
      ultra-low latency, low loss, and scalable throughput to support
      latency-sensitive applications.

    - **mixed-queue**: A shared queue that can handle both L4S and traditional
      traffic, offering a balance between ultra-low latency for L4S flows and
      compatibility with non-L4S flows.
    """

    max_downstream_burst_rate: Optional[Rate] = FieldInfo(alias="maxDownstreamBurstRate", default=None)
    """Specification of rate"""

    max_downstream_rate: Optional[Rate] = FieldInfo(alias="maxDownstreamRate", default=None)
    """Specification of rate"""

    max_duration: Optional[Duration] = FieldInfo(alias="maxDuration", default=None)
    """Specification of duration"""

    max_upstream_burst_rate: Optional[Rate] = FieldInfo(alias="maxUpstreamBurstRate", default=None)
    """Specification of rate"""

    max_upstream_rate: Optional[Rate] = FieldInfo(alias="maxUpstreamRate", default=None)
    """Specification of rate"""

    min_duration: Optional[Duration] = FieldInfo(alias="minDuration", default=None)
    """Specification of duration"""

    packet_delay_budget: Optional[Duration] = FieldInfo(alias="packetDelayBudget", default=None)
    """Specification of duration"""

    packet_error_loss_rate: Optional[int] = FieldInfo(alias="packetErrorLossRate", default=None)
    """
    This field specifies the acceptable level of data loss during transmission. The
    value is an exponent of 10, so a value of 3 means that up to 10⁻³, or 0.1%, of
    the data packets may be lost. This setting is part of a broader system that
    categorizes different types of network traffic (like phone calls, video streams,
    or data transfers) to ensure they perform reliably on the network.
    """

    priority: Optional[int] = None
    """
    Priority levels allow efficient resource allocation and ensure optimal
    performance for various services in each technology, with the highest priority
    traffic receiving preferential treatment. The lower value the higher priority.
    Not all access networks use the same priority range, so this priority will be
    scaled to the access network's priority range.
    """

    service_class: Optional[
        Literal[
            "microsoft_voice",
            "microsoft_audio_video",
            "real_time_interactive",
            "multimedia_streaming",
            "broadcast_video",
            "low_latency_data",
            "high_throughput_data",
            "low_priority_data",
            "standard",
        ]
    ] = FieldInfo(alias="serviceClass", default=None)
    """
    **NOTE**: serviceClass is experimental and could change or be removed in a
    future release.

    The name of a Service Class, representing a QoS Profile designed to provide
    optimized behavior for a specific application type. While DSCP values are
    commonly associated with Service Classes, their use may vary across network
    segments and may not be applied throughout the entire end-to-end QoS session.
    This aligns with the serviceClass concept used in HomeDevicesQoQ for consistent
    terminology.

    Service classes define specific QoS behaviors that map to DSCP (Differentiated
    Services Code Point) values or Microsoft QoS traffic types.

    The supported mappings are:

    1. Values aligned with the
       [RFC4594](https://datatracker.ietf.org/doc/html/rfc4594) guidelines for
       differentiated traffic classes.
    2. Microsoft
       [QOS_TRAFFIC_TYPE](https://learn.microsoft.com/en-us/windows/win32/api/qos2/ne-qos2-qos_traffic_type)
       values for Windows developers.

    **Supported Service Classes**:

    | Service Class Name    | DSCP Name | DSCP value (decimal) | DCSP value (binary) | Microsoft Value | Application Examples                                                 |
    | --------------------- | --------- | -------------------- | ------------------- | --------------- | -------------------------------------------------------------------- |
    | Microsoft Voice       | CS7       | 56                   | 111000              | 4,5             | Microsoft QOSTrafficTypeVoice and QOSTrafficTypeControl              |
    | Microsoft Audio/Video | CS5       | 40                   | 101000              | 2,3             | Microsoft QOSTrafficTypeExcellentEffort and QOSTrafficTypeAudioVideo |
    | Real-Time Interactive | CS4       | 32                   | 100000              |                 | Video conferencing and Interactive gaming                            |
    | Multimedia Streaming  | AF31      | 26                   | 011010              |                 | Streaming video and audio on demand                                  |
    | Broadcast Video       | CS3       | 24                   | 011000              |                 | Broadcast TV & live events                                           |
    | Low-Latency Data      | AF21      | 18                   | 010010              |                 | Client/server transactions Web-based ordering                        |
    | High-Throughput Data  | AF11      | 10                   | 001010              |                 | Store and forward applications                                       |
    | Low-Priority Data     | CS1       | 8                    | 001000              | 1               | Any flow that has no BW assurance - also:                            |
    |                       |           |                      |                     |                 | Microsoft QOSTrafficTypeBackground                                   |
    | Standard              | DF(CS0)   | 0                    | 000000              | 0               | Undifferentiated applications - also:                                |
    |                       |           |                      |                     |                 | Microsoft QOSTrafficTypeBestEffort                                   |
    """

    target_min_downstream_rate: Optional[Rate] = FieldInfo(alias="targetMinDownstreamRate", default=None)
    """Specification of rate"""

    target_min_upstream_rate: Optional[Rate] = FieldInfo(alias="targetMinUpstreamRate", default=None)
    """Specification of rate"""
