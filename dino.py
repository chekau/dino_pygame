import pygame



class Dino:

    def __init__(self):
        self.dino_image = pygame.image.load(r"static/dino.png")
        self.image = pygame.transform.scale(self.dino_image,(70,70))
        self.img_rect = self.image.get_rect()
        self.img_rect.x = 50
        self.img_rect.y = 250
        self.vert_vel = 0
        self.gravity = 1
        self.is_jump = False
        self.jump_max = 15
        self.jump_count = 0

    def jump(self):
        self.is_jump = True
        self.jump_count = self.jump_max

        if self.is_jump:
            self.img_rect.y -= self.jump_count
            if self.jump_count > -self.jump_max:
                self.jump_count -= 1
            else:
                self.is_jump = False 
        

    def crash():
        ...
    def position():
        ...