import pygame
import sys
from obstacle import Obstancle
from dino import  Dino

class Road:
    def __init__(self):
        self.road_image = pygame.image.load(r"static\road.png")
        self.image = pygame.transform.scale(self.road_image,(1500,400))
        self.obstancle = Obstancle()
        self.dino = Dino()
        
        


    
    def add_obstancle(self):
        if self.obstancle.rect.x == 0:
            self.obstancle.rect.x = 600


    def closer_obstancle():
        ...