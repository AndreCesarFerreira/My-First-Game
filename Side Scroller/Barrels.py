import pygame

""" Barrels Class """


class Barrels(object):
    """ Barrels initializer """
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (x, y, width, height)
        self.count = 0


""" Barrel 1 with a distinct image and hitbox """


class Barrel1(Barrels):
    """ loading of the proper image file """
    img = pygame.image.load('images/barrel_1.png')

    """ Method to draw the Barrel correctly across the Main panel """
    def draw(self, win):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height - 5)
        if self.count >= 0:
            self.count = 0
        win.blit(self.img, (self.x, self.y))
        """ For testing purposes the next line of code was used to test out the hitbox
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) """

    """ Method to detect the collision between the Player and the Barrel """
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


""" Barrel 2 with a distinct image and hitbox """


class Barrel2(Barrels):
    """ loading of the proper image file """
    img = pygame.image.load('images/barrel_2.png')

    """ Method to draw the Barrel correctly across the Main panel """
    def draw(self, win):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height - 5)
        if self.count >= 0:
            self.count = 0
        win.blit(self.img, (self.x, self.y))
        """ For testing purposes the next line of code was used to test out the hitbox
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) """

    """ Method to detect the collision between the Player and the Barrel """
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False


""" Barrel 3 with a distinct image and hitbox """


class Barrel3(Barrels):
    """ loading of the proper image file """
    img = pygame.image.load('images/barrel_3.png')

    """ Method to draw the Barrel correctly across the Main panel """
    def draw(self, win):
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height - 5)
        if self.count >= 0:
            self.count = 0
        win.blit(self.img, (self.x, self.y))
        """ For testing purposes the next line of code was used to test out the hitbox
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2) """

    """ Method to detect the collision between the Player and the Barrel """
    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False
