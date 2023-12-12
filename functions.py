from classes import Stop, Line, User, Tram, Symulation

import pygame
from sys import exit

def stopsFromLine(line):

    stopsxy = []
    for stop in line.stops:
        stopsxy.append([stop.xy[0],stop.xy[1]])

    return stopsxy

def listOfStopsFromLine(lines):
    stopsxy = []
    for line in lines:
        stopsxy.append(stopsFromLine(line))
    return stopsxy

def draw_stops(stop_positions, screen = pygame.display.set_mode((1400,750))):
    ## stop_positions <- pary xy
    
    for i, pos in enumerate(stop_positions):
        pygame.draw.circle(screen, 'Blue', pos, 8)
        if i < len(stop_positions) - 1:
            pygame.draw.line(screen, 'Blue', stop_positions[i], stop_positions[i + 1], 2)
        

def addStopsInscriptions(stops, screen=pygame.display.set_mode((1400, 750))):
    font = pygame.font.Font(None, 24)  # Ustawienie czcionki

    for stop in stops:
        x = stop.xy[0]
        y = stop.xy[1]
        text = str(str(stop.name) + " users:" + str(len(stop.users)))
        text = font.render(text, True, 'Black')  # Tekst zawierający numer stopu
        screen.blit(text, (x + 15, y - 15))  # Umieszczenie tekstu obok każdego stopu


def draw_tram(tramPosition, users, screen = pygame.display.set_mode((1400,750)), color='Red'):
    width = 50
    height = 20
    newTramPosition = [tramPosition[0] - width/2, tramPosition[1] - height/2]
    
    tram = pygame.Surface([width, height])
    tram.fill(color)
    screen.blit(tram, newTramPosition)

    font = pygame.font.Font(None, 24)  # Ustawienie czcionki
    text = str(users)
    text = font.render(text, True, 'Black')  # Tekst zawierający numer stopu
    screen.blit(text, tramPosition)  # Umieszczenie tekstu obok każdego stopu

def addDeliveredInformation(symulation, screen=pygame.display.set_mode((1400, 750))):
    font = pygame.font.Font(None, 24)  # Ustawienie czcionki
    
    text = str(symulation.deliveredUsers)
    text = font.render(text, True, 'Black')  # Tekst zawierający numer stopu
    screen.blit(text, (1300, 100))  # Umieszczenie tekstu obok każdego stopu

def playSym(symulation, goFor=0):

    stopxy = listOfStopsFromLine(symulation.lines)

    if goFor == 0:
        maxPatch = maxP(symulation.lines)
        goFor = 2*maxPatch

    pygame.init()
    screen = pygame.display.set_mode((1400,750))
    pygame.display.set_caption("TRAMSYM")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 15)
    
    for _ in range(goFor):
        screen.fill('White')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()   
        
        for line in stopxy:        
            draw_stops(line)

        addStopsInscriptions(symulation.stops)
        
        for tram in symulation.trams:

            draw_tram(tram.getTramXY(), len(tram.users))
        
        addDeliveredInformation(symulation)
        
        symulation.symGo()

        pygame.time.delay(300)   
        pygame.display.update()
        clock.tick(60)
    pygame.time.delay(3000) 

def maxP(lines):
    maxPatch = len(lines[0].stops)
    for line in lines:
        if len(line.stops) > maxPatch:
            maxPatch = len(line.stops)
    return maxPatch