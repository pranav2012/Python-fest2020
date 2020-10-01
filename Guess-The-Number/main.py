#number guessing game
# importing required modules
import random

# defining function named getchar 
def getchar():
   '''
   Returns a single character from standard input
   '''
   # importing other modules needed
   import tty, termios, sys
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

guess_number = 0

# Print statements
print("This is a number guessing game. \nYou will first choose a range of number. \nThen we will generate a secreat number.\nYou have to guess it in minimum number of tries.")
print("If you enter your guess we will inform you either the number is smaller than the secreat number or bigger.")
print("RULE : give all inputs as integers\nPress Enter" ,end = "")

# Running while loop to find the range
while getchar() and not guess_number:
    print("\nChoose Your Range")
    #print("Your number will be in between :")
    print("Enter the starting number:", end = "")
    start = int(input())
    print("Enter the ending number: ",end = "")
    end = int(input())
    #guess_number = 0
    ans = random.randint(start,end)
    if ans == ValueError:
    	print("Your range is wrong")
    else:
      # Running a while loop inside a if statement
        while True:
            print("Enter your guess: ",end = "")
            user_input = int(input())
            guess_number+=1
            if user_input == ans:
                print("Congratulations!! You have made it. \n This is the secreat number")
                break
            elif user_input > ans:
                print("Try something small")
            elif user_input < ans:
                print("Try something big")
            else:
                print("Please follow the rules!!!")
    exit()
   # Exiting the game



