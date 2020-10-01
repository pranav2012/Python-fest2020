#import important modules
import numpy as np  

input_num = [0.1, 0.3, 0.5, 0.7, 0.9, 0.5]

#take the input from the user end and split it on the basis on "," you can give the integer as input values too by using int instead of float
# input_num = list(map(float, input().split(",")))
# input_num = list(map(int, input().split(",")))


#defiene the function
def max_number(input):
	max_number = max(input)
	return max_number


#call the max function
print(max_number(input_num))