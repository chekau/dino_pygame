import pygame

class Obstancle:

    def __init__(self):
        self.obst_image = pygame.image.load(r"static\obstancle.png")
        self.image = pygame.transform.scale(self.obst_image,(700,70))
        # self.rect = self.image.get_rect()
        # self.rect.x = 100
        # self.rect.y = 100
        # self.speed = 2
        

    def move(self):
        self.rect.x -= self.speed
        
    def position(self):
        ...