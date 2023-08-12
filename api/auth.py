import requests
from config import get_account_details

# Constants
TOKEN_URL = "https://auth.bouncie.com/oauth/token"
REDIRECT_URI = "http://localhost:8080/callback"  # Replace with your redirect_uri if different

def get_access_token(account_number):
    """
    Retrieve the access token for a specific account based on its number.
    
    Args:
    - account_number (int): The number of the account (e.g., 1 for the first account, 2 for the second, etc.)

    Returns:
    - str: The access token for the specified account or None if the request fails.
    """
    account_details = get_account_details(account_number)
    
    data = {
        "client_id": account_details["client_id"],
        "client_secret": account_details["client_secret"],
        "grant_type": "authorization_code",
        "code": account_details["auth_code"],
        "redirect_uri": REDIRECT_URI
    }
    
    response = requests.post(TOKEN_URL, data=data)
    
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        print(f"Failed to get access token for account {account_number}. HTTP Status Code: {response.status_code}")
        return None
