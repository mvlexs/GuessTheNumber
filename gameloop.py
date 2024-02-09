import random
import number

obj = number.Number(0,0,0,0)

def gameloop():
    obj.randomNumber = random.randint(obj.minRange,obj.maxRange)
    print ("I have chosen my number, try and guess it! :D")
    x = 0
    while 0 == x :
        obj.guessNumber = int(input())
        if obj.guessNumber > int(obj.randomNumber):
            print ("My number is smaller")
            x += 1
        elif obj.guessNumber < int(obj.randomNumber):
            print ("My number is bigger")
            x += 1
        elif obj.guessNumber == int(obj.randomNumber):
            print("Congrats! You guessed my number")
            playAgain()
            x = 4 
            # add playagain with same range
        else:
            print ("Something went wrong")
    while 3 > x > 0:
        print ("Try again!")
        obj.guessNumber = int(input())
        if obj.guessNumber > int(obj.randomNumber):
            print ("My number is smaller")
            x += 1
        elif obj.guessNumber < int(obj.randomNumber):
            print ("My number is bigger")
            x += 1
        elif obj.guessNumber == int(obj.randomNumber):
            print("Congrats! You guessed my number")
            playAgain()
            x = 4 
    while x == 3:
        print ("You are out of guesses, you lose :(\nMy Number was: " + str(obj.randomNumber))
        playAgain()
    while x > 3:
        print("What the heck did you do?")



def play():
    print ("Please enter the lowest number you want to be in range for our guessing game.")
    obj.minRange = int(input())
    
    print ("Now please enter the highest number you want to be in range.")
    obj.maxRange = int(input())
   
    #add handler for input() =! int
    
    gameloop()
    

#ask if user wants to play again
def playAgain():
    print("Do you want to play again? y/n")
    ab = 1
    while ab == 1:
        y = input()
        if y == "y" or y == "yes" or y == "Yes" or y == "YES":
            same()     
        elif y == "n" or y == "no" or y == "No" or y == "NO":
            exit()
        else:
            print("Unrecognized input, please try again")

#play with same range check
def same():
    print("Do you want to play with the same range?\ny/n")
    bc = 1
    while bc == 1:
        i = input()
        if i == "y" or i == "yes" or i == "Yes" or i == "YES":
            gameloop()
        elif i == "n" or i == "no" or i == "No" or i == "NO":
            play()
        else:
            print("Unrecognized input, please try again")