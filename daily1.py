''' Question: Pizza Party
Given an array of hours worked today per person,
return the number of pizzas to order for a pizza party.

Divide each person's hours worked by 3 to get their slice count.
You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
Each person gets a minimum of two slices.
Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.

<<<<<<< HEAD
Tests:
Passed:1. get_pizzas_to_order([8, 8, 8]) should return 2.
Passed:2. get_pizzas_to_order([10, 9, 8, 2, 2, 6, 10]) should return 3.
Passed:3. get_pizzas_to_order([1, 2, 3, 4, 5]) should return 2.
Passed:4. get_pizzas_to_order([8, 8, 8, 8, 8, 8, 8, 8]) should return 3.
Passed:5. get_pizzas_to_order([9, 9, 6]) should return 1.
Passed:6. get_pizzas_to_order([10, 12, 16, 9, 8, 11, 15, 8, 0]) should return 5.

from freeCodeCamp'''
=======
Question from FreeCodeCamp
'''
>>>>>>> 8f14be31237de2512a66aa4d888985a48ffbf476

import math 
def get_pizzas_to_order(hours_worked): 
    s=0 
    for i in hours_worked: 
        x=i/3 
        if x<2: 
            s+=2 
        elif x>=2: 
            s+=math.ceil(x) 
    s=s/8 
    s=math.ceil(s) 
<<<<<<< HEAD
    return s
=======
    return s
print(get_pizzas_to_order(l))
>>>>>>> 8f14be31237de2512a66aa4d888985a48ffbf476
