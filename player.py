
from graphics import*
class Player:
    def __init__(self,avatar,win):
        self.avatar=avatar
        self.step=25
        self.win=win

    def move(self,key):
        if key=='Left':
            self.moveL()
        elif key=='Right':
            self.moveR()
     

    def moveR(self):
        x=self.getX()
        if (x + self.step) < self.win.getWidth():
            self.avatar.move(self.step,0)
      

    def moveL(self):
        x=self.getX()
        if (x - self.step) > 0:
            self.avatar.move(-self.step,0)
        


    def draw(self):
        self.avatar.draw(self.win)

    def getX(self):
        if type(self.avatar)==type(Circle(Point(0,0),5)):
            return self.avatar.getCenter().getX()
        elif type(self.avatar)==type(Image(Point(0,0),"")):
            return self.avatar.getAnchor().getX()
        else:
            print("Type is not understood")

    def getY(self):
        if type(self.avatar)==type(Circle(Point(0,0),5)):
            return self.avatar.getCenter().getY()
        elif type(self.avatar)==type(Image(Point(0,0),"")):
            return self.avatar.getAnchor().getY()
        else:
            print("Type is not understood")
    

    
    def getSide(self):
        return self.avatar.getWidth()