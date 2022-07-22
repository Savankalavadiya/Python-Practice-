#Funcation with No Arguments & No Return Value

def printLine():
    print('*'*50)
printLine()
print('Welcom To User Defined Funcation')
printLine()

#Funcation with Arguments But No Return Value

def add(a,b):
    print('Addition :',a+b)

printLine()
x=int(input('Enter Value:'))
y=int(input('Enter Value:'))
add(x,y)
printLine()

#Funcation with Arguments & Return Value

def sub(a,b):
    return a-b

printLine()
x=int(input('Enter Value:'))
y=int(input('Enter Value:'))
z=sub(x,y)
print('Subtraction : ',z)
printLine()
