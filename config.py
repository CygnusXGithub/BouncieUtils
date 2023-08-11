import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.bouncie.dev/v1/"
REDIRECT_URI = "http://localhost:8080/callback"

def get_client_id(account_number):
    return os.environ.get(f"BOUNCIE_CLIENT_ID_{account_number}")

def get_client_secret(account_number):
    return os.environ.get(f"BOUNCIE_CLIENT_SECRET_{account_number}")

def get_access_token(account_number):
    return os.environ.get(f"BOUNCIE_ACCESS_TOKEN_{account_number}")

def get_access_code(account_number):
    return os.environ.get(f"BOUNCIE_ACCESS_CODE_{account_number}")


