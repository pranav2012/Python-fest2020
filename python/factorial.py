#take the input from the user end in the integer format
input_num = int(input("Enter the number:"))

#define the factorial function
def factorial(input_num):
	if input_num==0 or input_num==1:
		return 1
	else:
		return input_num*factorial(input_num-1)

#call the factorial function
print(factorial(input_num))
