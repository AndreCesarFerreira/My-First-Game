from Barrels import *
from Mechanics import *
from random import randint

""" Main window setup """
W, H = 800, 500
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Gota get him Fast!')
bg = pygame.image.load(os.path.join('images', 'dark_city.png')).convert()
bg = pygame.transform.scale(bg, (800, 500))
bgX = 0
bgX2 = bg.get_width()
clock = pygame.time.Clock()

""" Method to update the score file """


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


""" Method for the end screen to display the final score as well as the one registered on the scores file """


def end_screen():
    global objects, score
    objects = []
    while True:
        pygame.time.delay(100)
        large_font = pygame.font.SysFont('comicsans', 80)
        max_score = large_font.render('Best Score: ' + str(update_file()), 1, (255, 255, 255))
        win.blit(max_score, (W / 2 - max_score.get_width() / 2, H/2 - 100))
        new_score = large_font.render('Score: ' + str(score), 1, (255, 255, 255))
        win.blit(new_score, (W / 2 - new_score.get_width() / 2, 320))
        pygame.display.update()

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif keys[pygame.K_SPACE]:
                pass


""" Method to redraw the main window over time """


def redraw_window():
    win.blit(bg, (bgX, 0))
    win.blit(bg, (bgX2, 0))
    catcher.draw(win)
    runner.draw(win)
    for x in objects:
        x.draw(win)

    font = pygame.font.SysFont('comicsans', 30)
    score_text = font.render('Score: ' + str(int(score)), 1, white)
    gotchafam = font.render('Gotcha: ' + str(gotcha), 1, white)
    missmefam = font.render('Miss: ' + str(miss), 1, white)
    win.blit(score_text, (650, 10))
    win.blit(gotchafam, (650, 30))
    win.blit(missmefam, (650, 50))
    pygame.display.update()


""" Set up for some basic variables """
speed = 100
score = 0
objects = []
gotcha = randint(1, 3)
run = True


""" Main game """
while run:

    redraw_window()
    bg_sound.play(loops=-1)
    winning = pygame.font.SysFont('comicsans', 40)

    for objectt in objects:
        if objectt.collide(catcher.hitbox):
            pygame.time.delay(5)
            runner.x += 1
            score = score - 1
        elif runner.collide(catcher.hitbox):
            if gotcha == miss:
                bg_sound.stop()
                pygame.time.delay(10)
                gotchafam.play()
                pygame.time.delay(1000)
                gotcha_text = winning.render('Gotcha! and in ' + str(tries) + ' tries!', 1, white)
                win.blit(gotcha_text, (W/2 - gotcha_text.get_width()/2, H/2))
                end_screen()

            else:
                gotcha = randint(1, 3)
                runner.x = runner.x + 100
                redraw_window()
                tries += 1

        objectt.x -= 1
        if objectt.x < objectt.width * -1:
            objects.pop(objects.index(objectt))

    if score < 0:
        score = 0

    """ This helps the background to keep moving """
    bgX -= 2
    bgX2 -= 2
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == USEREVENT + 1:
            if speed < 150:
                speed += 1
                score += 10

        if event.type == USEREVENT + 2:
            r = randint(0, 4)
            if r == 0:
                objects.append(Barrel1(910, 325, 40, 40))
                speed = speed - 1
            elif r == 1:
                objects.append(Barrel2(910, 325, 78, 40))
                speed = speed - 1
            else:
                objects.append(Barrel3(910, 285, 39, 78))
                speed = speed - 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not catcher.jumping:
            catcher.jumping = True

    runner.x -= 0.1
    clock.tick(speed)
