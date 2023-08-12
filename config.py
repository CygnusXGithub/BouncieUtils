import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def get_account_details(account_number):
    """
    Retrieve the details of a specific account based on its number.
    
    Args:
    - account_number (int): The number of the account (e.g., 1 for the first account, 2 for the second, etc.)

    Returns:
    - dict: A dictionary containing the client_id, client_secret, and auth_code for the specified account.
    """
    client_id_key = f"BOUNCIE_CLIENT_ID_{account_number}"
    client_secret_key = f"BOUNCIE_CLIENT_SECRET_{account_number}"
    auth_code_key = f"BOUNCIE_AUTH_CODE_{account_number}"

    client_id = os.getenv(client_id_key)
    client_secret = os.getenv(client_secret_key)
    auth_code = os.getenv(auth_code_key)

    if not all([client_id, client_secret, auth_code]):
        raise ValueError(f"Details for account {account_number} not found or incomplete in .env file.")

    return {
        "client_id": client_id,
        "client_secret": client_secret,
        "auth_code": auth_code
    }

def get_all_accounts():
    """
    Retrieve the details of all accounts present in the .env file.

    Returns:
    - list: A list of dictionaries, each containing the client_id, client_secret, and auth_code for an account.
    """
    accounts = []
    account_number = 1

    while True:
        try:
            account_details = get_account_details(account_number)
            accounts.append(account_details)
            account_number += 1
        except ValueError:
            break

    return accounts
