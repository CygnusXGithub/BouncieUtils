# tests/test_client.py

from api.client import BouncieClient
from api.auth import get_access_token
import datetime

def test_search_trips_after_date():
    # Get access token for the first account
    access_token_1 = get_access_token(1)

    # Initialize the BouncieClient with the access token
    bouncie_client = BouncieClient(access_token_1)

    # Define the date after which to search for trips
    after_date = datetime.datetime(2023, 8, 10, 5, 0)  # August 10, 2023, 5 am
    after_date_str = after_date.isoformat() + "Z"  # Convert to ISO format with 'Z' for UTC

    # Search for trips with a specific IMEI, gps_format, and starts_after date
    trips = bouncie_client.search_trips(imei="866392060557448", gps_format="polyline", starts_after=after_date_str)

    # Print the trips
    print(trips)

    # Assert that the trips are not empty (this will depend on your data)
    assert trips, "No trips found after the specified date."

# Run the test
test_search_trips_after_date()
