from loadFromTxt import readMap
filename = "mapa1.txt"

import random

class Stop:
    def __init__(self, name="", xy=[0,0]):
        self.name = name
        self.xy = xy
        self.users = []

    def printAmountOfUsers(self):
        print(len(self.users))

    def amountOfUsers(self):
        return len(self.users)

    def addUser(self, User):
        self.users.append(User)

    def removeUser(self, User):
        try:self.users.remove(User)
        except:pass

class Line:
    def __init__(self, nr=0, stops=None):
        self.nr = nr
        if stops == None:
            self.stops = []
        else: self.stops = stops
        self.amountOfStops = len(self.stops)

    def addStop(self, stop):
        self.stops.append(stop)
        self.amountOfStops +=1
       
class User:
    def __init__(self, line=None, currentPosition=0, destination=0):
        self.line = line
        self.currentPosition = currentPosition 
        self.destination = destination    

    def __str__(self):
        return str("User on line: " + str(self.line.nr) + ", currentPosition: " + str(self.currentPosition) + ", destination: " + str(self.destination))
              

    def isDirection(self, currentStop, direction):

        if (self.destination - currentStop) > 0:

            if direction == 1:
                return True
            
            else:
                return False

        else:

            if direction == -1:
                return True
            
            else:
                return False
            
    def delivered(self):
        self.currentPosition = -1 
        self.destination = -1
        
    def putOnTram(self, tram):
        self.line.stops[self.currentPosition].removeUser(self)
        self.currentPosition = tram.position

class Tram:
    def __init__(self, line, position=-1, direction=1, users=None):
        self.line = line
        self.position = position
        self.direction = direction

        if users == None:
            self.users = []
        else: self.users = users
        

        if -1 < (position + direction) and (position + direction) < (self.line.amountOfStops +1):
            self.nextPosition = (position + direction)
        else: self.nextPosition = position

        if position >= 0: self.stop = self.line.stops[position]
        else: self.stop=self.line.stops[0] 
        

    def updateNextPosition(self):
        
        if(0 <= (self.position + self.direction) and (self.position + self.direction) < (self.line.amountOfStops)):
            pass        
        else: self.changeDirection()

        self.nextPosition = (self.position + self.direction)
        
    def changeDirection(self):
        self.direction *=(-1)

    def onStop(self):
        if self.position > -1:
            self.stop = self.line.stops[self.position]

        else: self.stop = None
    
    def go(self):
        self.position = self.nextPosition
        
        self.updateNextPosition()
        self.onStop()
        
    def getTramXY(self):
        if self.position == -1: return [0,0]
        
        return (self.line.stops[self.position].xy)
    
    def letInUsers(self):
        currentStop = self.line.stops[self.position]
        for user in currentStop.users:
            if user.isDirection(self.position, self.direction):
                self.addUser(user)
                user.putOnTram(self)
            else: 
                pass

    def letOutUsers(self):
        currentStop = self.line.stops[self.position]
        for user in self.users:
            if user.destination == self.position:
                user.delivered()
                self.removeUser(user)
            else: 
                pass
        

    def addUser(self, User):
        self.users.append(User)

    def removeUser(self, User):
        self.users.remove(User)

class Symulation:
    def __init__(self, lines=[], stops=[], users=[], trams=[]):
        self.lines = lines
        self.stops = stops
        self.users = users
        self.trams = trams

        self.deliveredUsers = 0

    def createBasicSym(self):
        self.createMapFromTxt(filename=filename)

    def createTestSym(self):
        
        self.createMapFromTxt(filename="mapasimple.txt")

        self.createTram(line=self.lines[0], position=0)
        self.createTram(line=self.lines[1], position=0)

    def createTest1Sym(self):
        
        self.createMapFromTxt(filename="mapasimple.txt")

        self.createTram(line=self.lines[0], position=0)
        self.createTram(line=self.lines[1], position=0)

        for _ in range(100):
            self.randomUser()

    def symGo(self):
        for tram in self.trams:
            
            self.letOutUsers(tram)
            self.letInUsers(tram)

            tram.go()

    def goForXTimes(self, x):
        for _ in range(x):
            self.symGo() 
        

    def createMapFromTxt(self, filename):
        listMap = readMap(filename)
        for indexLine, line in enumerate(listMap):
            for index, element in enumerate(line):

                if index == 0:
                    self.createLine(nr=int(element))
                    continue
                
                self.createStop(element[0], [int(element[1]) * 30, int(element[2]) * 30])
                stopIndex = self.searchStop(element[0], [int(element[1]) * 30, int(element[2]) * 30])

                self.addStopToLine(self.lines[indexLine], self.stops[stopIndex])
            

    def createLine(self, nr=0, stops=[]):
        line = Line(nr, *stops)
        self.lines.append(line)

    def addStopToLine(self, line, stop):
        line.addStop(stop)


    def createStop(self, name="", xy=[0,0]):
        if not (self.searchStop(name, xy)):
            stop = Stop(name, xy)
            self.stops.append(stop)

    def searchStop(self, name, xy):
        for i, stop in enumerate(self.stops):
            if stop.name == name and stop.xy == xy: return i

        return False

        
    def createUser(self, line=None, currentPosition=0, destination=0):
        user = User(line, currentPosition, destination)
        self.users.append(user) 

        line.stops[currentPosition].users.append(user)

    def randomUser(self, line=None, currentPosition=None, destination=None):
        if line == None:
            line = random.randint(0, len(self.lines)-1)

        if currentPosition == None:
            currentPosition = random.randint(0, len(self.lines[line].stops)-1)
            
        if destination == None:
            while destination == None or destination == currentPosition:
                destination = random.randint(0, len(self.lines[line].stops)-1)
        
        self.createUser(line=self.lines[line], currentPosition=currentPosition, destination=destination)

    def userDelivered(self, user):
        user.delivered()
        self.deliveredUsers += 1

    def letInUsers(self, tram):
        
        usersToAdd = []
        currentStop = tram.line.stops[tram.position]

        #print("Ludzie na przystanku:", len(currentStop.users))

        for user in currentStop.users:
            if user.isDirection(tram.position, tram.direction) and user.line == tram.line:
                usersToAdd.append(user)
            else: 
                pass

        for user in usersToAdd:
            #print("in")
            tram.addUser(user)
            user.putOnTram(tram)

    def letOutUsers(self, tram):
        
        usersToRemove = []
        
        for user in tram.users:
            
            if user.destination == tram.position:
                self.userDelivered(user)
                usersToRemove.append(user)
                
            else: 
                pass
        for user in usersToRemove:
            #print("out")
            tram.removeUser(user)

    def printUsers(self):
        for user in self.users:
            print(user)


    def createTram(self, line, position=-1, direction=1, users=None):
        tram = Tram(line, position, direction, users)
        self.trams.append(tram)

    







        
    
