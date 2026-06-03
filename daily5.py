'''QUESTION: Schema Validator Part 3
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}
The pipe (|) symbol means "or". role must be one of the listed Roles values.
Extra keys are allowed
Tests:
Passed:1. is_valid_schema({"username": "henry", "posts": 0, "verified": True, "role": "staff"}) should return True.
Passed:2. is_valid_schema({"username": "sara", "posts": 45, "verified": False, "role": "creator", "followers": 70}) should return True.
Passed:3. is_valid_schema({"username": "penelope", "posts": 20, "verified": True, "role": "admin"}) should return True.
Passed:4. is_valid_schema({"username": "kevin", "posts": 0, "verified": False, "role": "user"}) should return True.
Passed:5. is_valid_schema({"username": "george", "posts": 15, "verified": True, "role": "moderator"}) should return True.
Passed:6. is_valid_schema({"username": "david", "posts": 0, "verified": False, "role": "guest"}) should return False.
Passed:7. is_valid_schema({"username": "wendy", "posts": 10, "verified": True}) should return False.
Passed:8. is_valid_schema({"username": "fabian", "posts": 1, "verified": True, "role": True}) should return False.
Passed:9. is_valid_schema({"username": 8, "posts": 1, "verified": True, "role": "user"}) should return False.
Passed:10. is_valid_schema({"username": "penny", "posts": "10", "verified": True, "role": "staff"}) should return False.
Passed:11. is_valid_schema({"username": "john", "posts": "1", "verified": "true", "role": "admin"}) should return False.
from freeCodeCamp'''

def is_valid_schema(obj):
    return (all(key in obj for key in ['username', 'posts', 'verified', 'role']) and
    isinstance(obj['username'],str) and
    isinstance(obj['posts'],int) and
    isinstance(obj['verified'],bool) and 
    obj['role'] in ["user","creator","moderator","staff","admin"])