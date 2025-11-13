import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("APOLLO_API_KEY")

# Apollo People Search API endpoint
url = "https://api.apollo.io/v1/people/search"

# ✅ Headers must include the API key
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": API_KEY
}

# Example: search HR contacts at Infosys
payload = {
    "q_organization_domains": ["infosys.com"],   # Company domain
    "person_titles": ["HR", "Recruiter", "Talent Acquisition"]
}

# Make request with headers
response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)

data = response.json()
print("Raw Response:", data)   # Debug output

# Print results nicely
print("\n🔎 Top HR Contacts Found:\n")
for person in data.get("people", [])[:5]:
    print(
        f"{person.get('first_name')} {person.get('last_name')} | "
        f"{person.get('title')} | "
        f"{person.get('email')}"
    )
