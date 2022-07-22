# tuple will be made in round bracket ()

t = (1,2,10,1.1,[10,20,30],'tops',True,'python',1,2,100)

print(t)
print(t.count(1))
print(t.index(100))
print(1.1 in t) # we can use it in list as well #answer will be True or False
print(t[5])
t[4].append(40) #tuple ni andar list hoy to ene change kari skie..
print(t[4])

n=int(input('Enter Number : '))
d1={}
for i in range(1,n+1):
    d1[i]=i*i

print(d1)



