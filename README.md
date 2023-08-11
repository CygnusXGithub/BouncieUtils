# Bouncie Tools: Project Structure and Overview

## Directory Structure

```
bouncie_tools/
│
├── api/
│   ├── init.py
│   ├── auth.py                # Handles authentication and token management
│   ├── endpoints.py           # Defines API endpoints and related constants
│   └── client.py              # Centralized API client to handle requests
│
├── tools/
│   ├── init.py
│   └── vehicle_checker.py     # Tool to check vehicle activity
│
├── utils/
│   ├── init.py
│   └── date_utils.py          # Helper functions for date calculations
│
├── tests/
│   ├── init.py
│   ├── test_auth.py
│   ├── test_client.py
│   └── test_vehicle_checker.py
│
├── main.py                    # Main script to run the tools
│
└── config.py                  # Configuration file for API keys, endpoints, etc.
```

## Authentication

The authentication process remains consistent. The `auth.py` module is responsible for managing the OAuth 2.0 flow.

## API Client

The `client.py` module contains methods designed to fetch details about vehicles and their respective trips. It utilizes the endpoints defined within `endpoints.py`.

## Vehicle Activity Check

The `vehicle_checker.py` tool leverages the API client to retrieve information about vehicles and their trips. Its primary function is to identify vehicles that have remained stationary for the past week.

## Main Script

`main.py` serves as the project's entry point. It employs the `vehicle_checker` tool to obtain the required output, which is then displayed on the console.

## Testing

Testing is a crucial aspect of this project. The primary focus is on evaluating the core components, which include:

- Authentication
- API client methods
- Vehicle activity checks

Ensure that all tests are comprehensive and cover potential edge cases to maintain the integrity and reliability of the tools.
