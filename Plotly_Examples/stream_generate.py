import json
from random import randint

n = 0
x=[]
y=[]
while n < 3:
    x.append(randint(0,9))
    y.append(randint(0,9))
    n += 1
d = {"x":x, "y":y, 'type':'scatter'}
json.dump(d, open("nums.txt",'w'))
#  example write x=[5, 7], y=[8, 9]
