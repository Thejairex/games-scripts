import pygame

class State():
    def __init__(self, width, height, size) -> None:
        self.size = size
        self.rect = pygame.Rect(25, 25, width, height)
    
    def draw(self, screen: pygame.Surface):
        return pygame.draw.rect(screen, self.color, self.rect)
    
class Poison(State):
    def __init__(self, width: int, height: int, size: tuple) -> None:
        super().__init__(width, height, size)
        
        self.color = (0, 180, 0)
        self.state = "veneno"
        self.duration = 3 #seconds
        self.dagame = 1

class Burn(State):
    def __init__(self, width: int, height: int, size: tuple) -> None:
            super().__init__(width, height, size)
            self.rect.x = 35 
            self.rect.y = 35
            self.color = (0, 180, 0)
            self.state = "quemado"
            self.dagame = 1
            