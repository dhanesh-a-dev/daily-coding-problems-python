'''Schema Validator Part 4
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
Extra keys are allowed
Tests:
Passed:1. is_valid_schema({"username": "vivian", "posts": 1, "verified": False, "role": "user", "supporter": True}) should return True.
Passed:2. is_valid_schema({"username": "rudolph", "posts": 15, "verified": True, "role": "creator"}) should return True.
Passed:3. is_valid_schema({"username": "hernandez", "posts": 35, "verified": True, "role": "moderator", "supporter": False, "followers": 55}) should return True.
Passed:4. is_valid_schema({"username": "julia", "posts": 50, "verified": True, "role": "admin", "supporter": "true"}) should return False.
Passed:5. is_valid_schema({"username": "bernard", "posts": 0, "verified": True, "role": "friend", "supporter": True}) should return False.
Passed:6. is_valid_schema({"username": "felix", "posts": 40, "verified": "yes", "role": "staff", "supporter": False}) should return False.
Passed:7. is_valid_schema({"username": "jimmy", "posts": True, "verified": False, "role": "creator", "supporter": True}) should return False.
Passed:8. is_valid_schema({"username": True, "posts": 30, "verified": True, "role": "moderator", "supporter": False}) should return False.'''

def is_valid_schema(obj):
    return (
        all(key in obj for key in ['username', 'posts', 'verified', 'role']) and
        isinstance(obj['username'], str) and
        type(obj['posts']) is int and
        isinstance(obj['verified'], bool) and
        obj['role'] in ["user", "creator", "moderator", "staff", "admin"] and
        ('supporter' not in obj or isinstance(obj['supporter'], bool))
    )