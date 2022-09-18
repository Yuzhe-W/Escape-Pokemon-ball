from player import Player
import random
class Simulation:
    def __init__(self,probA,probB,numGames):
        self.pl1=Player(probA)
        self.pl2=Player(probB)
        self.numGames=numGames
    
    def simulateGames(self):
        ScoreA=0
        ScoreB=0
        serving='A'
        while not (self.pl1.wonAgame(ScoreA) or self.pl2.wonAgame(ScoreB)):
            if serving=='A':
                if random.random()<self.pl1.getProb():
                    ScoreA=ScoreA+1
                else:
                    serving='B'
            else:
                if random.random()<self.pl2.getProb():
                    ScoreB=ScoreB+1
                else:
                    serving='A'
        return ScoreA,ScoreB

    def run(self):
        for i in range(self.numGames):
            ScoreA,ScoreB=self.simulateGames()
            if ScoreA>ScoreB:
                self.pl1.incWins()
            else:
                self.pl2.incWins()
        self.printReport()
        
    def printReport(self):
        print('player1 wins {0}'.format(self.pl1.getWins()))
        print('player2 wins {0}'.format(self.pl2.getWins()))



