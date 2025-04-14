import pygame
from road import Road






class Game:
    pygame.init()

    def __init__(self):
        self.running = True
        self.display = pygame.display.set_mode((700,400))
        self.name = pygame.display.set_caption("Dino")
        self.color_display = (255,255,255)
        self.road = Road()


    def process_input(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

    def update_game(self):
         ...

    def render(self):
        self.display.fill(self.color_display)
        self.display.blit(self.road.image,(-100,300))
        pygame.display.update()
         


    def game_loop(self):
        while self.running:
            self.process_input()
            self.update_game()
            self.render()
            
        pygame.quit()

              
        
        
           

            
    
    
game = Game()
game.game_loop()