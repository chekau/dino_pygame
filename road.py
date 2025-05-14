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
            self.display_game_over()
            return
        
        
        self.spawn_timer += 1
        if self.spawn_timer >= 100:  
            self.add_obstacle()
            self.spawn_timer = 0

    
        active_cacti = []
        for cactus in self.obstacles:
            cactus.move()

            if self.check_colision():
                self.dino.crash()
                

            
        
            if cactus.rect.x >= -cactus.rect.width:
                active_cacti.append(cactus) 
            else:
                self.dino.score_succes_jump += 1 

        self.obstacles = active_cacti
         

    def check_colision(self):
        return self.dino.get_rect().colliderect(self.obstancle.get_rect())
    
    def display_game_over(self):
        self.screen.fill((255, 0, 0))
        game_over_text = self.font.render("Игра Окончена!", True, (255, 255, 255))
        self.screen.blit(game_over_text, (200, 180))
        pygame.display.flip()

    def closer_obstancle():
        ...