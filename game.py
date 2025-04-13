import pygame,road


display = pygame.display.set_mode((700,400))
name = pygame.display.set_caption("Dino")


class Game:
    def __init__(self):
        ...
    

    def road(self):
        self.road = road.Road()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

        display.fill((255,255,255))
        pygame.display.update()
            
if __name__ == "__main__":
    main()