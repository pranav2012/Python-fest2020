#implementation of stack using list in python
s=[]
#index for top element of stack
top=-1
print("Enter 1 for POP operation")
print("Enter 2 for PUSH operation")
print("Enter 3 for PEEK operation")
t=1;
while(t):
    i=int(input("enter your choice"))
    if(i==1):
        #underflow-condition
        if(top==-1):
            print("No item in stack to delete ")
        else:
            #delete the element at top of the stack
            s.pop()
            #deacrease value of top by 1
            top-=1
    if(i==2):
        item=int(input("enter item to append "))
        s.append(item)
        #increase value of top by 1
        top+=1
    if(i==3):
        #peek operation gives the value of element at top
        if(top==-1):
            print("no element is there in stack !!")
        else:
            print("the element at top is ",s[top])
    t=int(input("enter 0 if you want to discontinue "))
#print final stack
print("final stack formed is",s)

#sample input-output
#Enter 1 for POP operation
#Enter 2 for PUSH operation
#Enter 3 for PEEK operation
#enter your choice2
#enter item to append 90
#enter 0 if you want to discontinue 2
#enter your choice2
#enter item to append 89
#enter 0 if you want to discontinue 8
#enter your choice3
#the element at top is  89
#enter 0 if you want to discontinue 0
#final stack formed is [90, 89]
