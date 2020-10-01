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
print("This is a number guessing game. \nYou will first choose a range of number. \nThen we will generate a secret number.\nYou have to guess it in minimum number of tries.")
print("If you enter your guess we will inform you either the number is smaller than the secret number or bigger.")
print("RULE : give all inputs as integers\nPress Enter" ,end = "")

# Running while loop to find the range
while getchar() and not guess_number:
    print("\nChoose Your Range")
    #print("Your number will be in between :")
    print("Enter the starting number:")
    start = int(input())
    print("Enter the ending number: ")
    end = int(input())
    #guess_number = 0
    ans = random.randint(start,end)
    if ans == ValueError:
    	print("Your range is wrong")
    else:
      # Running a while loop inside a if statement
      # When the user the guess_number reaches 5, the game will end
        while (guess_number<5):
           
            print("Enter your guess: ",end = "")
            user_input = int(input())
            guess_number+=1
            
            if guess_number==5:
                print("Sorry no more guesses! You lost!")
                break
            
            
            if user_input == ans:
                print("Congratulations!! You have made it. \n This is the secret number")
                break
            elif user_input > ans:
                print("Try something small")
            elif user_input < ans:
                print("Try something big")
            else:
                print("Please follow the rules!!!")
    exit()
   # Exiting the game



