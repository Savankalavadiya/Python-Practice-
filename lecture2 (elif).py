# All IF Condition

# 1)
'''

a=int(input('Enter A:-'))
b=int(input('Enter B:-'))
c=int(input('Enter C:-'))

if a>b:
    if a>c:
        print (a,'Is Greter Value')
    else:
        print (c,'Is Greter Value')
elif b>c:
    print (b,'Is Greter Value')
else:
    print (c,'Is Greter Value')
    

    
# 2)


rno=int(input('Enter Roll No :-'))
sname=input('Enter Student Name :-')
s1=int(input('Enter Mark Of Sub 1:-'))
s2=int(input('Enter Mark Of Sub 2:-'))
s3=int(input('Enter Mark Of Sub 3:-'))

Total=s1+s2+s3
Per=Total/3

print('Roll no :-',rno)
print('Student Name :-',sname)
print('Total :-',Total)
print('Percentage :-',Per)

if Per>=70:
    print('Distinction')
elif Per>=60:
    print('First Class')
elif Per>=50:
    print ('Second Class')
elif Per>=40:
    print ('Pass Class')
else:
    print ('Fail')

'''












