import pygame
from pygame.time import Clock 
from road import Road






class Game:
    pygame.init()

    def __init__(self):
        self.running = True
        self.display = pygame.display.set_mode((700,400))
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
        self.road.obstancle.move()
        self.road.add_obstancle()
        self.road.dino.jump()
        

    def render(self):
        self.display.fill(self.color_display)
        self.display.blit(self.road.image,(-150,120))
        self.display.blit(self.road.obstancle.image,(self.road.obstancle.rect.x,
                                                     self.road.obstancle.rect.y))
        self.display.blit(self.road.dino.img_rect,(50,250))
        
        
        pygame.display.flip()
        self.clock.tick(self.fps)
        pygame.display.update()
         


    def game_loop(self):
        while self.running:
            self.process_input()
            self.update_game()
            self.render()
            
        pygame.quit()

              

    
    
game = Game()
game.game_loop()