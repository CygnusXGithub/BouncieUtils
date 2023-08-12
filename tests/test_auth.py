from api.auth import get_access_token

# Get access token for the first account
access_token_1 = get_access_token(1)
print(access_token_1)

# Get access token for the second account
access_token_2 = get_access_token(2)
print(access_token_2)