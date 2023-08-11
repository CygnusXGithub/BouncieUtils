from api.auth import authenticate

def test_authentication():
    for account_number in [1, 2]:
        print(f"Authenticating for Account {account_number}...")
        token = authenticate(account_number)
        if token:
            print(f"Access Token for Account {account_number}: {token}")
        else:
            print(f"Authentication failed for Account {account_number}.")

if __name__ == "__main__":
    test_authentication()
