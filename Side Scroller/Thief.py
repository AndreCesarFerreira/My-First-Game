import pygame
import os

""" Thief Class """


class Thief(object):
    """ Run behaviour setup """
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(16, 24)]

    """ Thief initializer """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.runCount = 0
        self.hitbox = (x, y, width, height)

    """ Method to draw the Thief correctly across the Main panel """
    def draw(self, win):
        if self.runCount > 42:
            self.runCount = 0
        win.blit(self.run[self.runCount // 6], (self.x, self.y))
        self.runCount += 1
        self.hitbox = (self.x + 4, self.y, self.width - 20, self.height)
        """ For testing purposes the next line of code was used to test out the hitbox
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) """

    """ Method to detect the collision between the Player and the Thief """
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
