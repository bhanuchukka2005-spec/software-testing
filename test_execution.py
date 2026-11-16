
def login(username, password):

    # Simulating login logic
    if username == "admin" and password == "admin123":
        return "Login Successful"
    else:
        return "Login Failed"


# Sample test cases
test_cases = [
    {
        "id": 1,
        "username": "admin",
        "password": "admin123",
        "expected": "Login Successful"
    },
    {
        "id": 2,
        "username": "admin",
        "password": "wrongpass",
        "expected": "Login Successful"
    }  # Intentional fail
]


# Execute test cases
for test in test_cases:

    actual = login(test["username"], test["password"])

    print(f"Test Case ID: {test['id']}")
    print(f"Expected: {test['expected']}, Actual: {actual}")

    if actual == test["expected"]:
        print("Result: PASSED\n")

    else:
        print("Result: FAILED")
        print("Log Defect: Mismatch in login result\n")
