# Customerinsights

## Scoring

Types:

```python
from camara.types.customerinsights import ScoringRetrieveResponse
```

Methods:

- <code title="post /customerinsights/scoring/retrieve">client.customerinsights.scoring.<a href="./src/camara/resources/customerinsights/scoring.py">retrieve</a>(\*\*<a href="src/camara/types/customerinsights/scoring_retrieve_params.py">params</a>) -> <a href="./src/camara/types/customerinsights/scoring_retrieve_response.py">ScoringRetrieveResponse</a></code>

# Deviceswap

Types:

```python
from camara.types import DeviceswapCheckResponse, DeviceswapRetrieveDateResponse
```

Methods:

- <code title="post /deviceswap/check">client.deviceswap.<a href="./src/camara/resources/deviceswap.py">check</a>(\*\*<a href="src/camara/types/deviceswap_check_params.py">params</a>) -> <a href="./src/camara/types/deviceswap_check_response.py">DeviceswapCheckResponse</a></code>
- <code title="post /deviceswap/retrieve-date">client.deviceswap.<a href="./src/camara/resources/deviceswap.py">retrieve_date</a>(\*\*<a href="src/camara/types/deviceswap_retrieve_date_params.py">params</a>) -> <a href="./src/camara/types/deviceswap_retrieve_date_response.py">DeviceswapRetrieveDateResponse</a></code>

# Knowyourcustomerageverification

Types:

```python
from camara.types import KnowyourcustomerageverificationVerifyResponse
```

Methods:

- <code title="post /knowyourcustomerageverification/verify">client.knowyourcustomerageverification.<a href="./src/camara/resources/knowyourcustomerageverification.py">verify</a>(\*\*<a href="src/camara/types/knowyourcustomerageverification_verify_params.py">params</a>) -> <a href="./src/camara/types/knowyourcustomerageverification_verify_response.py">KnowyourcustomerageverificationVerifyResponse</a></code>

# KnowyourcustomerfillIn

Types:

```python
from camara.types import KnowyourcustomerfillInCreateResponse
```

Methods:

- <code title="post /knowyourcustomerfill-in/fill-in">client.knowyourcustomerfill_in.<a href="./src/camara/resources/knowyourcustomerfill_in.py">create</a>(\*\*<a href="src/camara/types/knowyourcustomerfill_in_create_params.py">params</a>) -> <a href="./src/camara/types/knowyourcustomerfill_in_create_response.py">KnowyourcustomerfillInCreateResponse</a></code>

# Knowyourcustomermatch

Types:

```python
from camara.types import MatchResult, KnowyourcustomermatchMatchResponse
```

Methods:

- <code title="post /knowyourcustomermatch/match">client.knowyourcustomermatch.<a href="./src/camara/resources/knowyourcustomermatch.py">match</a>(\*\*<a href="src/camara/types/knowyourcustomermatch_match_params.py">params</a>) -> <a href="./src/camara/types/knowyourcustomermatch_match_response.py">KnowyourcustomermatchMatchResponse</a></code>

# Tenure

Types:

```python
from camara.types import TenureVerifyResponse
```

Methods:

- <code title="post /tenure/check-tenure">client.tenure.<a href="./src/camara/resources/tenure.py">verify</a>(\*\*<a href="src/camara/types/tenure_verify_params.py">params</a>) -> <a href="./src/camara/types/tenure_verify_response.py">TenureVerifyResponse</a></code>

# Numberrecycling

Types:

```python
from camara.types import NumberrecyclingCheckSubscriberChangeResponse
```

Methods:

- <code title="post /numberrecycling/check">client.numberrecycling.<a href="./src/camara/resources/numberrecycling.py">check_subscriber_change</a>(\*\*<a href="src/camara/types/numberrecycling_check_subscriber_change_params.py">params</a>) -> <a href="./src/camara/types/numberrecycling_check_subscriber_change_response.py">NumberrecyclingCheckSubscriberChangeResponse</a></code>

# Otpvalidation

Types:

```python
from camara.types import OtpvalidationSendCodeResponse
```

Methods:

- <code title="post /otpvalidation/send-code">client.otpvalidation.<a href="./src/camara/resources/otpvalidation.py">send_code</a>(\*\*<a href="src/camara/types/otpvalidation_send_code_params.py">params</a>) -> <a href="./src/camara/types/otpvalidation_send_code_response.py">OtpvalidationSendCodeResponse</a></code>
- <code title="post /otpvalidation/validate-code">client.otpvalidation.<a href="./src/camara/resources/otpvalidation.py">validate_code</a>(\*\*<a href="src/camara/types/otpvalidation_validate_code_params.py">params</a>) -> None</code>

# Callforwardingsignal

Types:

```python
from camara.types import (
    CreateCallForwardingSignal,
    CallforwardingsignalCheckActiveForwardingsResponse,
    CallforwardingsignalCheckUnconditionalForwardingResponse,
)
```

Methods:

- <code title="post /callforwardingsignal/call-forwardings">client.callforwardingsignal.<a href="./src/camara/resources/callforwardingsignal.py">check_active_forwardings</a>(\*\*<a href="src/camara/types/callforwardingsignal_check_active_forwardings_params.py">params</a>) -> <a href="./src/camara/types/callforwardingsignal_check_active_forwardings_response.py">CallforwardingsignalCheckActiveForwardingsResponse</a></code>
- <code title="post /callforwardingsignal/unconditional-call-forwardings">client.callforwardingsignal.<a href="./src/camara/resources/callforwardingsignal.py">check_unconditional_forwarding</a>(\*\*<a href="src/camara/types/callforwardingsignal_check_unconditional_forwarding_params.py">params</a>) -> <a href="./src/camara/types/callforwardingsignal_check_unconditional_forwarding_response.py">CallforwardingsignalCheckUnconditionalForwardingResponse</a></code>

# Devicelocation

## Subscriptions

Types:

```python
from camara.types.devicelocation import (
    DeviceLocationArea,
    DeviceLocationConfig,
    DeviceLocationDevice,
    DeviceLocationProtocol,
    DeviceLocationSubscription,
    DeviceLocationSubscriptionEventType,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="post /devicelocation/subscriptions">client.devicelocation.subscriptions.<a href="./src/camara/resources/devicelocation/subscriptions.py">create</a>(\*\*<a href="src/camara/types/devicelocation/subscription_create_params.py">params</a>) -> <a href="./src/camara/types/devicelocation/device_location_subscription.py">DeviceLocationSubscription</a></code>
- <code title="get /devicelocation/subscriptions/{subscriptionId}">client.devicelocation.subscriptions.<a href="./src/camara/resources/devicelocation/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/camara/types/devicelocation/device_location_subscription.py">DeviceLocationSubscription</a></code>
- <code title="get /devicelocation/subscriptions">client.devicelocation.subscriptions.<a href="./src/camara/resources/devicelocation/subscriptions.py">list</a>() -> <a href="./src/camara/types/devicelocation/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /devicelocation/subscriptions/{subscriptionId}">client.devicelocation.subscriptions.<a href="./src/camara/resources/devicelocation/subscriptions.py">delete</a>(subscription_id) -> <a href="./src/camara/types/devicelocation/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Populationdensitydata

Types:

```python
from camara.types import PopulationdensitydataRetrieveResponse
```

Methods:

- <code title="post /populationdensitydata/retrieve">client.populationdensitydata.<a href="./src/camara/resources/populationdensitydata.py">retrieve</a>(\*\*<a href="src/camara/types/populationdensitydata_retrieve_params.py">params</a>) -> <a href="./src/camara/types/populationdensitydata_retrieve_response.py">PopulationdensitydataRetrieveResponse</a></code>

# Regiondevicecount

Types:

```python
from camara.types import RegiondevicecountGetCountResponse
```

Methods:

- <code title="post /regiondevicecount/count">client.regiondevicecount.<a href="./src/camara/resources/regiondevicecount.py">get_count</a>(\*\*<a href="src/camara/types/regiondevicecount_get_count_params.py">params</a>) -> <a href="./src/camara/types/regiondevicecount_get_count_response.py">RegiondevicecountGetCountResponse</a></code>

# Webrtc

## Sessions

Types:

```python
from camara.types.webrtc import (
    MediaSessionInformation,
    SdpDescriptor,
    WebRtcCircleCoordinates,
    WebRtcEllipsoidCoordinates,
    WebRtcLocationDetails,
)
```

Methods:

- <code title="post /webrtc/sessions">client.webrtc.sessions.<a href="./src/camara/resources/webrtc/sessions.py">create</a>(\*\*<a href="src/camara/types/webrtc/session_create_params.py">params</a>) -> <a href="./src/camara/types/webrtc/media_session_information.py">MediaSessionInformation</a></code>
- <code title="get /webrtc/sessions/{mediaSessionId}">client.webrtc.sessions.<a href="./src/camara/resources/webrtc/sessions.py">retrieve</a>(media_session_id) -> <a href="./src/camara/types/webrtc/media_session_information.py">MediaSessionInformation</a></code>
- <code title="delete /webrtc/sessions/{mediaSessionId}">client.webrtc.sessions.<a href="./src/camara/resources/webrtc/sessions.py">delete</a>(media_session_id) -> None</code>
- <code title="put /webrtc/sessions/{mediaSessionId}/status">client.webrtc.sessions.<a href="./src/camara/resources/webrtc/sessions.py">update_status</a>(media_session_id, \*\*<a href="src/camara/types/webrtc/session_update_status_params.py">params</a>) -> <a href="./src/camara/types/webrtc/media_session_information.py">MediaSessionInformation</a></code>

# Connectivityinsights

## Subscriptions

Types:

```python
from camara.types.connectivityinsights import (
    Config,
    EventType,
    Protocol,
    Subscription,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="post /connectivityinsights/subscriptions">client.connectivityinsights.subscriptions.<a href="./src/camara/resources/connectivityinsights/subscriptions.py">create</a>(\*\*<a href="src/camara/types/connectivityinsights/subscription_create_params.py">params</a>) -> <a href="./src/camara/types/connectivityinsights/subscription.py">Subscription</a></code>
- <code title="get /connectivityinsights/subscriptions/{subscriptionId}">client.connectivityinsights.subscriptions.<a href="./src/camara/resources/connectivityinsights/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/camara/types/connectivityinsights/subscription.py">Subscription</a></code>
- <code title="get /connectivityinsights/subscriptions">client.connectivityinsights.subscriptions.<a href="./src/camara/resources/connectivityinsights/subscriptions.py">list</a>() -> <a href="./src/camara/types/connectivityinsights/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /connectivityinsights/subscriptions/{subscriptionId}">client.connectivityinsights.subscriptions.<a href="./src/camara/resources/connectivityinsights/subscriptions.py">delete</a>(subscription_id) -> <a href="./src/camara/types/connectivityinsights/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Qualityondemand

Types:

```python
from camara.types import (
    Duration,
    QosProfile,
    QosProfileStatus,
    Rate,
    QualityondemandRetrieveQosProfilesResponse,
)
```

Methods:

- <code title="get /qualityondemand/qos-profiles/{name}">client.qualityondemand.<a href="./src/camara/resources/qualityondemand.py">retrieve_qos_profile</a>(name) -> <a href="./src/camara/types/qos_profile.py">QosProfile</a></code>
- <code title="post /qualityondemand/retrieve-qos-profiles">client.qualityondemand.<a href="./src/camara/resources/qualityondemand.py">retrieve_qos_profiles</a>(\*\*<a href="src/camara/types/qualityondemand_retrieve_qos_profiles_params.py">params</a>) -> <a href="./src/camara/types/qualityondemand_retrieve_qos_profiles_response.py">QualityondemandRetrieveQosProfilesResponse</a></code>

# Deviceidentifier

Types:

```python
from camara.types import (
    DeviceIdentifierDevice,
    DeviceIdentifierDeviceIpv4Addr,
    DeviceIdentifierRequestBody,
    DeviceidentifierRetrieveIdentifierResponse,
    DeviceidentifierRetrievePpidResponse,
    DeviceidentifierRetrieveTypeResponse,
)
```

Methods:

- <code title="post /deviceidentifier/retrieve-identifier">client.deviceidentifier.<a href="./src/camara/resources/deviceidentifier.py">retrieve_identifier</a>(\*\*<a href="src/camara/types/deviceidentifier_retrieve_identifier_params.py">params</a>) -> <a href="./src/camara/types/deviceidentifier_retrieve_identifier_response.py">DeviceidentifierRetrieveIdentifierResponse</a></code>
- <code title="post /deviceidentifier/retrieve-ppid">client.deviceidentifier.<a href="./src/camara/resources/deviceidentifier.py">retrieve_ppid</a>(\*\*<a href="src/camara/types/deviceidentifier_retrieve_ppid_params.py">params</a>) -> <a href="./src/camara/types/deviceidentifier_retrieve_ppid_response.py">DeviceidentifierRetrievePpidResponse</a></code>
- <code title="post /deviceidentifier/retrieve-type">client.deviceidentifier.<a href="./src/camara/resources/deviceidentifier.py">retrieve_type</a>(\*\*<a href="src/camara/types/deviceidentifier_retrieve_type_params.py">params</a>) -> <a href="./src/camara/types/deviceidentifier_retrieve_type_response.py">DeviceidentifierRetrieveTypeResponse</a></code>

# Simswap

## Subscriptions

Types:

```python
from camara.types.simswap import (
    SimSwapConfig,
    SimSwapProtocol,
    SimSwapSubscription,
    SimSwapSubscriptionEventType,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="post /simswap/subscriptions">client.simswap.subscriptions.<a href="./src/camara/resources/simswap/subscriptions.py">create</a>(\*\*<a href="src/camara/types/simswap/subscription_create_params.py">params</a>) -> <a href="./src/camara/types/simswap/sim_swap_subscription.py">SimSwapSubscription</a></code>
- <code title="get /simswap/subscriptions/{subscriptionId}">client.simswap.subscriptions.<a href="./src/camara/resources/simswap/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/camara/types/simswap/sim_swap_subscription.py">SimSwapSubscription</a></code>
- <code title="get /simswap/subscriptions">client.simswap.subscriptions.<a href="./src/camara/resources/simswap/subscriptions.py">list</a>() -> <a href="./src/camara/types/simswap/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /simswap/subscriptions/{subscriptionId}">client.simswap.subscriptions.<a href="./src/camara/resources/simswap/subscriptions.py">delete</a>(subscription_id) -> <a href="./src/camara/types/simswap/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Deviceroamingstatus

## Subscriptions

Types:

```python
from camara.types.deviceroamingstatus import (
    DeviceRoamingStatusConfig,
    DeviceRoamingStatusProtocol,
    DeviceRoamingStatusSubscription,
    DeviceRoamingStatusSubscriptionEventType,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="post /deviceroamingstatus/subscriptions">client.deviceroamingstatus.subscriptions.<a href="./src/camara/resources/deviceroamingstatus/subscriptions.py">create</a>(\*\*<a href="src/camara/types/deviceroamingstatus/subscription_create_params.py">params</a>) -> <a href="./src/camara/types/deviceroamingstatus/device_roaming_status_subscription.py">DeviceRoamingStatusSubscription</a></code>
- <code title="get /deviceroamingstatus/subscriptions/{subscriptionId}">client.deviceroamingstatus.subscriptions.<a href="./src/camara/resources/deviceroamingstatus/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/camara/types/deviceroamingstatus/device_roaming_status_subscription.py">DeviceRoamingStatusSubscription</a></code>
- <code title="get /deviceroamingstatus/subscriptions">client.deviceroamingstatus.subscriptions.<a href="./src/camara/resources/deviceroamingstatus/subscriptions.py">list</a>() -> <a href="./src/camara/types/deviceroamingstatus/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /deviceroamingstatus/subscriptions/{subscriptionId}">client.deviceroamingstatus.subscriptions.<a href="./src/camara/resources/deviceroamingstatus/subscriptions.py">delete</a>(subscription_id) -> <a href="./src/camara/types/deviceroamingstatus/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Devicereachabilitystatus

## Subscriptions

Types:

```python
from camara.types.devicereachabilitystatus import (
    DeviceReachabilityStatusConfig,
    DeviceReachabilityStatusProtocol,
    DeviceReachabilityStatusSubscription,
    DeviceReachabilityStatusSubscriptionEventType,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="post /devicereachabilitystatus/subscriptions">client.devicereachabilitystatus.subscriptions.<a href="./src/camara/resources/devicereachabilitystatus/subscriptions.py">create</a>(\*\*<a href="src/camara/types/devicereachabilitystatus/subscription_create_params.py">params</a>) -> <a href="./src/camara/types/devicereachabilitystatus/device_reachability_status_subscription.py">DeviceReachabilityStatusSubscription</a></code>
- <code title="get /devicereachabilitystatus/subscriptions/{subscriptionId}">client.devicereachabilitystatus.subscriptions.<a href="./src/camara/resources/devicereachabilitystatus/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/camara/types/devicereachabilitystatus/device_reachability_status_subscription.py">DeviceReachabilityStatusSubscription</a></code>
- <code title="get /devicereachabilitystatus/subscriptions">client.devicereachabilitystatus.subscriptions.<a href="./src/camara/resources/devicereachabilitystatus/subscriptions.py">list</a>() -> <a href="./src/camara/types/devicereachabilitystatus/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /devicereachabilitystatus/subscriptions/{subscriptionId}">client.devicereachabilitystatus.subscriptions.<a href="./src/camara/resources/devicereachabilitystatus/subscriptions.py">delete</a>(subscription_id) -> <a href="./src/camara/types/devicereachabilitystatus/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>

# Connectednetworktype

## Subscriptions

Types:

```python
from camara.types.connectednetworktype import (
    ConnectedNetworkTypeConfig,
    ConnectedNetworkTypeProtocol,
    ConnectedNetworkTypeSubscription,
    ConnectedNetworkTypeSubscriptionEventType,
    SubscriptionListResponse,
    SubscriptionDeleteResponse,
)
```

Methods:

- <code title="post /connectednetworktype/subscriptions">client.connectednetworktype.subscriptions.<a href="./src/camara/resources/connectednetworktype/subscriptions.py">create</a>(\*\*<a href="src/camara/types/connectednetworktype/subscription_create_params.py">params</a>) -> <a href="./src/camara/types/connectednetworktype/connected_network_type_subscription.py">ConnectedNetworkTypeSubscription</a></code>
- <code title="get /connectednetworktype/subscriptions/{subscriptionId}">client.connectednetworktype.subscriptions.<a href="./src/camara/resources/connectednetworktype/subscriptions.py">retrieve</a>(subscription_id) -> <a href="./src/camara/types/connectednetworktype/connected_network_type_subscription.py">ConnectedNetworkTypeSubscription</a></code>
- <code title="get /connectednetworktype/subscriptions">client.connectednetworktype.subscriptions.<a href="./src/camara/resources/connectednetworktype/subscriptions.py">list</a>() -> <a href="./src/camara/types/connectednetworktype/subscription_list_response.py">SubscriptionListResponse</a></code>
- <code title="delete /connectednetworktype/subscriptions/{subscriptionId}">client.connectednetworktype.subscriptions.<a href="./src/camara/resources/connectednetworktype/subscriptions.py">delete</a>(subscription_id) -> <a href="./src/camara/types/connectednetworktype/subscription_delete_response.py">SubscriptionDeleteResponse</a></code>
