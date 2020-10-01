

l=[]  #empty list
#taking 3 input value and appending in the list
l.append(int(input('Enter your first number: ')))
l.append(int(input('Enter your second number: ')))
l.append(int(input('Enter your third number: ')))
x=l[0] #setting a defult value
#checking which is largest
for i in range (1,3):
    if x<l[i]:
        x=l[i]
#printing the output
print('largest number among',l,'is',x)
input('press enter to leave ')

