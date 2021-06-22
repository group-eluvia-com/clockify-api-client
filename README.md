# Clockify API Client

# Simple API client for Clockify.
Simple Python API client for Clockify. [Clockify API reference](https://clockify.me/developers-api)

- Base endpoints
  - Client
  - Project
  - Task  
  - Time Entry
  - User
  - Workspace
- Reports Endpoints
  - Reports
  - Shared reports


## 1. Installation

Add package to your project:

```
pipenv install clockify-api-client
```

## 2. Usage


```python
from clockify_api_client.client import ClockifyAPIClient

API_KEY = 'yourclockifyAPIkey'
API_URL = 'api.clockify.me/v1'

client = ClockifyAPIClient().build(API_KEY, API_URL)

workspaces = client.workspaces.get_workspaces()  # Returns list of workspaces.

```
