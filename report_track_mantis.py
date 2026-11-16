
import requests
import json

# Configuration
MANTIS_URL = "https://your-mantis-url.com/api/rest"
API_TOKEN = "your_api_token"

headers = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

# Create a new issue
create_payload = {
    "summary": "Bug via API",
    "description": "Steps to reproduce...",
    "project": {"name": "TestProject"},
    "category": {"name": "General"}
}

# MOCK MODE: No real server credentials available
MOCK_MODE = True

if MOCK_MODE:

    # Simulate POST response
    create_response = {
        "issue": {"id": 101}
    }

    print("Bug Created:", json.dumps(create_response))

    # Track the issue
    issue_id = create_response["issue"]["id"]

    # Simulate GET response
    track_response = {
        "issue": {
            "id": issue_id,
            "summary": "Bug via API",
            "status": {"name": "new"},
            "project": {"name": "TestProject"}
        }
    }

    print("Bug Details:", json.dumps(track_response, indent=2))

else:

    # Actual API request to create issue
    create_response = requests.post(
        f"{MANTIS_URL}/issues/",
        headers=headers,
        json=create_payload
    )

    print("Bug Created:", create_response.json())

    # Track the issue
    issue_id = create_response.json()["issue"]["id"]

    track_response = requests.get(
        f"{MANTIS_URL}/issues/{issue_id}",
        headers=headers
    )

    print("Bug Details:", track_response.json())
