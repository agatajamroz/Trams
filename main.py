import random
import pygame
from sys import exit
from classes import Stop, Line, User, Tram, Symulation
from functions import listOfStopsFromLine, draw_stops, draw_tram, addStopsInscriptions, maxP, playSym

symulation = Symulation()
symulation.createTest1Sym()

playSym(symulation)