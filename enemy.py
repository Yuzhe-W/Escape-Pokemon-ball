from graphics import *
from random import randrange
class Enemy:
    def __init__(self,side,win):
        self.win=win
        self.side=side
        xPos=randrange(0+side,win.getWidth()-side)
        yPos=randrange(-2*self.win.getHeight(),0)
        #self.avatar=Circle(Point(xPos,yPos),randrange(10,20))
        self.avatar = Image(Point(xPos,yPos),"pokeball.gif")
        #self.avatar.setFill('yellow')
        self.speed=15

    def draw(self):
        self.avatar.draw(self.win)

    def move(self):
        time.sleep(0.07)
        self.avatar.move(0,self.speed)



    def getX(self):
        #return self.avatar.getCenter().getX()
        if type(self.avatar)==type(Circle(Point(0,0),5)):
            return self.avatar.getCenter().getX()
        elif type(self.avatar)==type(Image(Point(0,0),"")):
            return self.avatar.getAnchor().getX()
        else:
            print("Type is not understood")

    def getY(self):
        #return self.avatar.getCenter().getY()
        if type(self.avatar)==type(Circle(Point(0,0),5)):
            return self.avatar.getCenter().getY()
        elif type(self.avatar)==type(Image(Point(0,0),"")):
            return self.avatar.getAnchor().getY()
        else:
            print("Type is not understood")
    
    def getSide(self):
        return self.side

    def isDead(self):
        if self.getY()>self.win.getHeight():
            return True
        else:
            return False

    def undraw(self):
        self.avatar.undraw()