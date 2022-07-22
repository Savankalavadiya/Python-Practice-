#1.Write a Python program to check if a number is positive, negative or zero.

n=int(input('Enter the Number :'))
if (n>0):
    print('Number Is Positive')
elif (n==0):
    print ('Number Is Zero')
else:
    print('Number Is Negitive')
    

#2.Write a Python program to get the Factorial number of given number.

n=int(input('Enter Number For Fac.'))
s=1
while n>=1:
    s=s*n
    n=n -1
print(s)

#3.Write a Python program to get the Fibonacci series of given range.

n=int(input('Enter N :'))
a,b=0,1
print(a,end=' ')
while b<n:
    print(b,end=' ')
    a,b=b,a+b


#4.How memory is managed in Python?

                                
#5.What is the purpose continue statement in python?

#6.Write python program that swap two number with temp variable and without temp variable.

x=int(input('Enter x :'))
y=int(input('Enter y :'))
temp=x
x = y
y=temp
print('x after swap :',x)
print('y after swap :',y)


x=int(input('Enter x :'))
y=int(input('Enter y :'))
x,y=y,x

print('x after swap :',x)
print('y after swap :',y)


#7.Write a Python program to find whether a given number is even or odd,print out an appropriate
#message to the user

n=int(input('Enter the Number'))
if n%2==0:
      print(n,'Is An Even Number')
else:
      print(n,'Is An Odd Number')

#8.Write a Python program to test whether a passed letter is a vowel or not.

n=str(input('Enter the Character :'))
if(n=='a' or n=='e'or n=='i' or n=='o' or n=='u'):
    print('Character IS Vowel')
else:
    print('Character Consonant')


#9.Write a Python program to sum of three given integers.However, if two
#values are equal sum will be zero


a=int(input('Enter A :'))
b=int(input('Enter B :'))
c=int(input('Enter C :'))

if a==b or b==c or a==c :
      print ('Sum Is Zero')
else:
     print('sum is : ',a+b+c)



#10.Write a Python program that will return true if the two given integer values
#are equal or their sum or difference is 5.

a=int(input('Enter A :'))
b=int(input('Enter B :'))
c=a+b
d=a-b
if a==b or c==5 or d==5:
    print('True')
else:
    print('False')


#11.Write a python program to sum of the first n positive integers.

n=int(input('Enter Number'))

sum=(n*(n+1))/2
print (int(sum))

a=0
while n>0:
    a=a+n
    n=n-1
print(a)


#12.Write a Python program to calculate the length of a string.

a=str(input('Enter String'))
print(len(a))



#13.Write a Python program to count the number of characters (character
#frequency) in a string

a=str(input('Enter String'))
b=0
for i in a:
    if i.isalnum():
        b+=1
print(b)


#14. What are negative indexes and why are they used?


#15.Write a Python program to count occurrences of a substring in a string.

str1 = 'Savan Savan Kalavadiya'
str2 = 'Patel Savan Savan Kalavadiya'
print(str1.count('Savan'))
print(str2.count('Savan'))

#16.Write a Python program to count the occurrences of each word in a given sentence


str5 = 'Savan Savan Kalavadiya'
print(str5.count('Savan'))

#17.Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

a='savan'
b='kalavadiya'
c=b[0:2]+a[2:]
d=a[0:2]+b[2:]
print(c,' ',d)

#or

str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")
 
x=str1[0:2]
 
str1=str1.replace(str1[0:2],str2[0:2])
 
str2=str2.replace(str2[0:2],x)
 
print("Your first string has become :- ",str1)
print("Your second string has become :- ",str2)

#18.Write a Python program to add 'ing' at the end of a given string (length
#should be at least 3). If the given string already ends with 'ing' then add 'ly'
#instead if the string length of the given string is less than 3, leave it
#unchanged

a=str(input('Enter The String:'))    
b=0
for i in a:
      b+=1
    
if a[-3:]=='ing':  #or If a.endwith(ing):
     print(a[:-3]+"ly")
     print(a+'ly')
elif b>=3:
    print(a+'ing')
else:
    print(a,'string will remain unchanged')

#19.Write a Python program to find the first appearance of the substring 'not'
#and 'poor' from a given string, if 'not' follows the 'poor', replace the whole
#'not'...'poor'substring with 'good'. Return the resulting string.


a=str(input('Enter the String : '))
c=a.find('not poor')
#d=a.find('poor')
if c>=0:
      a=a.replace(a[c:c+8],'good')
      print(a)


#20.Write a Python function that takes a list of words and returns the length
#of the longest one.


a=str(input('Enter the string'))
b=list(a.split())
print(b)
c=0
for i in b:
      if len(i) > c:
            c=len(i)
            d=i
print ('enter the length of longest word is ',c)
print('longest word',d)

#21.Write a Python function to reverses a string if its length is a multiple of 4

name=input("enter a name:")

if(len(name)%4==0):
    print(name[::-1])
else:
    print(name)

#22.Write a Python program to get a string made of the first 2 and the last 2
#chars from a given a string. If the string length is lessthan 2,return instead
#of the empty string.


a=str(input('enter string :'))
if len(a)<2:
      print('empty string')
else:
      b=a[:2]+a[-2:]
      print(b)



#23.Write a Python function to insert a string in the middle of a string.


a=str(input('enter the string : '))
b=str(input('enter the string : '))
c=int(len(a)/2)
d=a[:c]+b+a[c:]
print(d)


























     
    






























    



















      
      


