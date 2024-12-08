from direction import Direction 
from color import BLUE

import pygame


class Player:
    def __init__(self) -> None:
        self.__position = pygame.math.Vector2(50, 50)
        self.speed = 6 * 100
        self.width = 50
        self.height = 50
        self.direction = Direction.RIGHT

    @property
    def x(self):
        return self.__position.x
    
    @property
    def y(self):
        return self.__position.y

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.__move(keys, dt)
        self.__set_direction(keys)

    def get_direction(self):
        return self.direction

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.__position.x, self.__position.y, self.width, self.height))

    def __set_direction(self, keys: dict):
        if keys[pygame.K_UP]:
            self.direction = Direction.UP
        elif keys[pygame.K_DOWN]:
            self.direction = Direction.DOWN
        if keys[pygame.K_LEFT]:
            self.direction = Direction.LEFT
        elif keys[pygame.K_RIGHT]:
            self.direction = Direction.RIGHT

        if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            self.direction = Direction.UP_LEFT
        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]: 
            self.direction = Direction.UP_RIGHT
        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            self.direction = Direction.DOWN_LEFT
        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            self.direction = Direction.DOWN_RIGHT

    def __move(self, keys: dict, dt: float):
        if keys[pygame.K_UP]:
            self.__position.y -= self.speed * dt
        elif keys[pygame.K_DOWN]:
            self.__position.y += self.speed * dt

        if keys[pygame.K_LEFT]:
            self.__position.x -= self.speed * dt
        elif keys[pygame.K_RIGHT]:
            self.__position.x += self.speed * dt
