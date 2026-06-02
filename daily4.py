'''Question:Schema Validator Part 2
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string,
  posts: number,
  verified: boolean
}
Extra keys are allowed
Tests:
Passed:1. is_valid_schema({"username": "alice", "posts": 10, "verified": False}) should return True.
Passed:2. is_valid_schema({"username": "carol", "posts": 15, "verified": True, "followers": 25}) should return True.
Passed:3. is_valid_schema({"username": "frank", "posts": "21", "verified": True}) should return False.
Passed:4. is_valid_schema({"username": "sam", "posts": 17, "verified": "false"}) should return False.
Passed:5. is_valid_schema({"username": "bill", "verified": True}) should return False.
Passed:6. is_valid_schema({"username": "fred", "verified": True}) should return False.
Passed:7. is_valid_schema({"username": 5, "posts": 10, "verified": True}) should return False.

from freeCodeCamp'''

def is_valid_schema(obj):
    return ("username" in obj and 
    "posts" in obj and 
    "verified" in obj and 
    isinstance(obj['username'],str) and
    isinstance(obj['posts'],int) and 
    isinstance(obj['verified'],bool))