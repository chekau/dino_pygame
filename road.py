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
        self.spawn_timer += 1
        if self.spawn_timer >= 60:  # Увеличьте интервал до 60 кадров
            self.add_obstacle()
            self.spawn_timer = 0

    # Используйте новый список для удаления кактусов
        active_cacti = []
        for cactus in self.obstacles:
            cactus.move()  # Движение каждого кактуса
        # Проверка выхода за границы
            if cactus.rect.x >= -cactus.rect.width:
                active_cacti.append(cactus)  # Только те, что еще на экране
            else:
                self.score += 1  # Увеличение счёта для убранных кактусов

        self.obstacles = active_cacti  # Обновите список кактусов

    def closer_obstancle():
        ...