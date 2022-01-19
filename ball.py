import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius


        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((2 * radius, 2 * radius))
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created. Just use the pygame.draw.circle method.
        # The surface will be self.image
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)

        # Give the ball an initial speed. You will need a speed for the x direction and one for the y direction.
        self.speed_x = 2
        self.speed_y = 3

    def move(self):
       self.rect.x += self.speed_x
       self.rect.y += self.speed_y
       if self.rect.left <= 0:
           self.speed_x *= -1
       if self.rect.right >= self.windowWidth:
            self.speed_x *= -1
       if self.rect.top <= 0:
            self.speed_y *= -1
       if self.rect.bottom >= self.windowHeight:
           self.speed_y *= -1
