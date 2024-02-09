import gameloop
def tutorial():
    print("Hello, we are playing the random number Game today, would you like an explanation first?\ny/n")
    a = 1
    while a == 1:
        y = input()
        if y.lower() == "y" or y.lower() == "yes":
            print("1.You select a range of numbers.\n2.I select a random Number\n3.You try to guess it, you get 3 tries in total\n4.If you guess a wrong number i will tell you if my number is higher or lower than the one you guessed\nThats it, so let us begin!")
            gameloop.play()
        elif y.lower() == "n" or y.lower() == "no":
            print ("Okay, lets continue then!")
            gameloop.play()
        else:
            print("Unrecognized input, please try again")


        