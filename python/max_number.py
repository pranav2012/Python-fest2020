#import important modules
import numpy as np  

# inp_list = [0.1, 0.3, 0.5, 0.7, 0.9, 0.5]

#take the input from the user end and split it on the basis on ","
print("Enter the list ")
input_num = list(map(float, input().split(",")))

def max_number(input):
	max_number = max(input)
	print(max_number)

max_number(input_num)