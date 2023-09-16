import pygame

from assets.player import Player
from assets.state import Poison
from assets.logic import Logic


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.inGame = False

        self.original = (800, 600)
        self.screen = pygame.display.set_mode(self.original)

        pygame.display.set_caption("Elementos")

        # Ticks
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Config
        self.mainFont = pygame.font.SysFont("Dancing Script", 24)

    def load_resources(self):
        pass

    def load_assets(self):
        # player
        self.player = Player(50, 50, self.original)

        # state
        self.poison = Poison(50, 50, self.original)

        # logic
        self.logic = Logic()

    def run(self):
        self.inGame = True
        self.load_resources()
        self.load_assets()
        while self.inGame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.inGame = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        if self.player.state == "veneno":
                            print("Te curaste.")
                            self.player.state = ""
                            self.player.color = (255, 255, 255)

                    if event.key == pygame.K_SPACE:
                        print("Vida: ", self.player.hp)

            keys = pygame.key.get_pressed()
            self.player.movement(keys)
            if keys[pygame.K_q]:
                self.inGame = False

            # Logic
            if self.player.rect.colliderect(self.poison.rect):
                if not self.player.state:
                    print("envenenado. ")
                    self.player.state = self.poison.state
                    self.player.color = self.poison.color

            if self.player.state == "veneno":
                if self.logic.decrease_hp(self.player, self.poison.dagame, self.poison.duration):
                    self.player.state = ""
                    self.player.color = (255, 255, 255)

            # frame
            self.screen.fill((0, 0, 0))

            # dibujo
            self.player.draw(self.screen)
            
            label_hp = self.mainFont.render(
                str(self.player.hp), True, (0, 0, 0))

            self.screen.blit(label_hp, (
                self.player.rect.centerx  - (label_hp.get_width() / 2),
                self.player.rect.centery  - (label_hp.get_height() / 2)
                ))

            self.poison.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    game = Game()
    game.run()
