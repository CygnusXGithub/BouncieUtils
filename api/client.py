import requests
from .auth import authenticate
from config import BASE_URL

# Set up headers for API requests
HEADERS = {
    "Authorization": f"Bearer {authenticate()}",
    "Content-Type": "application/json"
}

def fetch_vehicles():
    """
    Fetch all vehicles associated with the authenticated user.
    """
    response = requests.get(f"{BASE_URL}vehicles", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        return None

def fetch_trips(vehicle_id):
    """
    Fetch trips for a specific vehicle.
    """
    response = requests.get(f"{BASE_URL}trips?vehicleId={vehicle_id}", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error
        return None
