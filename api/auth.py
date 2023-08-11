import requests
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from config import CLIENT_ID, CLIENT_SECRET

AUTH_URL = "https://auth.bouncie.com/dialog/authorize"
TOKEN_URL = "https://auth.bouncie.com/oauth/token"

class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urlparse(self.path).query
        query_components = parse_qs(query)
        authorization_code = query_components.get("code")[0]

        # Store the code in the server to use later
        self.server.authorization_code = authorization_code

        # Respond to the browser
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Authorization successful. You can close this window.")

def get_authorization_url(redirect_uri, state=None):
    """
    Generate the URL to redirect the user to for authorization.
    """
    params = {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": redirect_uri
    }
    if state:
        params["state"] = state

    return AUTH_URL + "?" + "&".join(f"{k}={v}" for k, v in params.items())

def get_authorization_code(redirect_uri):
    # Open the authorization URL in the user's browser
    webbrowser.open(get_authorization_url(redirect_uri))

    # Start a temporary server to capture the redirect
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, AuthHandler)
    httpd.handle_request()  # Handle a single request, then exit

    return httpd.authorization_code

def get_access_token(authorization_code, redirect_uri):
    """
    Exchange the authorization code for an access token.
    """
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri
    }

    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        # Handle error
        return None

def authenticate():
    redirect_uri = "http://localhost:8080/callback"
    authorization_code = get_authorization_code(redirect_uri)
    access_token = get_access_token(authorization_code, redirect_uri)
    return access_token
