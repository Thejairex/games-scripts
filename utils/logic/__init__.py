import pygame
from entities.player import Player
import threading

class Logic:
    def __init__(self) -> None:
        self.duration_time = None
        self.last_second = None
    
# Logic Effect

    def decrease_hp(self, entity: Player, damage, duration):
        if self.duration_time is None:
            self.duration_time = 0
            self.last_second =  pygame.time.get_ticks() // 1000
        
        current_time = pygame.time.get_ticks() // 1000
        
        if current_time != self.last_second:
            self.last_second = current_time
            self.duration_time += 1
            entity.hp -= damage
            
            if self.duration_time == duration:
                self.duration_time = None
                self.last_second = None
                
                return True
            
            else:
                return False
            
    def decrease_hp_endless(self, entity: Player, damage):
        if self.last_second == None:
            self.last_second = 0
    
        current_time = pygame.time.get_ticks() // 1000
        
        if current_time != self.last_second:
            self.last_second = current_time
            entity.hp -= damage
        
    def decrease_speed(self, entity: Player, speed, duration):
        if self.duration_time is None:
            self.duration_time = 0
            entity.speed -= speed
            self.last_second =  pygame.time.get_ticks() // 1000

        current_time = pygame.time.get_ticks() // 1000

        if self.duration_time == duration and self.duration_time != 0:
            self.duration_time = None
            self.last_second = None
            entity.speed += speed
            return True
            
        if current_time != self.last_second:
            self.last_second = current_time
            self.duration_time += 1

    def decrease_speed_endless(self, entity: Player, speed):
        pass

    def cancel_state(self, entity: Player, state):
        entity.state.remove(state)
        entity.color = (255, 255, 255)

    def cancel_endless(self):
        self.last_second = None
