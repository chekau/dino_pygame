import pygame
from pygame.time import Clock 
from road import Road
import random






class Game:
    pygame.init()

    def __init__(self):
        self.running = True
        self.display = pygame.display.set_mode((1000,400))
        self.name = pygame.display.set_caption("Dino")
        self.color_display = (255,255,255)
        self.clock = Clock()
        self.fps = 60
        self.road = Road()



    def process_input(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.road.dino.jump()

    def update_game(self):
        self.road.dino.update()
        self.road.update()
        
            
        
        
        
        
    def crash():
        ...
        
    
        

    def render(self):
        self.display.fill(self.color_display)
        self.display.blit(self.road.image,(-150,120))
        
        for obstacle in self.road.obstacles:  # Отрисовка всех препятствий
            self.display.blit(obstacle.image, (obstacle.rect.x, obstacle.rect.y))

        self.display.blit(self.road.dino.image,(self.road.dino.img_rect.x,
                                                   self.road.dino.img_rect.y))
        
        
        pygame.display.flip()
        
        
        
         


    def game_loop(self):
        while self.running:
            self.process_input()
            self.update_game()
            self.render()
            self.clock.tick(self.fps)
        pygame.quit()

              

    
    
game = Game()
game.game_loop()