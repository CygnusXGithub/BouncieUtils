# tests/test_auth.py

from api.auth import authenticate

def test_authentication():
    token = authenticate()
    if token:
        print(f"Access Token: {token}")
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    test_authentication()
