def is_palindrome_possible(word):
    #check if the number of letters appearing odd number of times is either 0 or 1 
    return len( [ch for ch in word.lower if word.count(ch) % 2 == 1] ) <= 1 

if __name__ == '__main__':
    word = input("Enter a word to check if it's palindrome are possible or not: ")
    response = is_palindrome_possible(word)
    if response:
        print("Yes")
    else:
        print("No")
