from pygame.locals import *
from Player import *
from Thief import *
from random import randint

""" Pygame initializer for general purposes """
pygame.init()

""" Pygame Mixer initializer for sound related music content """
pygame.mixer.init()

""" Background sound set up """
bg_sound = pygame.mixer.Sound("sounds/background_sound.mp3")
bg_sound.set_volume(0.2)

""" Jump sound set up """
jump = pygame.mixer.Sound("sounds/jump.mp3")
jump.set_volume(1)

""" Hurt sound set up """
hurt = pygame.mixer.Sound("sounds/hurt.mp3")
hurt.set_volume(0.1)

""" Win sound set up """
gotchafam = pygame.mixer.Sound("sounds/win.wav")
gotchafam.set_volume(0.5)

""" Game clock set up """
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)

""" Catcher initializer with a Player as a base """
catcher = Player(50, 300, 64, 64)

""" Runner initializer with a Thief as a base """
runner = Thief(650, 300, 64, 64)

""" Method from pygame to set up the player position """
pygame.time.set_timer(USEREVENT + 1, 1000)

""" Method from pygame to set up the thief position """
pygame.time.set_timer(USEREVENT + 2, 3000)

""" random generator for the chance to miss the thief when close by him """
miss = randint(1, 3)

""" random generator for the chance to catch the thief when close by him """
gotcha = randint(1, 3)

""" score initializer """
score = 0

""" number of tries before catching the thief initializer """
tries = 1

""" Method to update the scores.txt file if the final score is higher than the one registered on the file"""


def update_file():
    f = open('scores.txt', 'r')
    file = f.readlines()
    last_score = int(file[0])
    if last_score < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()
        return score
    return last_score
