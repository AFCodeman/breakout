import pygame

class Paddle(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.width = width

        # Create a surface with the correct height and width
        self.image = pygame.Surface((self.width, self.height))

        # Get the rect coordinates
        self.rect = self.image.get_rect()

        # Fill the surface with the correct color
        self.image.fill(self.color)

    def move(self):
        pass

