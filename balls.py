#  Space Game with platforms

import pygame
import random

pygame.init()
pygame.mixer.init()

# Window settings
WIDTH = 900
HEIGHT = 600
TITLE = "Bouncing Ball"
FPS = 60

# Make the window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (175, 0, 0)
GREEN = (20, 200, 75)
BLUE_GREY = (211, 223, 227)
FOREST_GREEN = (72, 82, 23)
PINK = (255, 133, 163)
LIGHT_ORANGE = (255, 169, 99)

# Physics
H_SPEED = 4
JUMP_POWER = 12
GRAVITY = 0.4
TERMINAL_VELOCITY = 100

# Other configurations
# --


class Ball():
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.vx = random.randint(1, 7)
        self.vy = random.randint(1, 7)

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def get_ellipse(self):
        return [self.x, self.y, self.w, self.h]
    
    def check_movement(self):
        self.move()
        if self.x >= WIDTH - self.w:
            self.vx = self.vx * -1
        elif self.x <= 0:
            self.vx = self.vx * -1
        elif self.y >= HEIGHT - self.h:
            self.vy = self.vy * -1
        elif self.y <= 0:
            self.vy = self.vy * -1
        
    def get_rect(self):
        return [self.x, self.y, self.w, self.h]

    def update(self):
        self.check_movement()
        
    def draw(self):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.w, self.h])


def setup():
    global balls, red

    red = Ball(400, 300, 75, 75, RED)
    orange = Ball(200, 200, 100, 100, LIGHT_ORANGE)
    green = Ball(800, 400, 50, 50, GREEN)
    pink = Ball(100, 500, 60, 60, PINK)
    bluegrey = Ball(500, 300, 150, 150, BLUE_GREY)
    balls = [red, orange, green, pink, bluegrey]
    
setup()
done = False

while not done:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)

    for ball in balls:
        ball.draw()
        ball.move()
        ball.update()
   
    # update screen
    pygame.display.update()
    clock.tick(FPS)

# close window on quit
pygame.quit ()
