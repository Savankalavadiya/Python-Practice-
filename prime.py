n=int(input('enter no:'))
if n%2==0:
    print (n,'Is not prime')

else:
    for i in range (3,int(n/2)+1,2):
        if n%i==0:
            print(n,'IS not prime')
            break
    else:
        print(n,'Is prime')
        
