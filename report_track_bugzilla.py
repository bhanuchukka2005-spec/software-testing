
import json

# Simulated Bugzilla bug storage
bugs = {}

# Create a new bug
create_payload = {
    "product": "TestProduct",
    "component": "TestComponent",
    "summary": "Test Bug via API",
    "version": "unspecified",
    "description": "Steps to reproduce: ...",
    "op_sys": "All",
    "platform": "All"
}

# Simulate bug creation
bug_id = 12345

bugs[bug_id] = {
    "id": bug_id,
    "summary": create_payload["summary"],
    "status": "NEW",
    "product": create_payload["product"]
}

print("Bug Created:", json.dumps({"id": bug_id}))

# Track the bug
tracked_bug = bugs.get(bug_id)

if tracked_bug:
    print("Bug Details:")
    print(json.dumps({
        "bugs": [tracked_bug]
    }, indent=4))
else:
    print("Bug not found")
