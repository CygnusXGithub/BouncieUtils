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
    - dict: A dictionary containing the account_name, client_id, client_secret, and auth_code for the specified account.
    """
    account_name_key = f"ACCOUNT_NAME_{account_number}"
    client_id_key = f"BOUNCIE_CLIENT_ID_{account_number}"
    client_secret_key = f"BOUNCIE_CLIENT_SECRET_{account_number}"
    auth_code_key = f"BOUNCIE_AUTH_CODE_{account_number}"

    account_name = os.getenv(account_name_key)
    client_id = os.getenv(client_id_key)
    client_secret = os.getenv(client_secret_key)
    auth_code = os.getenv(auth_code_key)

    if not all([account_name, client_id, client_secret, auth_code]):
        raise ValueError(f"Details for account {account_number} not found or incomplete in .env file.")

    return {
        "account_name" : account_name,
        "client_id": client_id,
        "client_secret": client_secret,
        "auth_code": auth_code
    }

def get_total_accounts():
    """
    Retrieve the total number of accounts present in the .env file based on the presence of BOUNCIE_CLIENT_ID_X keys.

    Returns:
    - int: The total number of accounts.
    """
    account_number = 1
    while True:
        client_id_key = f"BOUNCIE_CLIENT_ID_{account_number}"
        if os.getenv(client_id_key):
            account_number += 1
        else:
            break
    return account_number - 1

#
