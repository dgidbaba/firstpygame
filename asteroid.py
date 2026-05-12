import pygame
import random
from constants import *
from circleshape import CircleShape
from logger import log_event



class Asteroid(CircleShape):    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)
        
    def split(self):
        self.kill()
        if self.radius >= ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            rand = random.uniform(20, 50)
            new_vel = self.velocity.rotate(rand)
            new_vel2 = self.velocity.rotate(rand * -1)
            new_rad = self.radius - ASTEROID_MIN_RADIUS

            self.spawn(new_rad, self.position, new_vel).velocity *= 1.2
            self.spawn(new_rad, self.position, new_vel2).velocity *= 1.2 

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity 
        return asteroid  

        
