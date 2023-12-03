class Stop:
    def __init__(self):
        self.users = []

    def printAmountOfUsers(self):
        print(len(self.users))

    def amountOfUsers(self):
        return len(self.users)

    def addUser(self, User):
        self.users.append(User)

    def removeUser(self, User):
        self.users.remove(User)

class Line:
    def __init__(self, stops):
        self.stops = stops

class User:
    destination = 0

    def __str__(self):

        print("destination =", self.destination)

    def isDirection(self, direction, currentStop):

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
    
class Tram:
    def __init__(self, line):
        self.line = line
        self.position = -1
        self.direction = 1
        self.users = []

    def go(self):

        self.position += self.direction
        
        if self.direction == 1:
            if self.position == len(self.line.stops)-1:
                self.direction = -1

        else:
            if self.position == 0:
                self.direction = 1
            
        

    def addUser(self, User):
        self.users.append(User)

    def removeUser(self, User):
        self.users.remove(User)

