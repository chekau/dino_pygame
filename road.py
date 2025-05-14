import pygame
import sys
from obstacle import Obstancle
from dino import  Dino
import random

class Road:
    def __init__(self):
        self.road_image = pygame.image.load(r"static\road.png")
        self.image = pygame.transform.scale(self.road_image,(1500,400))
        self.obstancle = Obstancle()
        self.dino = Dino()

        self.obstacles = []
        self.spawn_timer = 0
        self.score = 0

        

        
        
    def add_obstacle(self):
        new_obstacle = Obstancle()
        self.obstacles.append(new_obstacle)

    def update(self):
        if not self.dino.alive:
            # self.display_game_over()
            pygame.quit()
        
        
        self.spawn_timer += 1
        if self.spawn_timer >= 100:  
            self.add_obstacle()
            self.spawn_timer = 0

    
        active_cacti = []
        for cactus in self.obstacles:
            cactus.move()

            if self.check_colision(self.dino,cactus):

                self.dino.crash()
                break
                

            
        
            if cactus.rect.x >= -cactus.rect.width:
                active_cacti.append(cactus) 
            else:
                self.dino.score_succes_jump += 1 

        self.obstacles = active_cacti
         

    def check_colision(self,dino,obstancle):
        return dino.get_rect().colliderect(obstancle.get_rect())
    
    

    def closer_obstancle():
        ...