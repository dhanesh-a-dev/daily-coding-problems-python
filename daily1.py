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