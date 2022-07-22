import random

# Demo Program 
l=[22,6,1992,'savan','ahmedabad',True,2.2,29,False,'python']
print(random.choice(l)) #any Random num or char print when run

#Lucky Number Print

l=[]
lucky=[]

for i in range (1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)
