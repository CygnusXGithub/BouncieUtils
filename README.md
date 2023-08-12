# Bouncie Tools: Project Structure and Overview

## Directory Structure

```
bouncie_tools/
│
├── api/
│   ├── auth.py                # Handles authentication and token management
│   ├── endpoints.py           # Defines API endpoints and related constants
│   └── client.py              # Centralized API client to handle requests
│
├── tools/
│   └── vehicle_checker.py     # Tool to check vehicle activity
│
├── utils/
│   └── date_utils.py          # Helper functions for date calculations
│
├── tests/
│   ├── test_auth.py           # Tests for authentication module
│   ├── test_client.py         # Tests for API client module
│   └── test_vehicle_checker.py# Tests for vehicle checker tool
│
├── main.py                    # Main script to run the tools
│
└── config.py                  # Configuration file for API keys, endpoints, etc.
```

## Modules Overview

### Authentication (`auth.py`)
This module is responsible for managing the OAuth 2.0 flow. It provides functions to authenticate with the Bouncie API and retrieve access tokens.

### API Client (`client.py`)
The `client.py` module contains methods designed to fetch details about vehicles and their respective trips. It utilizes the endpoints defined within `endpoints.py`.

#### Usage:
- `search_vehicles(vin=None, imei=None, limit=None, skip=None)`: Search for vehicles based on specific criteria.
- `search_trips(imei, gps_format, transaction_id=None, starts_after=None, ends_before=None)`: Search for trips based on specific criteria.

### Vehicle Activity Check (`vehicle_checker.py`)
The `vehicle_checker.py` tool leverages the API client to retrieve information about vehicles and their trips. Its primary function is to identify vehicles that have remained stationary for the past week.

### Main Script (`main.py`)
`main.py` serves as the project's entry point. It employs the `vehicle_checker` tool to obtain the required output, which is then displayed on the console.

### Utilities (`date_utils.py`)
This module provides helper functions for date calculations, which can be used across different parts of the project.

## Configuration

The project uses a `.env` file to store configuration parameters. This file is not included in the repository for security reasons. Its structure is as follows:

```
#  Account 1
ACCOUNT_NAME_1=1
BOUNCIE_CLIENT_ID_1=bouncieutils1
BOUNCIE_CLIENT_SECRET_1=
BOUNCIE_AUTH_CODE_1=

# Account 2
ACCOUNT_NAME_2=2
BOUNCIE_CLIENT_ID_2=bouncieutils2
BOUNCIE_CLIENT_SECRET_2=
BOUNCIE_AUTH_CODE_2=
```

## Building and Running Tools

1. Ensure you have the required dependencies installed.
2. Set up your `.env` file with the necessary parameters as shown in the Configuration section.
3. Update the `config.py` file to read values from the `.env` file.
4. Run the `main.py` script to execute the tools and view the output.

## Testing

The `tests` directory contains unit tests for the following:
- Authentication
- API client methods
- Vehicle activity checks

To run tests, navigate to the `tests` directory and execute the desired test script.