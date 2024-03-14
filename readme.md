# Azure Swagger File Fix

Azure API Management current does not support swagger files that use 'x-ms-parameterized-host' and the swagger will be imported incorrectly.  The pupose of this repo is to provide a simple script that will update the swagger file.

For this sample, we are using the Azure AI Search swagger file.  The original swagger file can be found [here](https://raw.githubusercontent.com/Azure/azure-rest-api-specs/master/specification/search/data-plane/Azure.Search/stable/2023-11-01/searchindex.json).

You should update the python code if you are experiencing issues with a different Azure service.

## Usage

1. Clone the repo locally.
1. Install the latest version of Python.
1. Download the swagger file you want to fix.
1. Update the python code, searching for 'TODO'.
1. Run the python code `python fix_swagger.py`.
1. The updated swagger file will be saved as '<inputfile>-updated.json'.
1. Get the URL suffix from the 'hostTemplate' parameter in the original swagger file.  In the case of AI Search, the URL suffix is 'indexes'
1. In Azure API Management, select Add API -> OpenAPI -> Select File and select your updated swagger file.
1. For Web service URL, enter the URL for the Azure service endpoint.  For AI Search, the URL is 'https://<service-name>.search.windows.net/' and add the url suffix you pulled from the original swagger file.  For AI Search, suffix is 'indexes' 'https://<service-name>.search.windows.net/indexes'.
1. For API URL suffic, enter the url suffix you pulled from the original swagger file.  For AI Search, suffix is 'indexes'.
    - Note: In the case of Azure AI Search, the DotNet client sdk is hardcoded to use the 'indexes' suffix.  If you use a different suffix, you will need to update the client sdk to use the correct suffix.
1. Click 'Create'.
1. Navigate to the 'Settings' tab of the new API and under 'Subscription' change 'Header name' from 'Ocp-Apim-Subscription-Key' to 'api-key'.
1. Navigate to the 'Design' tab and select 'All operations' end the 'Add policy' button under 'Inbound processing'.
1. Select 'Set headers' policy.
1. For 'name' enter 'api-key'.  For 'value' enter the subscription key for the Azure service.  For 'action' select 'append'.
1. Select 'Save'.