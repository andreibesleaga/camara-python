# Camara Python API library

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/camara.svg?label=pypi%20(stable))](https://pypi.org/project/camara/)

The Camara Python library provides convenient access to the Camara REST API from any Python 3.9+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is generated with [Stainless](https://www.stainless.com/).

## MCP Server

Use the Camara MCP Server to enable AI assistants to interact with this API, allowing them to explore endpoints, make test requests, and use documentation to help integrate this SDK into your application.

[![Add to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=camara-sdk-mcp&config=eyJjb21tYW5kIjoibnB4IiwiYXJncyI6WyIteSIsImNhbWFyYS1zZGstbWNwIl0sImVudiI6eyJDQU1BUkFfQkVBUkVSX1RPS0VOIjoiTXkgQ29ubmVjdGVkIE5ldHdvcmsgVHlwZSBUb2tlbiIsIkNBTUFSQV9ERVZJQ0VfTE9DQVRJT05fTk9USUZJQ0FUSU9OU19BUElfS0VZIjoiTXkgRGV2aWNlIExvY2F0aW9uIE5vdGlmaWNhdGlvbnMgQVBJIEtleSIsIkNBTUFSQV9OT1RJRklDQVRJT05TX0FQSV9LRVkiOiJNeSBOb3RpZmljYXRpb25zIEFQSSBLZXkiLCJDQU1BUkFfUE9QVUxBVElPTl9ERU5TSVRZX0RBVEFfTk9USUZJQ0FUSU9OU19BUElfS0VZIjoiTXkgUG9wdWxhdGlvbiBEZW5zaXR5IERhdGEgTm90aWZpY2F0aW9ucyBBUEkgS2V5IiwiQ0FNQVJBX1JFR0lPTl9ERVZJQ0VfQ09VTlRfTk9USUZJQ0FUSU9OU19BUElfS0VZIjoiTXkgUmVnaW9uIERldmljZSBDb3VudCBOb3RpZmljYXRpb25zIEFQSSBLZXkiLCJDQU1BUkFfQ09OTkVDVElWSVRZX0lOU0lHSFRTX05PVElGSUNBVElPTlNfQVBJX0tFWSI6Ik15IENvbm5lY3Rpdml0eSBJbnNpZ2h0cyBOb3RpZmljYXRpb25zIEFQSSBLZXkiLCJDQU1BUkFfU0lNX1NXQVBfTk9USUZJQ0FUSU9OU19BUElfS0VZIjoiTXkgU2ltIFN3YXAgTm90aWZpY2F0aW9ucyBBUEkgS2V5IiwiQ0FNQVJBX0RFVklDRV9ST0FNSU5HX1NUQVRVU19OT1RJRklDQVRJT05TX0FQSV9LRVkiOiJNeSBEZXZpY2UgUm9hbWluZyBTdGF0dXMgTm90aWZpY2F0aW9ucyBBUEkgS2V5IiwiQ0FNQVJBX0RFVklDRV9SRUFDSEFCSUxJVFlfU1RBVFVTX05PVElGSUNBVElPTlNfQVBJX0tFWSI6Ik15IERldmljZSBSZWFjaGFiaWxpdHkgU3RhdHVzIE5vdGlmaWNhdGlvbnMgQVBJIEtleSIsIkNBTUFSQV9DT05ORUNURURfTkVUV09SS19UWVBFX05PVElGSUNBVElPTlNfQVBJX0tFWSI6Ik15IENvbm5lY3RlZCBOZXR3b3JrIFR5cGUgTm90aWZpY2F0aW9ucyBBUEkgS2V5In19)
[![Install in VS Code](https://img.shields.io/badge/_-Add_to_VS_Code-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCA0MCA0MCI+PHBhdGggZmlsbD0iI0VFRSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMzAuMjM1IDM5Ljg4NGEyLjQ5MSAyLjQ5MSAwIDAgMS0xLjc4MS0uNzNMMTIuNyAyNC43OGwtMy40NiAyLjYyNC0zLjQwNiAyLjU4MmExLjY2NSAxLjY2NSAwIDAgMS0xLjA4Mi4zMzggMS42NjQgMS42NjQgMCAwIDEtMS4wNDYtLjQzMWwtMi4yLTJhMS42NjYgMS42NjYgMCAwIDEgMC0yLjQ2M0w3LjQ1OCAyMCA0LjY3IDE3LjQ1MyAxLjUwNyAxNC41N2ExLjY2NSAxLjY2NSAwIDAgMSAwLTIuNDYzbDIuMi0yYTEuNjY1IDEuNjY1IDAgMCAxIDIuMTMtLjA5N2w2Ljg2MyA1LjIwOUwyOC40NTIuODQ0YTIuNDg4IDIuNDg4IDAgMCAxIDEuODQxLS43MjljLjM1MS4wMDkuNjk5LjA5MSAxLjAxOS4yNDVsOC4yMzYgMy45NjFhMi41IDIuNSAwIDAgMSAxLjQxNSAyLjI1M3YuMDk5LS4wNDVWMzMuMzd2LS4wNDUuMDk1YTIuNTAxIDIuNTAxIDAgMCAxLTEuNDE2IDIuMjU3bC04LjIzNSAzLjk2MWEyLjQ5MiAyLjQ5MiAwIDAgMS0xLjA3Ny4yNDZabS43MTYtMjguOTQ3LTExLjk0OCA5LjA2MiAxMS45NTIgOS4wNjUtLjAwNC0xOC4xMjdaIi8+PC9zdmc+)](https://vscode.stainless.com/mcp/%7B%22name%22%3A%22camara-sdk-mcp%22%2C%22command%22%3A%22npx%22%2C%22args%22%3A%5B%22-y%22%2C%22camara-sdk-mcp%22%5D%2C%22env%22%3A%7B%22CAMARA_BEARER_TOKEN%22%3A%22My%20Connected%20Network%20Type%20Token%22%2C%22CAMARA_DEVICE_LOCATION_NOTIFICATIONS_API_KEY%22%3A%22My%20Device%20Location%20Notifications%20API%20Key%22%2C%22CAMARA_NOTIFICATIONS_API_KEY%22%3A%22My%20Notifications%20API%20Key%22%2C%22CAMARA_POPULATION_DENSITY_DATA_NOTIFICATIONS_API_KEY%22%3A%22My%20Population%20Density%20Data%20Notifications%20API%20Key%22%2C%22CAMARA_REGION_DEVICE_COUNT_NOTIFICATIONS_API_KEY%22%3A%22My%20Region%20Device%20Count%20Notifications%20API%20Key%22%2C%22CAMARA_CONNECTIVITY_INSIGHTS_NOTIFICATIONS_API_KEY%22%3A%22My%20Connectivity%20Insights%20Notifications%20API%20Key%22%2C%22CAMARA_SIM_SWAP_NOTIFICATIONS_API_KEY%22%3A%22My%20Sim%20Swap%20Notifications%20API%20Key%22%2C%22CAMARA_DEVICE_ROAMING_STATUS_NOTIFICATIONS_API_KEY%22%3A%22My%20Device%20Roaming%20Status%20Notifications%20API%20Key%22%2C%22CAMARA_DEVICE_REACHABILITY_STATUS_NOTIFICATIONS_API_KEY%22%3A%22My%20Device%20Reachability%20Status%20Notifications%20API%20Key%22%2C%22CAMARA_CONNECTED_NETWORK_TYPE_NOTIFICATIONS_API_KEY%22%3A%22My%20Connected%20Network%20Type%20Notifications%20API%20Key%22%7D%7D)

> Note: You may need to set environment variables in your MCP client.

## Documentation

The full API of this library can be found in [api.md](api.md).

## Installation

```sh
# install from this staging repo
pip install git+ssh://git@github.com/stainless-sdks/camara-python.git
```

> [!NOTE]
> Once this package is [published to PyPI](https://www.stainless.com/docs/guides/publish), this will become: `pip install camara`

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from camara import Camara

client = Camara(
    bearer_token=os.environ.get("CAMARA_BEARER_TOKEN"),  # This is the default and can be omitted
)

scoring = client.customerinsights.scoring.retrieve()
print(scoring.scoring_type)
```

While you can provide a `customer_insights_token` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `CAMARA_BEARER_TOKEN="My Customer Insights Token"` to your `.env` file
so that your Customer Insights Token is not stored in source control.

## Async usage

Simply import `AsyncCamara` instead of `Camara` and use `await` with each API call:

```python
import os
import asyncio
from camara import AsyncCamara

client = AsyncCamara(
    bearer_token=os.environ.get("CAMARA_BEARER_TOKEN"),  # This is the default and can be omitted
)


async def main() -> None:
    scoring = await client.customerinsights.scoring.retrieve()
    print(scoring.scoring_type)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from this staging repo
pip install 'camara[aiohttp] @ git+ssh://git@github.com/stainless-sdks/camara-python.git'
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from camara import DefaultAioHttpClient
from camara import AsyncCamara


async def main() -> None:
    async with AsyncCamara(
        bearer_token=os.environ.get(
            "CAMARA_BEARER_TOKEN"
        ),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        scoring = await client.customerinsights.scoring.retrieve()
        print(scoring.scoring_type)


asyncio.run(main())
```

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from camara import Camara

client = Camara()

device_location_subscription = client.devicelocation.subscriptions.create(
    config={"subscription_detail": {"area": {"area_type": "CIRCLE"}}},
    protocol="HTTP",
    sink="https://notificationSendServer12.supertelco.com",
    types=["org.camaraproject.geofencing-subscriptions.v0.area-entered"],
    sink_credential={"credential_type": "PLAIN"},
)
print(device_location_subscription.sink_credential)
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `camara.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `camara.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `camara.APIError`.

```python
import camara
from camara import Camara

client = Camara()

try:
    client.customerinsights.scoring.retrieve()
except camara.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except camara.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except camara.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from camara import Camara

# Configure the default for all requests:
client = Camara(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).customerinsights.scoring.retrieve()
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from camara import Camara

# Configure the default for all requests:
client = Camara(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Camara(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).customerinsights.scoring.retrieve()
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `CAMARA_LOG` to `info`.

```shell
$ export CAMARA_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from camara import Camara

client = Camara()
response = client.customerinsights.scoring.with_raw_response.retrieve()
print(response.headers.get('X-My-Header'))

scoring = response.parse()  # get the object that `customerinsights.scoring.retrieve()` would have returned
print(scoring.scoring_type)
```

These methods return an [`APIResponse`](https://github.com/stainless-sdks/camara-python/tree/main/src/camara/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/stainless-sdks/camara-python/tree/main/src/camara/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.customerinsights.scoring.with_streaming_response.retrieve() as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from camara import Camara, DefaultHttpxClient

client = Camara(
    # Or use the `CAMARA_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from camara import Camara

with Camara() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/stainless-sdks/camara-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import camara
print(camara.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
