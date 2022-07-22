
#1)
'''
for i in range(10):
    print('I : ',i)
print('************')
'''

#2)
'''
for i in range (3,10):
    print ('I : ',i)
print('****The End****')

'''

#3)
'''
for i in range (1,10,2):
    print ('I : ',i)
print('****The End****')

for i in range (10,0,-2):
    print ('I : ',i)
'''

#4)
'''
for i in range (1,10):
    print('*'*i)

for i in range (1,10):
    print(' '*(9-1),'*'*i)

for i in range (9,0,-1):
    print (' '*(9-i),'*'*i)
for i in range(1,10):
    print (' '*(9-i),'*'*i) #Note If you want nine space than (9-i)

'''

#5) hw 1 12 123 1234
for i in range (1,10):
    for j in range (1,i+1):
        print (j,end=' ')
    print()




#6)hw 9 87 87654 
for i in range (9,0,-1):
    print(''*i,*range(9,i-1,-1))

    






