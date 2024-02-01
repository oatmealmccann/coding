import random

x=99
number=[]
reverse=[]
for x in range(100):
    stuff= random.randrange(-1000,1000)
    number.append(stuff)
for y in range(100):
    hello=number[x]
    reverse.append(hello)
    x=x-1

print(number)
print(reverse)