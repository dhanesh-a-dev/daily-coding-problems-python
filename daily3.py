'''Schema Validator Part 1
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:

{
  username: string
}
Extra keys are allowed
Tests:
Passed:1. is_valid_schema({"username": "bob"}) should return True.
Passed:2. is_valid_schema({"username": "jen", "posts": 30}) should return True.
Passed:3. is_valid_schema({"username": ""}) should return True.
Passed:4. is_valid_schema({"username": 7}) should return False.
Passed:5. is_valid_schema({"posts": 25}) should return False.
from freeCodeCamp'''

#Mycode
def is_valid_schema(obj):
    flag=0
    for key in obj:
        if key=="username":
            if type(obj[key]) is str:
                flag=1
    if flag==0:
        return False
    else:
        return True


#Better version from AI
'''
def is_valid_schema(obj):
    return "username" in obj and isinstance(obj["username"], str)'''