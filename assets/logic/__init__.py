import pygame
from assets.player import Player


class Logic:
    def __init__(self) -> None:
        self.duration_time = None
        self.last_second = None
    
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
    
    def cancel_endless(self):
        self.last_second = None
        