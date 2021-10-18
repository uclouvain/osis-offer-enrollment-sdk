# osis_offer_enrollment_sdk.EnrollmentApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/offer_enrollment*

Method | HTTP request | Description
------------- | ------------- | -------------
[**my_enrollments_list**](EnrollmentApi.md#my_enrollments_list) | **GET** /my_enrollments/ | 
[**my_enrollments_year_list**](EnrollmentApi.md#my_enrollments_year_list) | **GET** /my_enrollments/{year} | 


# **my_enrollments_list**
> EnrollmentList my_enrollments_list()



Return all enrollments of the connected user

### Example

* Api Key Authentication (Token):
```python
import time
import osis_offer_enrollment_sdk
from osis_offer_enrollment_sdk.api import enrollment_api
from osis_offer_enrollment_sdk.model.enrollment_list import EnrollmentList
from osis_offer_enrollment_sdk.model.error import Error
from osis_offer_enrollment_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/offer_enrollment
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_offer_enrollment_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/offer_enrollment"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_offer_enrollment_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enrollment_api.EnrollmentApi(api_client)
    enrollment_state = [
        "enrollment_state_example",
    ] # [str] |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    limit = 25 # int | Limit of paginated results (optional)
    offset = 25 # int | Offset of paginated results (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.my_enrollments_list(enrollment_state=enrollment_state, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_offer_enrollment_sdk.ApiException as e:
        print("Exception when calling EnrollmentApi->my_enrollments_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enrollment_state** | **[str]**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **limit** | **int**| Limit of paginated results | [optional]
 **offset** | **int**| Offset of paginated results | [optional]

### Return type

[**EnrollmentList**](EnrollmentList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_enrollments_year_list**
> EnrollmentList my_enrollments_year_list(year)



Return all enrollments of the connected user for a specific year

### Example

* Api Key Authentication (Token):
```python
import time
import osis_offer_enrollment_sdk
from osis_offer_enrollment_sdk.api import enrollment_api
from osis_offer_enrollment_sdk.model.enrollment_list import EnrollmentList
from osis_offer_enrollment_sdk.model.error import Error
from osis_offer_enrollment_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/offer_enrollment
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_offer_enrollment_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/offer_enrollment"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_offer_enrollment_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = enrollment_api.EnrollmentApi(api_client)
    year = 1 # int | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)
    limit = 25 # int | Limit of paginated results (optional)
    offset = 25 # int | Offset of paginated results (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.my_enrollments_year_list(year)
        pprint(api_response)
    except osis_offer_enrollment_sdk.ApiException as e:
        print("Exception when calling EnrollmentApi->my_enrollments_year_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.my_enrollments_year_list(year, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id, limit=limit, offset=offset)
        pprint(api_response)
    except osis_offer_enrollment_sdk.ApiException as e:
        print("Exception when calling EnrollmentApi->my_enrollments_year_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]
 **limit** | **int**| Limit of paginated results | [optional]
 **offset** | **int**| Offset of paginated results | [optional]

### Return type

[**EnrollmentList**](EnrollmentList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

