
import json

# Simulated MantisBT issue storage
issues = {}

# Create a new issue
create_payload = {
    "summary": "Bug via API",
    "description": "Steps to reproduce...",
    "project": {"name": "TestProject"},
    "category": {"name": "General"}
}

# Simulate issue creation
issue_id = 101

issues[issue_id] = {
    "id": issue_id,
    "summary": create_payload["summary"],
    "description": create_payload["description"],
    "status": {"name": "new"},
    "project": create_payload["project"]
}

print("Bug Created:", json.dumps({
    "issue": {"id": issue_id}
}))

# Track the issue
tracked_issue = issues.get(issue_id)

if tracked_issue:
    print("\nBug Details:")
    print(json.dumps({
        "issue": tracked_issue
    }, indent=4))
else:
    print("Issue not found")
