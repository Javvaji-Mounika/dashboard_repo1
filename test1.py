import requests
import os

# --- Configuration ---
token = os.getenv("GITHUB_TOKEN")
repo_owner = "Javvaji-Mounika"
repo_name = "dashboard_repo1"
discussion_number = 1   # your discussion ID

# --- API Endpoint ---
url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/discussions/{discussion_number}"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# --- New dashboard content ---
new_body = """
## 🚀 Project Dashboard
- Status:  Completed
- Last Updated: 2025-10-27
"""

# --- Update the discussion ---
data = {"body": new_body}

response = requests.patch(url, headers=headers, json=data)

if response.status_code == 200:
    print(" Dashboard updated successfully!")
else:
    print(" Failed to update dashboard:", response.status_code, response.text)
