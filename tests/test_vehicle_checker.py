# inactivity_checker.py

from api.client import BouncieClient
from api.auth import get_access_token
from config import get_total_accounts, get_account_details
import datetime

def check_vehicle_inactivity(account_number, account_name, threshold_hours=48):
    """
    Check if any vehicles in the specified account have been inactive for more than the threshold hours.

    Args:
    - account_number (int): The number of the account to check.
    - threshold_hours (int, optional): The inactivity threshold in hours. Default is 48 hours.

    Returns:
    - list: A list of vehicle names that have been inactive for more than the threshold hours.
    """
    # Get access token for the specified account
    access_token = get_access_token(account_number)

    # Initialize the BouncieClient with the access token
    bouncie_client = BouncieClient(access_token)

    # Retrieve the list of vehicles
    vehicles = bouncie_client.search_vehicles()

    # List to store names of inactive vehicles
    inactive_vehicles = []

    for vehicle in vehicles:
        imei = vehicle.get("imei")
        # Retrieve the trips for the vehicle
        trips = bouncie_client.search_trips(imei=imei, gps_format="polyline")
        # If there are no trips, consider the vehicle as inactive
        if not trips:
            inactive_vehicles.append(f"{account_name} - {vehicle.get('nickName', 'Unknown Vehicle')}")
            continue

        # Get the endTime of the most recent trip
        last_trip_end_time = trips[0].get("endTime")
        if last_trip_end_time:
            last_trip_end_time = datetime.datetime.fromisoformat(last_trip_end_time.replace("Z", "+00:00"))
            current_time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
            time_difference = current_time - last_trip_end_time

            # Check if the time difference exceeds the threshold
            if time_difference.total_seconds() > threshold_hours * 3600:
                inactive_vehicles.append(f"{account_name} - {vehicle.get('nickName', 'Unknown Vehicle')}")

    return inactive_vehicles

def main():
    total_accounts = get_total_accounts()
    all_inactive_vehicles = []

    for account_number in range(1, total_accounts + 1):
        account_details = get_account_details(account_number)
        inactive_vehicles = check_vehicle_inactivity(account_number, account_details["account_name"])
        all_inactive_vehicles.extend(inactive_vehicles)


    if all_inactive_vehicles:
        print("Vehicles inactive for more than 48 hours:")
        for vehicle_name in all_inactive_vehicles:
            print(vehicle_name)
    else:
        print("All vehicles have been active in the last 48 hours.")

if __name__ == "__main__":
    main()

