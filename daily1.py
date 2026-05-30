''' Question: Pizza Party
Given an array of hours worked today per person,
return the number of pizzas to order for a pizza party.

Divide each person's hours worked by 3 to get their slice count.
You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
Each person gets a minimum of two slices.
Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza.
'''

import math 
l=eval(input('Hours worked as a list: '))
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
    return s
print(get_pizzas_to_order(l))