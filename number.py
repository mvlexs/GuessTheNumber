class Number():
    maxRange = None
    minRange = None
    guessNumber = None
    randomNumber = None
    score = 0
    input = None

    def __init__(self, maxRange, minRange, guessNumber, randomNumber, score, input):
        self.maxRange = maxRange
        self.minRange = minRange
        self.guessNumber = guessNumber
        self.randomNumber = randomNumber
        self.score = score
        self.input = input

    def displayScore(self):
        
        print("You currently have " + str(self.score)+ " points!" )
    
    def getMinRange(self):
        self.getInput()
        self.minRange = self.input

    def getMaxRange(self):
        self.getInput()
        self.maxRange = self.input

    def getInput(self):
        while True:
            try:
                self.input = int(input())
                return self.input
            except ValueError:
                print("Unrecognized input, please try again!")
            except TypeError:
                print("Unrecognized input, please try again!")

