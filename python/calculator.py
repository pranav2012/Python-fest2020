# Importing modules
import math

# defining functions
def add(s,t):
    print('sum of',s,'and',y,'is',s+t)
def sub(s,t):
    print('difference of',s,'and',y,'is',s-t)
def mul(s,t):
    print('product of',s,'and',y,'is',s*t)
def div(s,t):
    print('quotient of',s,'and',y,'is',s/t)
    

# Running while loop
q='y'
while q=='y':
    x=int(input('enter the first number: '))
    y=int(input('enter the second number: '))

    if x<y:
        x,y=y,x
        
    print('''Enter + for additon
            Enter - for subraction
            Enter * for multiplication
            Enter / for division
    '     ''')
    a=input('what operation do you want? ')
    if a=='+':
        add(x,y)
    elif a=='-':
        sub(x,y)
    elif a=='*':
        mul(x,y)
    elif a=='/':
        div(x,y)
    else:
        print('Operation not defined ')
    q=str(input('do you want to continue enter y: '))
    
# ==== CODE ENDED ====
