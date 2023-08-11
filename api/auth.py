import os
import requests
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from config import get_client_id, get_client_secret, REDIRECT_URI

AUTH_URL = "https://auth.bouncie.com/dialog/authorize"
TOKEN_URL = "https://auth.bouncie.com/oauth/token"

class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        query_components = parse_qs(query)
        authorization_code = query_components.get("code")
        
        if authorization_code:
            self.server.authorization_code = authorization_code[0]
        else:
            print("Authorization code not found in callback URL.")
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Authorization successful. You can close this window.")

def get_authorization_url(redirect_uri, account_number, state=None,):
    params = {
        "client_id": get_client_id(account_number),
        "response_type": "code",
        "redirect_uri": redirect_uri
    }
    if state:
        params["state"] = state

    return AUTH_URL + "?" + "&".join(f"{k}={v}" for k, v in params.items())

def get_authorization_code(redirect_uri, account_number):
    webbrowser.open(get_authorization_url(redirect_uri, account_number))
    server_address = ('', 8080)
    httpd = HTTPServer(('localhost', 8080), AuthHandler)
    while not hasattr(httpd, 'authorization_code'):
        httpd.handle_request()
    return httpd.authorization_code

def save_authorization_code(authorization_code, account_number):
    env_key = f"BOUNCIE_ACCESS_CODE_{account_number}"
    
    # Update the .env file
    with open(".env", "r") as file:
        lines = file.readlines()

    updated = False
    for index, line in enumerate(lines):
        if line.startswith(env_key):
            lines[index] = f"{env_key}={authorization_code}\n"
            updated = True
            break

    if not updated:
        lines.append(f"{env_key}={authorization_code}\n")

    with open(".env", "w") as file:
        file.writelines(lines)
    
    os.environ[env_key] = authorization_code

def load_authorization_code(account_number):
    env_key = f"BOUNCIE_ACCESS_CODE_{account_number}"
    return os.environ.get(env_key)

def get_access_token(authorization_code, redirect_uri, account_number):
    data = {
        "client_id": get_client_id(account_number),
        "client_secret": get_client_secret(account_number),
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri
    }

    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        json_response = response.json()
        access_token = json_response.get("access_token")
        expires_in = json_response.get("expires_in")
        return access_token, expires_in
    else:
        return None, None

def save_token(access_token, account_number):
    """
    Save the access token for a specific account number to the .env file.
    """
    env_key = f"BOUNCIE_ACCESS_TOKEN_{account_number}"
    
    # Read the entire .env file
    with open(".env", "r") as file:
        lines = file.readlines()

    # Modify the specific line
    updated = False
    for index, line in enumerate(lines):
        if line.startswith(env_key):
            lines[index] = f"{env_key}={access_token}\n"
            updated = True
            break

    # If the token was not found in the file, append it
    if not updated:
        lines.append(f"{env_key}={access_token}\n")

    # Write the updated content back to the .env file
    with open(".env", "w") as file:
        file.writelines(lines)
    
    # Update the environment variables in the current session
    os.environ[env_key] = access_token

def load_token(account_number):
    """
    Load the access token for a specific account number from the environment variables.
    """
    env_key = f"BOUNCIE_ACCESS_TOKEN_{account_number}"
    return os.environ.get(env_key)

def authenticate(account_number):
    access_token = load_token(account_number)
    authorization_code = load_authorization_code(account_number)

    if not authorization_code:
        print(f"Authorization code for account {account_number} not found. Initiating authentication process...")
        authorization_code = get_authorization_code(REDIRECT_URI, account_number)
        save_authorization_code(authorization_code, account_number)

    if not access_token:
        print(f"Access token for account {account_number} not found. Using authorization code to get a new token...")
        access_token, expires_in = get_access_token(authorization_code, REDIRECT_URI, account_number)
        if access_token:
            print(f"Access token for account {account_number} retrieved successfully.")
            print(f"Token lifetime: {expires_in} seconds.")
            save_token(access_token, account_number)
        else:
            print(f"Failed to retrieve access token for account {account_number}.")
            return None
    else:
        print(f"Access token for account {account_number} loaded from environment variables.")
    return access_token

def get_all_tokens():
    tokens = {}
    for account_number in range(1, 13):  # Assuming up to 12 accounts
        tokens[account_number] = authenticate(account_number)
    return tokens
