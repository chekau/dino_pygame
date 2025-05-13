import pygame

class Obstancle:

    def __init__(self):
        self.obst_image = pygame.image.load(r"static\obstacle.png")
        self.image = pygame.transform.scale(self.obst_image,(100,70))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 250
        self.speed = 6
        

    def move(self):
        self.rect.x -= self.speed
        
        
    def position(self):
        ...