import time

# Taking time input from the user
seconds = int(input("Enter no. of seconds: "))

for i in range(seconds):
    print(seconds - i, "seconds left")
    time.sleep(1)

print("Time Over!!!!")
