import pygame
from road import Road






class Game:
    pygame.init()

    def __init__(self):
        self.display = pygame.display.set_mode((700,400))
        self.name = pygame.display.set_caption("Dino")
        self.color_display = (255,255,255)
        self.road = Road()


    def game_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            self.display.fill(self.color_display)
            pygame.display.update()
            
    
    
game = Game()
game.game_loop()