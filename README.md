# Clockify API Client

# Simple API client for Clockify.

Simple Python API client for
Clockify. [Clockify API reference](https://clockify.me/developers-api)

- Base endpoints
    - Client
    - Custom Field
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

## 2. Example usage

```python
from clockify_api_client.client import ClockifyAPIClient

CK_API_KEY = "ZWQ5ZjQ2NDMtY2I2NS00OTQ2LTllZGEtNTkzZGMwMjgxODcy"
CK_API_DOMAIN = "developer.clockify.me"


async def main():
    api = ClockifyAPIClient().build(
        CK_API_KEY,
        f"{CK_API_DOMAIN}/api/v1",
    )
    workspaces = await api.workspaces.get_workspaces()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
```

## Developing against a local copy

If you want to make changes to this API client locally and test
[timekeeper](https://github.com/ion8/timekeeper) against those changes before committing
them:

1. Install this client once the normal way. This will ensure that the API client
   dependencies are installed in the timekeeper venv.
2. Clone https://github.com/ion8/clockify-api-client to a new project.
2. In a separate run configuration on the timekeeper project, set the environment
   variable `PYTHONPATH` to the directory with your copy of the API
   client. (This can't be set in `.env` because `.env` is loaded by `python-dotenv`
   after Python starts.)
3. Run timekeeper for development as normal. It will load `clockify-api-client` from
   PYTHONPATH, overriding the normal import from your project dependencies.
