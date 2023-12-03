import random
from klasy import Stop, Line, User, Tram

stop0 = Stop()
stop1 = Stop()
stop2 = Stop()

line = Line([stop0, stop1, stop2])

tram = Tram(line)

users = [User() for _ in range(10)]

for user in users:

    userStop = random.randint(0, 2)
    user.destination = userStop
    
    while user.destination == userStop: 
        user.destination = random.randint(0, 2)
    
    if userStop == 0:
        stop0.addUser(user)

        
    elif userStop == 1:
        stop1.addUser(user)
        
    else:
        stop2.addUser(user)


stop0.printAmountOfUsers()
stop1.printAmountOfUsers()
stop2.printAmountOfUsers()
print("\n")

for i in range(2*len(line.stops)-1):
    
    tram.go()
    print("Tramwaj na przystanku:",tram.position)
    currentStop = line.stops[tram.position]
    

    leftUsers = []
    
    for user in currentStop.users:

        if user.isDirection(tram.direction, tram.position):
            tram.addUser(user)
            leftUsers.append(user)

    for user in leftUsers:
        currentStop.removeUser(user)


    leftUsers = []

    for user in tram.users:

        if user.destination == tram.position:
            leftUsers.append(user)

    for user in leftUsers:
        tram.removeUser(user)
            
    
    print("ludzi w tramwaju:",len(tram.users), "\n")

    stop0.printAmountOfUsers()
    stop1.printAmountOfUsers()
    stop2.printAmountOfUsers()
    print("\n")


    

