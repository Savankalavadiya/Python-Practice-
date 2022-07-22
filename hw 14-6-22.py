#creat the funcation for how many characters
#1
s='My Name Is Savan Kalavadiya'
k=0
for i in s:
    if i.isalnum():
        k+=1
print('Total Number Of Char.',k)

# create the funcation for how many space
#2

s='My Name Is Savan Kalavadiya'
p=0
for i in s:
    if i.isspace():
        p+=1
print('total num of space:',p)


#create the fun for count the words
#3

s='My Name Is Savan Kalavadiya'
p=1
for i in s:
    if i.isspace():
        p+=1
print('total num of words',p)

#print('total num of words:',len(s.split())) #for one line code for ans if not using loops#

