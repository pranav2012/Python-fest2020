print("hello world")
print('IN THIS PROGRAM WE WILL CREATE A PYTHON PROGRAM TO PROVIDE DIFFERENT OPTIONS TO CALCULTE TWO NUMBERS')
print ('It will let you know your answer obtained is an even or odd number')
print("enter 2 numbers")
x=int(input())
y=int(input())
answer = 0
print("choose any of these option (+,-,*,/) ")
option=input()
if option == '+':
  answer=x+y
elif option == '-':
  answer=x-y
elif option == '*':
  answer=x*y
elif option == '/':
  answer=x / y
else:
  print("wrong option")

print(x,option,y,":",answer)
if answer%2==0 :
   print('The answer obtained is an even number')
else :
   print('Answer obtained is an odd number')

print('end')
