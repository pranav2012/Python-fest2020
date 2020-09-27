#take the input from the user end in the integer format
input_num = int(input("Enter the number:"))

#define the factorial function
def factorial(input_num):
	f = 1
	if input_num < 0:
		print("Factorial cannot be calculated")
	elif input_num == 0:
		print("Factorial of 0 is 1")
	else:
		for i in range(1,input_num+1):
			f = f * i
		return f


#call the factorial function
print(factorial(input_num))