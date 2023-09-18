import pygame
from entities.player import Player
from utils.logic import Logic

class State():
    def __init__(self, width, height, size) -> None:
        self.size = size
        self.rect = pygame.Rect(25, 25, width, height)
        self.logic  = Logic()

    def draw(self, screen: pygame.Surface):
        return pygame.draw.rect(screen, self.color, self.rect)

    def effect(self, player: Player):
        if player.rect.colliderect(self.rect):
            if self.state not in player.state:
                player.state.append(self.state)
                player.color = self.color

class Poison(State):
    def __init__(self, width: int, height: int, size: tuple) -> None:
        super().__init__(width, height, size)

        self.color = (0, 180, 0)
        self.state = "veneno"
        self.duration = 3  # seconds
        self.dagame = 1
    
    def effect(self, player: Player):
        super().effect(player)
        if self.state in player.state:
            if self.logic.decrease_hp(player, self.dagame, self.duration):
                player.state.remove(self.state)
                player.color = (255, 255, 255)


class Burn(State):
    def __init__(self, width: int, height: int, size: tuple) -> None:
        super().__init__(width, height, size)
        self.rect.x = 85
        self.rect.y = 25

        self.color = (180, 0, 0)
        self.state = "quemado"
        self.dagame = 1
        
    def effect(self, player: Player):
        super().effect(player)
        if self.state in player.state:
            self.logic.decrease_hp_endless(player, self.dagame)

class Wet(State):
    def __init__(self, width: int, height: int, size: tuple) -> None:
        super().__init__(width, height, size)
        self.rect.x = 145
        self.rect.y = 25

        self.color = (0, 0, 180)
        self.state = "humedo"
        self.dagame = 0
        self.speed = 2
        self.duration = 5
        
    def effect(self, player: Player):
        super().effect(player)
        if self.state in player.state:
            if self.logic.decrease_speed(player, self.speed, self.duration):
                player.state.remove(self.state)
                player.color = (255, 255, 255)
                
            if "quemado" in player.state:
                player.state.remove("quemado")
                self.logic.duration_time = self.duration-1