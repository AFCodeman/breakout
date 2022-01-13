import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color =

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image =
        self.rect =

        # Add a circle to represent the ball to the surface just created. Just use the pygame.draw.circle method.
        # The surface will be self.image


        # Give the ball an initial speed. You will need a speed for the x direction and one for the y direction.


    def move(self):
       pass
