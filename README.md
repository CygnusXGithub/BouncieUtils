# BouncieUtils

bouncie_tools/
│
├── api/
│   ├── __init__.py
│   ├── auth.py          # Handles authentication and token management
│   ├── endpoints.py     # Defines API endpoints and related constants
│   └── client.py        # Centralized API client to handle requests
│
├── tools/
│   ├── __init__.py
│   └── vehicle_checker.py  # Tool to check vehicle activity
│
├── utils/
│   ├── __init__.py
│   └── date_utils.py       # Helper functions for date calculations
│
├── tests/
│   ├── __init__.py
│   ├── test_auth.py
│   ├── test_client.py
│   └── test_vehicle_checker.py
│
├── main.py              # Main script to run the tools
└── config.py            # Configuration file for API keys, endpoints, etc.

Authentication:

The authentication process remains the same. The auth.py will handle the OAuth 2.0 flow.
API Client:

The client.py will have methods to fetch vehicles and their trips. It will use the endpoints defined in endpoints.py.
Vehicle Activity Check:

The vehicle_checker.py tool will use the API client to fetch vehicles and their trips. It will then determine which vehicles haven't moved in the past week.
Main Script:

The main.py will be the entry point. It will use the vehicle_checker tool to get the desired output and print it to the console.
Testing:

Focus on testing the core components: authentication, API client methods, and vehicle activity check.
