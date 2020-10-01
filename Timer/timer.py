import time
sec = int(input("Enter no. of seconds: "))

for i in range(sec):
    print(sec - i, "seconds left")
    time.sleep(1)

print("Time Over!!!!")
