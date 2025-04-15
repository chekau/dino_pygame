import pygame
import sys
from obstacle import Obstancle

class Road:
    def __init__(self):
        self.road_image = pygame.image.load(r"static\road.png")
        self.image = pygame.transform.scale(self.road_image,(1000,150))
        self.obstancle = Obstancle()
        
        


    
    def add_obstancle():
        ...
    def closer_obstancle():
        ...