from graphics import *
from player import Player
from enemy import Enemy
from random import randrange
class Dodger:
    def __init__(self):
        self.win=win=GraphWin("Dodger",300,400)
        self.win.setBackground("dodgerblue")
        av2=Image(Point(150,370),"pika.gif")
        self.player=Player(av2,win)
        self.player.draw()
        self.player.getX()
        self.enemy=Enemy(30,win)
        self.enemy.draw()

        self.enemies=[]
        self.enemyNum = randrange(10,20)
        self.createEnemies(self.enemyNum)
        self.message=Text(Point(150,300),"")
        self.scoremessage=Text(Point(50,10),"Score: 0")
        self.scoremessage.draw(win)
        self.score=0




    def createEnemies(self,count):
        for i in range(count):
            side=randrange(10,30,5)
            e=Enemy(side,self.win)
            e.draw()
            self.enemies.append(e)


    def run(self):
        self.message.setText("Help Pikachu escape pokeball!!")
        self.message.draw(self.win)
        time.sleep(3)
        self.message.undraw()

        self.message.setText("countdown: 3")
        self.message.draw(self.win)
        time.sleep(1)
        self.message.undraw()

        self.message.setText("countdown: 2")
        self.message.draw(self.win)
        time.sleep(1)
        self.message.undraw()

        self.message.setText("countdown: 1")
        self.message.draw(self.win)
        time.sleep(1)
        self.message.undraw()

        self.message.setText("game start!!")
        self.message.setSize(25)
        self.message.setStyle("bold italic")
        self.message.draw(self.win)
        time.sleep(1)
        self.message.undraw()

        while True:
            key = self.win.checkKey()
            if key == 'q':
                break
            elif key!='':
                print(key)
            self.player.move(key)
            for e in self.enemies:
                e.move()
            
            self.cleanDead()
            print("rest enemies count:",len(self.enemies))

            if self.checkCollision() == True:
                self.message.setText("lose (Please enter a bottom to quit)")
                self.message.setSize(12)
                self.message.draw(self.win)
                break
            if self.score == self.enemyNum:
                self.message.setText("Pass!! (Please Enter a bottom to quit)")
                self.message.setSize(12)
                self.message.setStyle('bold')
                self.message.draw(self.win)
                break

        self.win.getKey()
        self.win.close()
    
    def checkCollision(self):
        for enemy in self.enemies:
            minDist  =enemy.getSide() / 2 + self.player.getSide()
            vertical=abs(self.player.getY() - enemy.getY()) < minDist
            horizontal=abs(self.player.getX()-enemy.getX())<minDist
            if vertical and horizontal:
                return True
        return False

    def scoreUpdate(self):
        self.scoremessage.setText("Score:"+str(self.score))    

    def cleanDead(self):
        alive=[]
        for enemy in (self.enemies):
            if enemy.isDead():
                self.score=self.score+1
                self.scoreUpdate()
                enemy.undraw()
                continue#comment
            alive.append(enemy)
        self.enemies=alive

