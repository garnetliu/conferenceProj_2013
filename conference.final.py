#Conference
#Garnet Liu
from graphics import *
import random
import time
import math

import os
os.chdir('img')

#dialougeBox
#--------------------------------------------------------------------
#BUTTON

class Button:

    def __init__(self, win, shape, color, label):
        self.shape = shape
        self.shape.setFill(color)
        self.shape.draw(win)
        if label != None:
            self.text = Text(shape.getCenter(), label)
            self.text.draw(win)
        self.color = color

    def press(self):
        self.shape.setFill("gray")
        time.sleep(0.2)
        self.shape.setFill(self.color)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

#--------------------------------------------------------------------

class ArrowButton(Button):

    def __init__(self, win, p1, p2, p3, pl, pr, color):
        poly = Polygon(p1, p2, p3)
        Button.__init__(self, win, poly, color, None)
        self.position = Rectangle(pl, pr)
        self.pl = pl
        self.pr = pr

    def contains(self, point):
        x = point.getX()
        y = point.getY()
        leastX = self.pl.getX()
        greatestX = self.pr.getX()
        leastY = self.pl.getY()
        greatestY = self.pr.getY()
        if leastX <= x <= greatestX and leastY <= y <= greatestY:
            return True
        else:
            return False
        

#-------------------------------------------------------------------

class SquareButton(Button):

    def __init__(self, win, x, y, size, color, label):
        self.x1 = x - size/2
        self.x2 = x + size/2
        self.y1 = y - size/2
        self.y2 = y + size/2
        upperLeft = Point(self.x1, self.y1)
        lowerRight = Point(self.x2, self.y2)
        rect = Rectangle(upperLeft, lowerRight)
        Button.__init__(self, win, rect, color, label)

    def contains(self, point):
        x = point.getX()
        y = point.getY()
        if self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2:
            return True
        else:
            return False

#---------------------------------------------------------------

class Password:
    def __init__(self,p,n):
        self.x = p.getX()
        self.y = p.getY()
        self.key = Circle(p, .5)
        self.key.setFill("wheat")
        self.keyText = Text(p, n)

    def todraw(self, win):
        self.key.draw(win)
        self.keyText.draw(win)

    def press(self):
        self.key.setFill("gray")
        time.sleep(0.2)
        self.key.setFill("wheat")        

    def contains(self, point):
        x = point.getX()
        y = point.getY()
        distance = math.sqrt((x - self.x)**2 + (y - self.y)**2)
        if distance <= .5:
            return True
        else:
            return False
    def undraw(self):
        self.key.undraw()
        self.keyText.undraw()


#---------------------------------------------------------------
#Stuff

#objects
class Objects:
    def __init__(self):
        #set up objects for draw and image location
        self.imgStimulant = Image(Point(2, 2.5), "redpillbottle.gif")
        self.imgStimulant.p = Point(2, 2.5)
        
        self.imgTranquilizer = Image(Point(2.2, 2), "bluepillbottle.gif")
        self.imgTranquilizer.p = Point(2.2, 2)
        
        self.imgCup = Image(Point(3.5, 2.5), "cup.gif")
        self.imgCup.p = Point(3.5, 2.5)

        self.imgCupE = Image(Point(3.5, 2.5), "cupempty.gif")
        self.imgCupE.p = Point(3.5, 2.5)
        
        self.imgKey2H = Image(Point(5, 2.5), "goldkey.gif")
        self.imgKey2H.p = Point(5, 2.5)
        
        self.imgKey2R3 = Image(Point(4, .6), "bluekey.gif")
        self.imgKey2R3.p = Point(4, .6)

        self.imgPhone = Image(Point(4, 1.9), "cellphone.gif")
        self.imgPhone.p = Point(4, 1.9)

        #unpickable item
        self.imgLetter = Image(Point(4, 3), "letter.gif")
        self.imgMedical = Image(Point(4,3),"medicalhistory.gif")
        self.imgRedPill = Image(Point(7,.7),"redpill.gif")
        self.imgBluePill = Image(Point(1.2,.7),"bluepill.gif")
        self.imgDiary = Image(Point(4, 3), "diary.gif")
        self.imgMedical2 = Image(Point(4,3),"medicalhistory2.gif")
        self.imgBrainJar = Image(Point(4,3),"brain.gif")


        
        self.allObjects = [self.imgStimulant,self.imgTranquilizer,
                           self.imgCup,self.imgCupE,
                           self.imgKey2H,self.imgKey2R3,
                           self.imgPhone,
                           self.imgLetter,self.imgMedical,
                           self.imgRedPill,self.imgBluePill,
                           self.imgDiary,
                           self.imgMedical2,self.imgBrainJar]
        self.noNeed2Draw = [self.imgKey2H, self.imgKey2R3,
                            self.imgRedPill,self.imgBluePill]

#THE SHELF
class Shelf(Objects):
    def __init__(self):
        Objects.__init__(self)
        self.bposition = [Point(8.5, 4.5),Point(9.5, 4.5),Point(10.5, 4.5),
                         Point(8.5, 3.5),Point(9.5, 3.5),Point(10.5, 3.5),
                         Point(8.5, 2.5),Point(9.5, 2.5),Point(10.5, 2.5)]
        self.checkin = [False, False, False,
                        False, False, False,
                        False, False, False]
        #textbox
        self.textBox = Rectangle(Point(.5, 2), Point(7.5, .5))
        self.textBox.setFill("black")
        self.message = ""
        self.text = Text(Point(4, 1.25), self.message)
        self.text.setFill("White")
        self.text.setSize(20)



    def place(self, obj):
        for i in range(9):
            if self.checkin[i] == False:
                self.checkin[i] = obj
                dx = self.bposition[i].getX() - obj.p.getX()
                dy = self.bposition[i].getY() - obj.p.getY()
                obj.move(dx, dy)
                break

    def match(self,win, ButtonNum):
        #stimulant
        if self.checkin[ButtonNum] == self.allObjects[0]:
            self.updateText(win, "Stimulant...Not for me...where to use?")
            p = win.getMouse()
            if enterR(p,6,8,0,6) == True:
                return "stimulant"
            else:
                return ""
            
        #tranquilizer
        if self.checkin[ButtonNum] == self.allObjects[1]:
            self.updateText(win, "Tranquilizer...Not for me...where to use?")
            p = win.getMouse()
            if enterR(p,0,4.2,0,6) == True:
                return "tranquilizer"
            else:
                return "" 

        
        #cup
        if self.checkin[ButtonNum] == self.allObjects[2]:
            self.updateText(win, "Where to use the cup?")
            p = win.getMouse()
            if enterR(p,4,6,4,5) == True:
                return "spill"
            elif self.decisionText(win, "Drink it?") == "Y":
                self.updateText(win, "It's poisonous!")
                return "deadEnd"
            else:
                return ""
            

        #cup empty
        if self.checkin[ButtonNum] == self.allObjects[3]:
            self.updateText(win, "An empty cup...")
            return ""
            
        
        #key2Hall
        if self.checkin[ButtonNum] == self.allObjects[4]:
            self.updateText(win, "To use key, click the door")
            p = win.getMouse()
            if enterR(p,5,7,1,4) == True:
                return "go2Hall"
            else:
                return ""
        #key2R3
        if self.checkin[ButtonNum] == self.allObjects[5]:
            self.updateText(win, "To use key, click the door")
            p = win.getMouse()
            if  enterR(p,2.5,5.5,0,6) == True:
                return "go2Room3"
            else:
                return ""

        #cellphone
        if self.checkin[ButtonNum] == self.allObjects[6]:
            self.updateText(win, "Power is on.")
            if self.allObjects[11] in self.noNeed2Draw:
                if self.decisionText(win, "There is signal.'Mary' is in the call log...should I call?") == "Y":
                    return "end2"



        else:
            return ""

    def updateText(self, win, msg):
        self.textBox.draw(win)
        self.text.draw(win)
        self.text.setText(msg)
        p = win.getMouse()
        self.text.undraw()
        self.text.setText("")
        self.textBox.undraw()

    def decisionText(self, win, msg):
        self.textBox.draw(win)
        self.text.draw(win)
        self.text.setText(msg)
        self.yes = SquareButton(win, 7.375, 1.625, .75, "green", "YES")
        self.no = SquareButton(win, 7.375, .875, .75, "red", "NO")
        d = ""
        while d == "":
            p = win.getMouse()
            if self.yes.contains(p) == True:
                self.yes.press()
                d = "Y"
            elif self.no.contains(p) == True:
                self.no.press()
                d = "N"
        self.text.undraw()
        self.text.setText("")
        self.textBox.undraw()
        self.yes.undraw()
        self.no.undraw()
        return d
        
       
#---------------------------------------------------------------
#MAP
        
#room->set up in game(),setDirections

class BaseRoom:
    
    def __init__(self, name):
        self.name = name
        self.up = None
        self.down = None
        self.left = None
        self.right= None


    def __str__(self):
        return self.name
        
    def setDirections(self, u, d, l, r):
        self.up = u
        self.down = d
        self.left = l
        self.right = r




        

#rooms

class BlackR(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Fin")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("black")
    def todraw(self, win):
        self.wall.draw(win)
    def undraw(self):
        self.wall.undraw()        
    def getObject(self,p):
        None

class RedR(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Fin")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("red")
    def todraw(self, win):
        self.wall.draw(win)
    def undraw(self):
        self.wall.undraw()        
    def getObject(self,p):
        None

class BlueR(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Fin")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("light cyan")
    def todraw(self, win):
        self.wall.draw(win)
    def undraw(self):
        self.wall.undraw()        
    def getObject(self,p):
        None


class Room1F(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Room 1")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("beige")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("mint cream")
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))
        self.door2hall = Polygon(Point(5,1), Point(7,1), Point(7,4), Point(5,4))
        self.door2hall.setFill("gray")


    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)
        self.door2hall.draw(win)

    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()
        self.door2hall.undraw()

        
    def getObject(self,p):
        None



    


class Room1L(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Room 1")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("beige")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("mint cream")
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))
        #furniture
        self.imgDesk = Image(Point(2.5, 1.19), "desk.gif")
        
    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)
        self.imgDesk.draw(win)
        
        #objects
            #stilmulant
        if self.allObjects[0] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[0].draw(win)
            #cup
        if self.allObjects[2] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[2].draw(win)

    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()
        self.imgDesk.undraw()

        #objects
            #stimulant
        if self.allObjects[0] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[0].undraw()
            #cup
        if self.allObjects[2] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[2].undraw()

    
    def getObject(self,p):
            #stimulant
        if enterR(p,1.5,2.5,2,3):
            return self.allObjects[0]
            #cup
        if enterR(p,3,4,2,3):
            return self.allObjects[2]
        else:
            return None



class Room1R(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Room 1")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("beige")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("mint cream")        
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))
        #furniture
        self.imgMirror = Image(Point(5, 3.5), "mirrorSnot.gif")


    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)
        self.imgMirror.draw(win)
        #objects
            #key
        if self.allObjects[4] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[4].draw(win)

    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()
        self.imgMirror.undraw()

        #objects
            #key
        if self.allObjects[4] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[4].undraw()

    def getObject(self,p):
            #key
        if enterR(p,4.5,5.5,2.25,2.75):
            return self.allObjects[4]
        else:
            return None


class Room1B(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Room 1")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("beige")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("mint cream")
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))
        #furniture
        self.imgBed = Image(Point(3.5, .795), "bed.gif")
        #decor
        self.patch = Rectangle(Point(4, 4), Point(6, 5))
        self.patch.setFill("bisque2")
        self.patch.setOutline("bisque2")
        self.password = Text(Point(5,4.5), "Isolation Room 3")
        self.password.setSize(24)
        self.password.setFill("red")
        
        
    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)
        self.imgBed.draw(win)
        self.patch.draw(win)

    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()
        self.imgBed.undraw()
        self.patch.undraw()
        self.password.undraw()

    def getObject(self,p):
        None

    def spill(self,win):
        self.password.draw(win)

class Room1Rm(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Room 1")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("beige")
        self.imgMirrorL = Image(Point(4, 3), "mirrorLnot.gif")

        
    def todraw(self, win):
        self.wall.draw(win)
        self.imgMirrorL.draw(win)

    def undraw(self):
        self.wall.undraw()
        self.imgMirrorL.undraw()

    def getObject(self,p):
        None


class HallF(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Hall")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("white")
        self.floor = Polygon(Point(0,0), Point(3,3), Point(5,3), Point(8,0))
        self.floor.setFill("mint cream")
        self.door2 = Polygon(Point(7,1), Point(6,2), Point(6,6), Point(7,5))
        self.door2.setFill("gray")
        self.door1 = Polygon(Point(1,1), Point(2,2), Point(2,6), Point(1,5))
        self.door1.setFill("gray")
        self.door3 = Polygon(Point(3,3), Point(5,3), Point(5,6), Point(3,6))
        self.door3.setFill("SkyBlue4")
        
    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.door1.draw(win)
        self.door2.draw(win)
        self.door3.draw(win)

    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.door1.undraw()
        self.door2.undraw()
        self.door3.undraw()

    def getObject(self,p):
        None

class HallR(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Hall")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("white")
        self.imgOpenDoor = Image(Point(4,3),"dooropen.gif")
        self.imgCloseDoor = Image(Point(4,3),"doorclose.gif")
        
    def todraw(self, win):
        self.wall.draw(win)
        self.imgCloseDoor.draw(win)

    def undraw(self):
        self.wall.undraw()
        self.imgCloseDoor.undraw()
        
    def getObject(self,p):
        None

class HallL(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Hall")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("white")
        self.imgOpenDoor = Image(Point(4,3),"dooropen.gif")
        self.imgCloseDoor = Image(Point(4,3),"doorclose.gif")
        
    def todraw(self, win):
        self.wall.draw(win)
        self.imgCloseDoor.draw(win)

    def undraw(self):
        self.wall.undraw()
        self.imgCloseDoor.undraw()
        
    def getObject(self,p):
        None

class HallZ(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Hall")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("white")
        self.door = Rectangle(Point(1,0), Point(7,6))
        self.door.setFill("SkyBlue4")
        self.text = Text(Point(4,5.5),"LABOATORY NO.1 -- order matters")
        self.text.setFill("red")
        self.text.setSize(35)
        self.box = Rectangle(Point(2.5,4.5),Point(5.5,5.25))
        self.box.setFill("white")
        self.boxText = Text(Point(4,4.875),"")
        self.boxText.setSize(35)
        
        self.code = ""
        self.key1 = Password(Point(3,4),"1")
        self.key2 = Password(Point(4,4),"2")
        self.key3 = Password(Point(5,4),"3")
        self.key4 = Password(Point(3,3),"4")
        self.key5 = Password(Point(4,3), "5")
        self.key6 = Password(Point(5,3),"6")
        self.key7 = Password(Point(3,2),"7")
        self.key8 = Password(Point(4,2),"8")
        self.key9 = Password(Point(5,2),"9")
        
    def todraw(self, win):
        self.wall.draw(win)
        self.door.draw(win)
        self.text.draw(win)
        self.box.draw(win)
        self.boxText.draw(win)
        self.key1.todraw(win)
        self.key2.todraw(win)
        self.key3.todraw(win)
        self.key4.todraw(win)
        self.key5.todraw(win)
        self.key6.todraw(win)
        self.key7.todraw(win)
        self.key8.todraw(win)
        self.key9.todraw(win)

    def undraw(self):
        self.wall.undraw()
        self.door.undraw()
        self.text.undraw()
        self.box.undraw()
        self.boxText.undraw()
        self.key1.undraw()
        self.key2.undraw()
        self.key3.undraw()
        self.key4.undraw()
        self.key5.undraw()
        self.key6.undraw()
        self.key7.undraw()
        self.key8.undraw()
        self.key9.undraw()
        
    def getObject(self,p):
        None



class Room2(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Room 2")
        Objects.__init__(self)
        #background
        self.imgRoom2 = Image(Point(4, 3), "hospitalroom.gif")
        
    def todraw(self, win):
        self.imgRoom2.draw(win)
        #objects
            #tanquilizer
        if self.allObjects[1] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[1].draw(win)

    def undraw(self):
        self.imgRoom2.undraw()
            #tranquilizer
        if self.allObjects[1] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[1].undraw()

    def getObject(self,p):
            #tranquilizer
        if enterR(p,1.7,2.7,1.5,2.5):
            return self.allObjects[1]

class Room2Z(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Room 2")
        Objects.__init__(self)
        #background
        self.imgRoom2Z = Image(Point(4, 3), "room2Z2.gif")

        
    def todraw(self, win):
        self.imgRoom2Z.draw(win)
            #key2R3
        if self.allObjects[5] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[5].draw(win)
            #tranquilizer/stimulant
        if self.allObjects[9] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[9].draw(win)
        if self.allObjects[10] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[10].draw(win)



    def undraw(self):
        self.imgRoom2Z.undraw()
        self.allObjects[9].undraw()
        self.allObjects[10].undraw()
            #key2R3
        if self.allObjects[5] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[5].undraw()


    def getObject(self,p):
        #key2R3
        if enterR(p,3,5,0,1):
            return self.allObjects[5]


class Room3F(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Room 3")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("IndianRed4")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("steel blue")
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))
        self.door2hall = Rectangle(Point(1,1), Point(3,4))
        self.door2hall.setFill("gray")


    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)
        self.door2hall.draw(win)

    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()
        self.door2hall.undraw()

        
    def getObject(self,p):
        None

class Room3L(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Room 3")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("IndianRed4")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("steel blue")
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))


    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)


    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()


        
    def getObject(self,p):
        None

class Room3B(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Room 3")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("IndianRed4")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("steel blue")
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))
        self.imgCab = Image(Point(4, 1.5), "cabinet.gif")
        self.imgFam = Image(Point(3, 3), "familypic.gif")

    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)
        self.imgCab.draw(win)
        self.imgFam.draw(win)


    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()
        self.imgCab.undraw()
        self.imgFam.undraw()


        
    def getObject(self,p):
        None


class Room3R(BaseRoom, Objects):

    def __init__(self):
        BaseRoom.__init__(self, "Room 3")
        Objects.__init__(self)
        self.wall = Polygon(Point(0,0), Point(8,0), Point(8,6), Point(0,6))
        self.wall.setFill("IndianRed4")
        self.floor = Polygon(Point(0,0), Point(8,0), Point(7,1), Point(1,1))
        self.floor.setFill("steel blue")
        self.frontWall = Polygon(Point(1,1), Point(7,1), Point(7,6), Point(1,6))
        self.imgSofa = Image(Point(3.2, 1.34), "sofa.gif")

    def todraw(self, win):
        self.wall.draw(win)
        self.floor.draw(win)
        self.frontWall.draw(win)
        self.imgSofa.draw(win)
            #cellphone
        if self.allObjects[6] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[6].draw(win)



    def undraw(self):
        self.wall.undraw()
        self.floor.undraw()
        self.frontWall.undraw()
        self.imgSofa.undraw()
            #cellphone
        if self.allObjects[6] in self.noNeed2Draw:
            pass
        else:
            self.allObjects[6].undraw()


        
    def getObject(self,p):
            #cellphone
        if enterR(p,3.5,4.5,1.4,2.4):
            return self.allObjects[6]

class Room4(BaseRoom, Objects):
    def __init__(self):
        BaseRoom.__init__(self, "Room 4")
        Objects.__init__(self)
        #background
        self.imgRoom4 = Image(Point(4, 3), "laboratory.gif")
        self.imgBrain = Image(Point(2.7, 2.2), "brainicon.gif")
        
    def todraw(self, win):
        self.imgRoom4.draw(win)
        self.imgBrain.draw(win)

    def undraw(self):
        self.imgRoom4.undraw()
        self.imgBrain.undraw()


    def getObject(self,p):
        None


#------------------------------------------------------------
#motion
        
def enterR(p,leastX,greatestX,leastY,greatestY):
    if leastX <= p.getX() <= greatestX and leastY <= p.getY() <= greatestY:
        return True
    else:
        return False
            

#----------------------------------------------------------
#Gamepad


def game():
    #win
    win = GraphWin("",1100,600)
    win.setCoords(0.0, 0.0, 11.0, 6.0)
    #background
    sepLine = Line(Point(8, 0), Point(8, 6))
    sepLine.draw(win)
    arrowB = Rectangle(Point(8, 0), Point(11, 2))
    arrowB.setFill("lavender")
    arrowB.draw(win)
    #Indicator
    display = Text(Point(9,5.5), "")
    display.setSize(24)
    display.draw(win)

    #shelf
    shelf = Shelf()
    
    #buttons
    exit = SquareButton(win, 10.5, 5.5, 1, "red", "QUIT")
    uButton = ArrowButton(win, Point(9, 1), Point(10, 1), Point(9.5, 2),Point(9, 1), Point(10, 2),"cornsilk")
    lButton = ArrowButton(win, Point(8, .5), Point(9, 0), Point(9, 1), Point(8, 0), Point(9, 2),"cornsilk")
    rButton = ArrowButton(win, Point(10, 0), Point(11, .5), Point(10, 1), Point(10, 0), Point(11, 2),"cornsilk")
    dButton = ArrowButton(win, Point(9,1), Point(9.5, 0), Point(10, 1), Point(9, 0), Point(10, 1),"cornsilk")

    item1 = SquareButton(win, 8.5, 4.5, 1, "white", None)
    item2 = SquareButton(win, 9.5, 4.5, 1, "white", None)
    item3 = SquareButton(win, 10.5, 4.5, 1, "white", None)
    item4 = SquareButton(win, 8.5, 3.5, 1, "white", None)
    item5 = SquareButton(win, 9.5, 3.5, 1, "white", None)
    item6 = SquareButton(win, 10.5, 3.5, 1, "white", None)
    item7 = SquareButton(win, 8.5, 2.5, 1, "white", None)
    item8 = SquareButton(win, 9.5, 2.5, 1, "white", None)
    item9 = SquareButton(win, 10.5, 2.5, 1, "white", None)
    
    #set up rooms
    room1F = Room1F()
    room1B = Room1B()
    room1L = Room1L()
    room1R = Room1R()
    room1Rm = Room1Rm()
    hallF = HallF()
    hallR = HallR()
    hallL = HallL()
    hallZ = HallZ()
    room2 = Room2()
    room2Z = Room2Z()
    room3F = Room3F()
    room3L = Room3L()
    room3B = Room3B()
    room3R = Room3R()
    room4 = Room4()

    redR = RedR()
    blueR = BlueR()
    blackR = BlackR()
    
    
    #set up connections between rooms
    room1F.setDirections(None, None, room1L, room1R)
    room1L.setDirections(None, None, room1B, room1F)
    room1B.setDirections(None, None, room1R, room1L)
    room1R.setDirections(None, None, room1F, room1B)
    room1Rm.setDirections(None,room1R, room1R, room1R)
    hallF.setDirections(hallZ, room1B, hallL, hallR)
    hallR.setDirections(room2, hallF, hallF, hallF)
    hallL.setDirections(None, hallF, hallF, hallF)
    hallZ.setDirections(None, hallF, None, None)
    room2.setDirections(None, hallF, None, None)
    room2Z.setDirections(None, room2,None,None)
    room3F.setDirections(hallF, None, room3L, room3R)
    room3L.setDirections(None, None, room3B, room3F)
    room3B.setDirections(None, None, room3R, room3L)
    room3R.setDirections(None, None, room3F, room3B)
    room4.setDirections(None,hallF,None,None)

    redR.setDirections(None, None, None, None)
    blueR.setDirections(None, None, None, None)
    blackR.setDirections(None, None, None, None)
    
    #set up current location
    currentLocation = room1B
    currentLocation.todraw(win)

    #command
#    command = ""
    command = "wakeUp"
    
    #START LOOP
    while win.isClosed() == False:
    #--------------EXECUTE COMMAND-----------------
        if command != "":
            if command == "wakeUp" and currentLocation == room1B:
                shelf.updateText(win, "I woke up")
                shelf.updateText(win, "I don't know where I am.")
                shelf.updateText(win, "I don't remember anything...Ahh...Headache!")
                shelf.updateText(win, "I'd better start searching around (click again to continue)")
                command = ""
                
            elif command == "go2Hall" and currentLocation == room1F:
                currentLocation.undraw()
                currentLocation = hallF
                currentLocation.todraw(win)
                command = ""

            elif command == "go2Hall" and currentLocation == room3F:
                currentLocation.undraw()
                currentLocation = hallF
                currentLocation.todraw(win)
                command = ""
                
            elif command == "go2HallR":
                currentLocation.undraw()
                currentLocation = hallR
                currentLocation.todraw(win)
                command = ""
                
            elif command == "go2HallL":
                currentLocation.undraw()
                currentLocation = hallL
                currentLocation.todraw(win)
                command = ""

            elif command == "go2HallZ":
                currentLocation.undraw()
                currentLocation = hallZ
                currentLocation.todraw(win)
                command = ""

            elif command == "go2Room2" and currentLocation == hallR:
                currentLocation.imgOpenDoor.draw(win)
                time.sleep(.5)
                currentLocation.undraw()
                currentLocation.imgOpenDoor.undraw()
                currentLocation = room2
                currentLocation.todraw(win)
                command = ""

            elif command == "go2Room3" and currentLocation == hallL:
                currentLocation.imgOpenDoor.draw(win)
                time.sleep(.5)
                currentLocation.undraw()
                currentLocation.imgOpenDoor.undraw()
                currentLocation = room3B
                currentLocation.todraw(win)
                command = ""

            elif command == "go2Room4":
                currentLocation.undraw()
                currentLocation = room4
                currentLocation.todraw(win)
                command = ""

            elif command == "go2Room2Z":
                currentLocation.undraw()
                currentLocation = room2Z
                currentLocation.todraw(win)
                command = ""

                               
            elif command == "go2Room1Rm":
                currentLocation.undraw()
                currentLocation = room1Rm
                currentLocation.todraw(win)
                p = win.getMouse()
                shelf.updateText(win, "Who is this man? Me??")
                shelf.updateText(win, "I cannot believe I can't even recognize myself. What happend?")
                
                if shelf.allObjects[2] in shelf.checkin:
                    if shelf.decisionText(win, "Somehow I just hate to see this face...Use the cup to breake it? ") == "Y":
                        shelf.allObjects[2].undraw()
                        shelf.checkin[shelf.checkin.index(shelf.allObjects[2])] = False
                        room1R.imgMirror = Image(Point(5, 3.5), "mirrorSsh.gif")
                        currentLocation.undraw()
                        room1Rm.imgMirrorL = Image(Point(4, 3), "mirrorLsh.gif")
                        currentLocation = room1R
                        currentLocation.todraw(win)
                        room1L.noNeed2Draw.append(room1L.allObjects[2])
                        
                elif shelf.allObjects[3] in shelf.checkin:
                    if shelf.decisionText(win, "Somehow I just hate to see this face...Use the cup to breake it?") == "Y":
                        shelf.allObjects[3].undraw()
                        shelf.checkin[shelf.checkin.index(shelf.allObjects[3])] = False
                        room1R.imgMirror = Image(Point(5, 3.5), "mirrorSsh.gif")
                        currentLocation.undraw()
                        room1Rm.imgMirrorL = Image(Point(4, 3), "mirrorLsh.gif")
                        currentLocation = room1R
                        currentLocation.todraw(win)
                        
                #cup is used
                elif room1L.allObjects[2] in room1L.noNeed2Draw and shelf.allObjects[2] not in shelf.checkin:
                    #emptyCup is not present
                    if shelf.allObjects[3] not in shelf.checkin:
                        #doc1 Letter +Dear... Don't worry you'll live
                        shelf.allObjects[7].draw(win)
                        shelf.updateText(win, "A piece of paper hides behind the mirror...Let's read it.")
                        shelf.updateText(win, "'I know that I won't have much time.'")
                        shelf.updateText(win, "'They all cheat me that I'm gonna recover...Even Jane says so!'")
                        shelf.updateText(win, "'I know my body...It's gonna collapse.'")
                        shelf.updateText(win, "What does this mean??")
                        shelf.allObjects[7].undraw()
                        currentLocation.undraw()
                        currentLocation = room1R
                        currentLocation.todraw(win)

                command = ""

            elif command == "stimulant" and currentLocation == room2Z:
                shelf.allObjects[0].undraw()
                shelf.checkin[shelf.checkin.index(shelf.allObjects[0])] = False
                room1L.noNeed2Draw.append(room1L.allObjects[0])
                #redpill
                currentLocation.allObjects[9].draw(win)
                currentLocation.noNeed2Draw.remove(currentLocation.allObjects[9])
                if currentLocation.allObjects[5] in currentLocation.noNeed2Draw and shelf.allObjects[5] not in shelf.checkin:
                    if room2Z.allObjects[9] not in room2Z.noNeed2Draw and room2Z.allObjects[10] not in room2Z.noNeed2Draw:
                        currentLocation.noNeed2Draw.remove(currentLocation.allObjects[5])
                        currentLocation.undraw()
                        currentLocation = room2
                        currentLocation.todraw(win)
                        shelf.updateText(win, "Sound in the cabinet!")
                command = ""

            elif command == "tranquilizer" and currentLocation == room2Z:
                shelf.allObjects[1].undraw()
                shelf.checkin[shelf.checkin.index(shelf.allObjects[1])] = False
                room1L.noNeed2Draw.append(room2.allObjects[1])
                #redpill
                currentLocation.allObjects[10].draw(win)
                currentLocation.noNeed2Draw.remove(currentLocation.allObjects[10])
                if currentLocation.allObjects[5] in currentLocation.noNeed2Draw and shelf.allObjects[5] not in shelf.checkin:
                    if room2Z.allObjects[9] not in room2Z.noNeed2Draw and room2Z.allObjects[10] not in room2Z.noNeed2Draw:
                        currentLocation.noNeed2Draw.remove(currentLocation.allObjects[5])
                        currentLocation.undraw()
                        currentLocation = room2
                        currentLocation.todraw(win)
                        shelf.updateText(win, "Sound in the cabinet!")
                command = ""
                
            elif command == "spill" and currentLocation == room1B:
                #remove cup
                shelf.allObjects[2].undraw()
                shelf.checkin[shelf.checkin.index(shelf.allObjects[2])] = False
                room1L.noNeed2Draw.append(room1L.allObjects[2])
                #draw empty cup
                shelf.allObjects[3].draw(win)
                shelf.place(shelf.allObjects[3])
                currentLocation.spill(win)
                command = ""

            #ENDINGS+blackouts
            elif command == "end1":
                currentLocation.undraw()
                currentLocation = blackR
                currentLocation.todraw(win)
                shelf.updateText(win, "A woman picked call, and claimed to be my wife, Jane.")
                shelf.updateText(win, "I couldn't refute her because she showed me my photo ID.")
                shelf.updateText(win, "She told me that there was a car crush which caused my memory loss.")
                shelf.updateText(win, "I trusted her.")
                shelf.updateText(win, "NORMAL END")
                command = "finishGame"
                
            elif command == "end2":
                currentLocation.undraw()
                currentLocation = blackR
                currentLocation.todraw(win)
                shelf.updateText(win, "I called Mary, and she cried when hearing my voice...")
                shelf.updateText(win, "She said my disappearance blew her, and she thought I might be dead.")
                shelf.updateText(win, "I promised her I would be back.")
                shelf.updateText(win, "NORMAL END")
                command = "finishGame"

            elif command == "trueEnd":
                currentLocation.undraw()
                currentLocation = blueR
                currentLocation.todraw(win)
                shelf.updateText(win, "'I' survived in this body as 'experiment model,' but lost memory.")
                shelf.updateText(win, "'My body's' brain was perserved in that jar...'Jason' is dead.")
                shelf.updateText(win, "I would continue to use this body, and start my new life.")
                shelf.updateText(win, "TRUE END")
                command = "finishGame"

            elif command == "deadEnd":
                currentLocation.undraw()
                currentLocation = redR
                currentLocation.todraw(win)
                shelf.updateText(win, "DEAD END")
                command = "finishGame"

            elif command == "finishGame":
                currentLocation.undraw()
                currentLocation = blueR
                currentLocation.todraw(win)
                shelf.updateText(win, "Thanks for playing!")
                win.close()
                
            else:
                command = ""
        
                
                
    #--------------GET MOUSE------------------------
        else:
            p = win.getMouse()           
            #quit game
            if exit.contains(p) == True:
                exit.press()
                win.close()
                
            #move between rooms
            if uButton.contains(p) == True:
                uButton.press()
                if currentLocation.up != None:
                    currentLocation.undraw()
                    currentLocation = currentLocation.up
                    currentLocation.todraw(win)
                    
            elif lButton.contains(p) == True:
                lButton.press()
                if currentLocation.left != None:
                    currentLocation.undraw()
                    currentLocation = currentLocation.left
                    currentLocation.todraw(win)
                    
            elif dButton.contains(p) == True:
                dButton.press()
                if currentLocation.down != None:
                    currentLocation.undraw()
                    currentLocation = currentLocation.down
                    currentLocation.todraw(win)
                
            elif rButton.contains(p) == True:
                rButton.press()
                if currentLocation.right != None:
                    currentLocation.undraw()
                    currentLocation = currentLocation.right
                    currentLocation.todraw(win)
                    
            else:
                #-----------CONDITION TRIGGER

                #go to hallF
                if currentLocation == room3F and enterR(p,1,3,1,4) == True:
                    command = "go2Hall"

                #go hallR
                if currentLocation == hallF and enterR(p,6,7,2,4) == True:
                    command = "go2HallR"
                #go hallL
                if currentLocation == hallF and enterR(p,1,2,2,4) == True:
                    command = "go2HallL"
                #go hallZ
                if currentLocation == hallF and enterR(p,3,5,3,6) == True:
                    command = "go2HallZ"
                
                #go open the door in hallR enter room2
                if currentLocation == hallR and enterR(p,2.5,5.5,0,6) == True:
                    command = "go2Room2"

                #go to room2Z
                if currentLocation == room2 and enterR(p,3.8,5.2,4.3,5.5) == True:
                    command = "go2Room2Z"

                #go to room4
                if currentLocation == hallZ:
                    if currentLocation.key3.contains(p)==True:
                        currentLocation.key3.press()
                        currentLocation.boxText.setText("----")
                        p = win.getMouse()
                        if currentLocation.key5.contains(p)==True:
                            currentLocation.key5.press()
                            p = win.getMouse()
                            if currentLocation.key2.contains(p)==True:
                                currentLocation.key2.press()
                                p = win.getMouse()
                                if currentLocation.key1.contains(p)==True:
                                    currentLocation.key1.press()
                                    currentLocation.boxText.setText("PASS")
                                    time.sleep(.2)
                                    command = "go2Room4"
                    elif currentLocation.key1.contains(p)==True:
                        currentLocation.key1.press()
                        currentLocation.boxText.setText("----")
                    elif currentLocation.key2.contains(p)==True:
                        currentLocation.key2.press()
                        currentLocation.boxText.setText("----")                        
                    elif currentLocation.key4.contains(p)==True:
                        currentLocation.key4.press()
                        currentLocation.boxText.setText("----")
                    elif currentLocation.key5.contains(p)==True:
                        currentLocation.key5.press()
                        currentLocation.boxText.setText("----")
                    elif currentLocation.key6.contains(p)==True:
                        currentLocation.key6.press()
                        currentLocation.boxText.setText("----")                        
                    elif currentLocation.key7.contains(p)==True:
                        currentLocation.key7.press()
                        currentLocation.boxText.setText("----")
                    elif currentLocation.key8.contains(p)==True:
                        currentLocation.key8.press()
                        currentLocation.boxText.setText("----")
                    elif currentLocation.key9.contains(p)==True:
                        currentLocation.key9.press()
                        currentLocation.boxText.setText("----")                        
                               

                #telephone
                if currentLocation == room2 and enterR(p, 4.2, 4.8, 2.1, 2.5) == True:
                    if shelf.allObjects[8] in shelf.noNeed2Draw:
                        if shelf.decisionText(win, "Call the relative's number on the medical paper?") == "Y":
                            command = "end1"
                    else:
                        shelf.updateText(win, "A telephone.")

                #Key2R2 mirror trigger + make key appear
                if currentLocation == room1R and enterR(p, 4, 6, 2.75, 4.5) == True:
                    command = "go2Room1Rm"
                    #key is not present
                    if currentLocation.allObjects[4] in currentLocation.noNeed2Draw and shelf.allObjects[4] not in shelf.checkin:
                        #cup is used
                        if room1L.allObjects[2] in room1L.noNeed2Draw and shelf.allObjects[2] not in shelf.checkin:
                            #emptyCup is not present
                            if shelf.allObjects[3] not in shelf.checkin:
                                currentLocation.noNeed2Draw.remove(currentLocation.allObjects[4])


                #brain->trueEnd
                if currentLocation == room4 and enterR(p, 2.2, 2.8, 1.7, 2.7):
                    if shelf.allObjects[12] in shelf.noNeed2Draw:
                        shelf.allObjects[13].draw(win)
                        shelf.updateText(win, "......")
                        if shelf.decisionText(win,"Is this my brain?") == "Y":
                            command = "end2"
                        else:
                            command = "trueEnd"
                    else:
                        shelf.updateText(win, "A jar...of brain...")

                #----------------COMMENTS
                #Locked door in room1
                if currentLocation == room1F and enterR(p,5,7,1,4) == True:
                    if shelf.allObjects[4] in shelf.checkin:
                        shelf.updateText(win, "Use key to unlock")
                    else:
                        shelf.updateText(win, "Door is locked")

                #Locked door in HallL
                if currentLocation == hallL and enterR(p,2.5,5.5,0,6) == True:
                    if shelf.allObjects[5] in shelf.checkin:
                        shelf.updateText(win, "Use key to unlock")
                    else:
                        shelf.updateText(win, "Door is locked")
                        
                #patch
                if currentLocation == room1B and enterR(p, 4, 6, 4, 5) == True:
                    if shelf.allObjects[2] in shelf.checkin:
                        shelf.updateText(win, "powder on the wall seems like can be dissolved...")
                    elif shelf.allObjects[2] in room1L.noNeed2Draw:
                        shelf.updateText(win, "What does that mean?")
                    else:
                        shelf.updateText(win, "Why is here colored? It feels soft...Oops, some dregs fall.")

                #bed
                if currentLocation == room1B and enterR(p, .5, 6.5, 0, 1.59) == True:
                    shelf.updateText(win, "Where I woke up. This bed looks very new.")

                #sofa
                if currentLocation == room3R and enterR(p, .5, 6, 0, 3) == True:
                    shelf.updateText(win, "Sofa...a good place to rest.")


                #table
                if currentLocation == room1L and enterR(p, .5, 4.5, 0, 2.39) == True:
                    shelf.updateText(win, "A table. Nothing special.")

                #doc2 medical history +th patient +weak,legs cannot walk +requires stimulant to keep awake
                if currentLocation == room2 and enterR(p,2.4,4.2,1,2) == True:
                    shelf.allObjects[8].draw(win)
                    shelf.updateText(win, "A sheet of medical history...the photo is absent")
                    shelf.updateText(win, "'Leonard...28...necrotic leg ulcer...loss of walking ability'")
                    shelf.updateText(win, "'Chronic dehydration...Constant depression'")
                    shelf.updateText(win,"'...requires stimulant to keep consciousness.'")
                    shelf.updateText(win, "'All conditions fulfilled...Consider to be 5th case.'")
                    shelf.updateText(win, "Why is the photo not here? Am I the patient...?")
                    shelf.updateText(win, "It can't be me...My legs are perfectly fine!...What does 5th case mean...?")
                    shelf.allObjects[8].undraw()
                    shelf.noNeed2Draw.append(shelf.allObjects[8])

                #doc3 diary  +Mary+athletics identity NO.1
                if currentLocation == room3B and enterR(p,2,6,.5,2.4) == True:
                    if currentLocation.imgFam in currentLocation.noNeed2Draw:
                        shelf.allObjects[11].draw(win)
                        shelf.updateText(win, "Find a diary!")
                        shelf.updateText(win, "'...Jason.S.Siemon, 2nd place in this track& field meet.'")
                        shelf.updateText(win,"' Mary said she was proud of me. Won't lose again!'")
                        shelf.updateText(win, "'I need to find some places for special training next month...'")                    
                        shelf.updateText(win, "Doesn't feel like me...")
                        shelf.updateText(win,"but according to the picture, is my name Jason? Am I the one wrote this diary?")
                        shelf.allObjects[11].undraw()
                        shelf.noNeed2Draw.append(shelf.allObjects[11])
                    else:
                        shelf.updateText(win, "A cabinet, but something else catches my attention...")

                #doc4 labs  +brain exchange
                if currentLocation == room4 and enterR(p,2.7,4.8,.3,2) == True:
                        shelf.allObjects[12].draw(win)
                        shelf.updateText(win, "Find a pile of documents! It has a photo...very familiar...")
                        shelf.updateText(win, "'Case 5 (L&J): serious rejections happend after implantation'")
                        shelf.updateText(win, "'major surgery revision needed.'")
                        shelf.updateText(win, "'...The body passed danger period'")
                        shelf.updateText(win, "'Observation report to be continued...report from AACCGTTGATCCGCT BASE'")
                        shelf.updateText(win, "...So my real identity is...")
                        shelf.allObjects[12].undraw()
                        shelf.noNeed2Draw.append(shelf.allObjects[12])





                #doll...
                if currentLocation == room2Z and enterR(p, 0, 2, 0, 6) == True:
                    shelf.updateText(win, "This face seems maniac")
                if currentLocation == room2Z and enterR(p, 6, 8, 0, 6) == True:
                    shelf.updateText(win, "This face seems sad")

                #family
                if currentLocation == room3B and enterR(p, 2.5, 3.5, 2.5, 3.5) == True:
                    shelf.updateText(win, "A family picture. Seems like this man is with his wife and 2 children.")
                    shelf.updateText(win, "The man looks exactly like my reflection in the mirror...")
                    shelf.updateText(win,"But I have no idea about the other 3 people in the picture.")
                    #only as a condition trigger/not affecting drawing
                    currentLocation.noNeed2Draw.append(currentLocation.imgFam)
                   
                #-------------OBJECT PICK UP
                obj = currentLocation.getObject(p)
                    #stimulant
                if obj == currentLocation.allObjects[0]:
                    shelf.allObjects[0] = obj
                    if obj not in currentLocation.noNeed2Draw:
                        shelf.updateText(win, "Got stimulant. What am I suppose to do? I don't feel take it.")
                        shelf.place(obj)
                        currentLocation.noNeed2Draw.append(obj)
                    #tanquilizer
                elif obj == currentLocation.allObjects[1]:
                    shelf.allObjects[1] = obj
                    if obj not in currentLocation.noNeed2Draw:
                        shelf.updateText(win, "Got tranquilizer. What am I suppose to do? I don't feel take it.")
                        shelf.place(obj)
                        currentLocation.noNeed2Draw.append(obj)
                    #cup
                elif obj == currentLocation.allObjects[2]:
                    shelf.allObjects[2] = obj
                    if obj not in currentLocation.noNeed2Draw:
                        shelf.updateText(win, "Got cup. Ew, the coffee-like liquid stinks.")
                        shelf.place(obj)
                        currentLocation.noNeed2Draw.append(obj)
                    #key2H
                elif obj == currentLocation.allObjects[4]:
                    shelf.allObjects[4] = obj
                    if obj not in currentLocation.noNeed2Draw:
                        shelf.updateText(win, "A key is hinding behind...")
                        shelf.place(obj)
                        currentLocation.noNeed2Draw.append(obj)
                    #key2R3
                elif obj == currentLocation.allObjects[5]:
                    shelf.allObjects[5] = obj
                    if obj not in currentLocation.noNeed2Draw:
                        shelf.updateText(win, "Got the key!")
                        shelf.place(obj)
                        currentLocation.noNeed2Draw.append(obj)
                    #cellphone
                elif obj == currentLocation.allObjects[6]:
                    shelf.allObjects[6] = obj
                    if obj not in currentLocation.noNeed2Draw:
                        shelf.updateText(win, "Someone's phone...still powers on.")
                        shelf.place(obj)
                        currentLocation.noNeed2Draw.append(obj)
                else:
                    #----------------PICK ITEMS FROM GRID
                    #press button->to use:check obj(match)/loc/next getMouse
                    if item1.contains(p)==True:
                        item1.press()
                        command = shelf.match(win,0)
                    elif item2.contains(p)==True:
                        item2.press()
                        command = shelf.match(win,1)
                    elif item3.contains(p)==True:
                        item3.press()
                        command = shelf.match(win,2)
                    elif item4.contains(p)==True:
                        item4.press()
                        command = shelf.match(win,3)
                    elif item5.contains(p)==True:
                        item5.press()
                        command = shelf.match(win,4)
                    elif item6.contains(p)==True:
                        item6.press()
                        command = shelf.match(win,5)
                    elif item7.contains(p)==True:
                        item7.press()
                        command = shelf.match(win,6)
                    elif item8.contains(p)==True:
                        item8.press()
                        command = shelf.match(win,7)
                    elif item9.contains(p)==True:
                        item9.press()
                        command = shelf.match(win,8)


        
        #update location in the indicator
        display.setText(currentLocation)


game()