from multiprocessing.managers import DictProxy
from operator import truediv
import random
from re import X


def position(string,guess):
    i = 0
    while i < len(string):
        if string[i] == guess:
            return i 
        i = i+1
    return 0

def checkwin(string,check):
    i = 0
    while i < len(string):
        if check[i] != string[i]:
            return False  
        i = i + 1
    return True        




def main():
    count = 0

    Hang_Man_Graphics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    Dictionary = ["peanuts","cats","dogs","pizza","kangaroo","meat","feat","fountain"]
    print("-------------------------------------------------------------------")
    print("Welcome to my hang man application, enter exit at any time to quit:")
    print("-------------------------------------------------------------------")
    check = ["_"]*10
    counter = 0
    current_guess = random.randrange(0,len(Dictionary)-1)
    
    while count > -1:

        print("Please enter your guess(lower case only)")
        guess = input()

        if guess == "exit" or guess == "Exit":
            break
        
        #checking for our guess in the word were currently looking at
        if guess in Dictionary[current_guess]:
            temp = position(Dictionary[current_guess],guess)
            check[temp] = guess
            try:
                x = 1
                while temp < len(Dictionary[current_guess]):
                    if(Dictionary[current_guess][temp+x] == guess):
                        check[temp+x] = guess
                        counter = counter + 1
                    x = x+1
            except Exception:
                pass
            #in case of a duplicate letter were just do this process twice but send the array from the element after the previous temp
            print("correct guess")
            counter = counter + 1
        else:
            print("Incorrect guess, try again:")
            count = count+1 #itterate to next stage of hang man

        print(Hang_Man_Graphics[count])
        print(check)

        if(count == 6):
            print("You lose, to play again press enter and to quit write exit:")    
            guess = input()
            count = 0
            counter = 0
            check = ["_"]*10
            current_guess = random.randrange(0,4)

        if (checkwin(Dictionary[current_guess],check) == True and counter >= len(Dictionary[current_guess])):
            print("You win, to play again press enter and to quit write exit:")
            guess = input() 
            check = ["_"]*10
            count = 0
            counter = 0
            current_guess = random.randrange(0,4)

        #Extra quit statement just so if the user wants to quit after they win/lose they can
        if guess == "exit" or guess == "Exit":
            break
        
        

    
if __name__ == "__main__":
    main()