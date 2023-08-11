import os
from dotenv import load_dotenv

load_dotenv()

# Configuration for Bouncie API
BASE_URL = "https://api.bouncie.dev/v1/"
CLIENT_ID = os.environ.get("BOUNCIE_CLIENT_ID")
CLIENT_SECRET = os.environ.get("BOUNCIE_CLIENT_SECRET")

