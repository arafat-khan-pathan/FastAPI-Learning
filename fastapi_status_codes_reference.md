# FastAPI HTTP Status Codes Reference

In FastAPI, you can import and use readable HTTP status code constants directly from `fastapi.status` (e.g., `status.HTTP_200_OK`). Below is a complete list of standard HTTP status codes grouped by category.

---

## 1xx — Informational Responses

| Code | FastAPI Constant | Meaning |
| :--- | :--- | :--- |
| **100** | `HTTP_100_CONTINUE` | Server received request headers; client should proceed to send the body. |
| **101** | `HTTP_101_SWITCHING_PROTOCOLS` | Server is switching protocols as requested by the client (e.g., to WebSockets). |
| **102** | `HTTP_102_PROCESSING` | Server has received and is processing the request, but no response is available yet. |
| **103** | `HTTP_103_EARLY_HINTS` | Used to return some response headers before the final HTTP message. |

---

## 2xx — Success Responses

| Code | FastAPI Constant | Meaning |
| :--- | :--- | :--- |
| **200** | `HTTP_200_OK` | Standard response for successful HTTP requests. |
| **201** | `HTTP_201_CREATED` | Request succeeded and a new resource was created (commonly used for `POST`). |
| **202** | `HTTP_202_ACCEPTED` | Request has been accepted for processing, but processing is not yet complete. |
| **203** | `HTTP_203_NON_AUTHORITATIVE_INFORMATION` | Request succeeded, but returned metadata may be from a third-party copy. |
| **204** | `HTTP_204_NO_CONTENT` | Request succeeded, and there is no content to send back (commonly used for `DELETE`). |
| **205** | `HTTP_205_RESET_CONTENT` | Request succeeded; client should reset the document view (e.g., clear a form). |
| **206** | `HTTP_206_PARTIAL_CONTENT` | Server is delivering only part of the resource due to a range header sent by the client. |
| **207** | `HTTP_207_MULTI_STATUS` | Conveys information about multiple resources (WebDAV). |
| **208** | `HTTP_208_ALREADY_REPORTED` | Used inside a DAV response element to avoid enumerating internal members repeatedly. |
| **226** | `HTTP_226_IM_USED` | Server has fulfilled a `GET` request for the resource with instance-manipulations applied. |

---

## 3xx — Redirection Messages

| Code | FastAPI Constant | Meaning |
| :--- | :--- | :--- |
| **300** | `HTTP_300_MULTIPLE_CHOICES` | Request has more than one possible response; user/agent should choose one. |
| **301** | `HTTP_301_MOVED_PERMANENTLY` | URL of the requested resource has been changed permanently. |
| **302** | `HTTP_302_FOUND` | URI of requested resource has been changed temporarily. |
| **303** | `HTTP_303_SEE_OTHER` | Server directs client to get the requested resource at another URI with a `GET` request. |
| **304** | `HTTP_304_NOT_MODIFIED` | Resource has not been modified since the version specified by request headers (caching). |
| **305** | `HTTP_305_USE_PROXY` | Requested resource is available only through a proxy (deprecated). |
| **307** | `HTTP_307_TEMPORARY_REDIRECT` | Temporary redirect where the HTTP method (e.g., `POST`) must not change. |
| **308** | `HTTP_308_PERMANENT_REDIRECT` | Permanent redirect where the HTTP method must not change. |

---

## 4xx — Client Error Responses

| Code | FastAPI Constant | Meaning |
| :--- | :--- | :--- |
| **400** | `HTTP_400_BAD_REQUEST` | Server cannot process the request due to malformed syntax or invalid client input. |
| **401** | `HTTP_401_UNAUTHORIZED` | Authentication is required and has failed or has not yet been provided. |
| **402** | `HTTP_402_PAYMENT_REQUIRED` | Reserved for future use (sometimes used for digital payment systems). |
| **403** | `HTTP_403_FORBIDDEN` | Client is authenticated, but does not have permission to access the resource. |
| **404** | `HTTP_404_NOT_FOUND` | Server cannot find the requested resource or endpoint. |
| **405** | `HTTP_405_METHOD_NOT_ALLOWED` | HTTP method used (e.g., `POST` instead of `GET`) is not allowed for this route. |
| **406** | `HTTP_406_NOT_ACCEPTABLE` | Server cannot produce a response matching the list of acceptable values in headers. |
| **407** | `HTTP_407_PROXY_AUTHENTICATION_REQUIRED` | Client must first authenticate itself with the proxy. |
| **408** | `HTTP_408_REQUEST_TIMEOUT` | Server timed out waiting for the request. |
| **409** | `HTTP_409_CONFLICT` | Request conflicts with the current state of the server (e.g., duplicate email/username). |
| **410** | `HTTP_410_GONE` | Requested resource is no longer available and will not be available again. |
| **411** | `HTTP_411_LENGTH_REQUIRED` | Server rejected the request because the `Content-Length` header is not defined. |
| **412** | `HTTP_412_PRECONDITION_FAILED` | Server does not meet one of the preconditions specified in the request headers. |
| **413** | `HTTP_413_REQUEST_ENTITY_TOO_LARGE` | Request payload is larger than the server is willing or able to process. |
| **414** | `HTTP_414_REQUEST_URI_TOO_LONG` | URI requested by the client is longer than the server is willing to interpret. |
| **415** | `HTTP_415_UNSUPPORTED_MEDIA_TYPE` | Media format of the requested data is not supported by the server (e.g., wrong `Content-Type`). |
| **416** | `HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE` | Range specified by the `Range` header field in the request cannot be fulfilled. |
| **417** | `HTTP_417_EXPECTATION_FAILED` | Expectation indicated by the `Expect` request header field cannot be met. |
| **418** | `HTTP_418_IM_A_TEAPOT` | Server refuses the attempt to brew coffee with a teapot (April Fools' RFC joke). |
| **421** | `HTTP_421_MISDIRECTED_REQUEST` | Request was directed at a server that is not able to produce a response. |
| **422** | `HTTP_422_UNPROCESSABLE_ENTITY` | Validation error: request syntax is valid, but data fails Pydantic/schema validation. |
| **423** | `HTTP_423_LOCKED` | Resource that is being accessed is locked (WebDAV). |
| **424** | `HTTP_424_FAILED_DEPENDENCY` | Request failed due to failure of a previous request (WebDAV). |
| **425** | `HTTP_425_TOO_EARLY` | Server is unwilling to risk processing a request that might be replayed. |
| **426** | `HTTP_426_UPGRADE_REQUIRED` | Server refuses to perform the request using the current protocol; client must upgrade. |
| **428** | `HTTP_428_PRECONDITION_REQUIRED` | Origin server requires the request to be conditional. |
| **429** | `HTTP_429_TOO_MANY_REQUESTS` | User has sent too many requests in a given amount of time (rate limiting). |
| **431** | `HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE` | Server is unwilling to process the request because its header fields are too large. |
| **451** | `HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS` | Resource cannot legally be provided (e.g., censored by government). |

---

## 5xx — Server Error Responses

| Code | FastAPI Constant | Meaning |
| :--- | :--- | :--- |
| **500** | `HTTP_500_INTERNAL_SERVER_ERROR` | Generic error message when an unexpected condition/exception occurred on the server. |
| **501** | `HTTP_501_NOT_IMPLEMENTED` | Server either does not recognize the request method or lacks the ability to fulfill it. |
| **502** | `HTTP_502_BAD_GATEWAY` | Server, while acting as a gateway or proxy, received an invalid response from upstream. |
| **503** | `HTTP_503_SERVICE_UNAVAILABLE` | Server is not ready to handle the request (e.g., down for maintenance or overloaded). |
| **504** | `HTTP_504_GATEWAY_TIMEOUT` | Server, while acting as a gateway or proxy, did not get a response in time from upstream. |
| **505** | `HTTP_505_HTTP_VERSION_NOT_SUPPORTED` | HTTP version used in the request is not supported by the server. |
| **506** | `HTTP_506_VARIANT_ALSO_NEGOTIATES` | Server has an internal configuration error regarding content negotiation. |
| **507** | `HTTP_507_INSUFFICIENT_STORAGE` | Server is unable to store the representation needed to complete the request (WebDAV). |
| **508** | `HTTP_508_LOOP_DETECTED` | Server detected an infinite loop while processing the request (WebDAV). |
| **510** | `HTTP_510_NOT_EXTENDED` | Further extensions to the request are required for the server to fulfill it. |
| **511** | `HTTP_511_NETWORK_AUTHENTICATION_REQUIRED` | Client needs to authenticate to gain network access (e.g., captive Wi-Fi portals). |

---

## Quick Usage Example in FastAPI

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.post("/items/", status_code=status.HTTP_201_CREATED)
def create_item(name: str):
    if not name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Item name cannot be empty"
        )
    return {"name": name}
```