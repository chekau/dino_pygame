import pygame
import sys
from obstacle import Obstancle
from dino import  Dino
import random
import os


class Road:
    def __init__(self):
        self.road_image = pygame.image.load("static/road.png")
        self.image = pygame.transform.scale(self.road_image,(1500,400))
        self.obstancle = Obstancle()
        self.dino = Dino()
        self.obstacles = []
        self.spawn_timer = 0
        self.score = 0
        self.high_score = self.load_high_score()
        
    def add_obstacle(self):
        new_obstacle = Obstancle()
        self.obstacles.append(new_obstacle)

    def update(self):
        if not self.dino.alive:
            self.check_high_score()
            # self.display_game_over()
            return
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
        padding = 10
        return dino.get_rect().colliderect(obstancle.get_rect().inflate(-padding,-padding))
    
    def closer_obstancle():
        ...

    def check_high_score(self):
        if self.dino.score_succes_jump > self.high_score:
            self.high_score = self.dino.score_succes_jump
            self.save_high_score()

    def load_high_score(self):
        
        if os.path.exists("record.txt"):
            with open("record.txt", "r") as file:
                return int(file.read())
        return 0

    def save_high_score(self):
        with open("record.txt", "w") as file:
            file.write(str(self.high_score))

    