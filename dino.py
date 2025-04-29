import pygame



class Dino:

    def __init__(self):
        self.dino_image = pygame.image.load(r"static/dino.png")
        self.image = pygame.transform.scale(self.dino_image,(70,70))
        self.img_rect = self.image.get_rect()
        self.img_rect.x = 50
        self.img_rect.y = 250
    
        self.is_jumping = False
        self.y_velocity = 0
        

    def jump(self):
        if not self.is_jumping:
            self.y_velocity = -10  
            self.is_jumping = True


    def update(self):
        if self.is_jumping:
            self.img_rect.y += self.y_velocity
            self.y_velocity += 0.3

            
            if self.img_rect.y >=  250:  
                self.img_rect.y = 250
                self.is_jumping = False

    def crash():
        ...
    def position():
        ...