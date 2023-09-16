import pygame

class Player():
    def __init__(self, width, height, size: tuple) -> None:
        self.size = size
        
        self.speed = 4
        self.rect = pygame.Rect(400, 300, width, height)
        self.color = (255,255,255)
        self.state = ""
        
        self.hp = 50

    def movement(self, keys):
        if keys[pygame.K_a]:
            self.rect.left -= self.speed
            self.moveState = True

        if keys[pygame.K_d]:
            self.rect.right += self.speed
            self.moveState = True

        if keys[pygame.K_w]:
            self.rect.top -= self.speed
            self.moveState = True

        if keys[pygame.K_s]:
            self.rect.bottom += self.speed
            self.moveState = True

    def limit_player(self):
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.size[0]:
            self.rect.right =self. size[0]
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.size[1]:
            self.rect.bottom = self.size[1]
            
    def draw(self, screen: pygame.Surface):
        self.limit_player()

        return pygame.draw.rect(screen, self.color, self.rect)