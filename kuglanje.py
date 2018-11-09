class Frame:

    isSpare = False
    isStrike = False
    
    def __init__(self):#Sets the value of the rolls to -1 to indicate that the ball has not been thrown
        self.roll = [-1, -1]

    def frametype(self): #check if the frame was a spare, strike or normal
        if(self.roll[0] == 10 or self.roll[1] == 10):
            self.isStrike = True
        elif(self.roll[0] + self.roll[1] == 10):
            self.isSpare = True
    
    def __getitem__(self, attr):
        return attr
        
class Bowling:

    def __init__(self):
        self.frames = []
        for i in range(10):
            self.frames.append(Frame())



    def rollCheck(self, roll1, roll2): #checks if the roll values are within the allowed range

        if (roll1 > 10 or roll1 < 0):
            print("First roll invalid value!")
            return False
        elif (roll2 > 10 or roll2 < 0):
            print("Second roll invalid value!")
            return False
        elif (roll1 + roll2 > 10):
            print("Frame score invalid value")
            return False
        else:
            return True

    def score(self, currFrame, prevFrame, i): #scores the frame
        if(i == 0):#scoring for the first frame
            return currFrame.roll[0] + currFrame.roll[1]
        if(prevFrame.isStrike and currFrame.isStrike):#handles what happens if you roll multiple strikes in a row
            if (i == 1):
                return 20
            if (i > 1):
                return 30
        elif(prevFrame.isStrike and not currFrame.isStrike):
            return 2*(currFrame.roll[0] + currFrame.roll[1])
        elif(prevFrame.isSpare):
            return (2*currFrame.roll[0]) + currFrame.roll[1]
        else:
            return currFrame.roll[0] + currFrame.roll[1]


    def game(self): #frame score input
        currentscore = 0
        i = 0

        while (i<10):#roll input
            print("Frame" + str(i+1) + ":")
            while True:
                try:
                    self.frames[i].roll[0] = int(raw_input('Roll 1:'))
                    break
                except ValueError:
                    print("Wrong input please try again")
            if (self.frames[i].roll[0] == 10):#Handles if the strike happens on the first roll
                self.frames[i].roll[1] = 0
                self.frames[i].frametype()
                currentscore = currentscore + self.score(self.frames[i],self.frames[i-1], i)
                print("Your current score is: " + str(currentscore))
                i = i + 1
                continue;
            while True:
                try:
                    self.frames[i].roll[1] = int(raw_input('Roll 2:'))
                    break
                except ValueError:
                    print("Wrong input please try again")
            if(self.rollCheck(self.frames[i].roll[0], self.frames[i].roll[1])):
                 self.frames[i].frametype()
                 currentscore = currentscore + self.score(self.frames[i],self.frames[i-1], i)
                 print("Your current score is: " + str(currentscore))
                 i = i + 1
            else:
                print("Please enter your score again")
                
        print("Your final score is: " + str(currentscore))

newGame = Bowling()
newGame.game()
