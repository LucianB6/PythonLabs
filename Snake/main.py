import random
import time

import pygame as pg
import pygame.mouse

# crearea de display

WIDTH = 400
HEIGTH = 400

FILL_COLOR = (1, 0, 35)
SNAKE_COLOR = (255, 255, 255)
FOOD_COLOR = (255, 0, 0)

screen = pg.display.set_mode((HEIGTH, WIDTH))

pg.display.set_caption("Snake")

START_IMAGE = pg.image.load('start_button_low_di.png').convert_alpha()
STOP_IMAGE = pg.image.load('stop_button.png').convert_alpha()

pg.display.update()


# creem o clasa oentru butoanele disponibile

class Buttons:
    def __init__(self, x, y, image):
        self.image = pg.transform.scale(image, (100, 40))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False

        position = pygame.mouse.get_pos()

        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image, (self.x, self.y))

        return action


start_button = Buttons(50, 150, START_IMAGE)
stop_button = Buttons(250, 150, STOP_IMAGE)

x = 0
y = 0
new_x = 0
new_y = 0

play = True
clock = pygame.time.Clock()


def displayGame():
    screen.fill(FILL_COLOR)
    GAMEOVER = pg.image.load('gameover.jpg').convert_alpha()
    image = pg.transform.scale(GAMEOVER, (200, 80))
    screen.blit(image, (100, 150))

    pg.display.update()
    time.sleep(3)



# functionalitate joc
class RunGame():
    def __init__(self, x, y, new_x, new_y):
        self.x = x
        self.y = y
        self.new_x = new_x
        self.new_y = new_y

    def gamePlay(self, run):
        heigth = 20
        length = 20
        TIMER = 5
        x_width = 200
        y_width = 200
        length_of_snake = 1
        increase = 0
        snake_list = [(self.x, self.y)]
        prevKey = "name"
        SCORE = (0, 255, 0)
        while run:
            pg.font.init()
            font = pygame.font.Font(None, 24)
            text = font.render("SCORE: " + str(length_of_snake), 1, SCORE)
            screen.blit(text, (160, 10))
            pg.display.update()

            for decision in pg.event.get():
                if decision.type == pg.QUIT:
                    print("GoodBye")
                    exitButton = False
                    quit()

                if decision.type == pg.KEYDOWN:
                    if decision.key == pg.K_LEFT:
                        if prevKey != "right":
                            self.new_x -= 20
                            self.new_y = 0
                            prevKey = "left"
                    elif decision.key == pg.K_RIGHT:
                        if prevKey != "left":
                            self.new_x += 20
                            self.new_y = 0
                            prevKey = "right"
                    elif decision.key == pg.K_UP:
                        if prevKey != "down":
                            self.new_x = 0
                            self.new_y -= 20
                            prevKey = "up"
                    elif decision.key == pg.K_DOWN:
                        if prevKey != "up":
                            self.new_x = 0
                            self.new_y += 20
                            prevKey = "down"

            self.x += self.new_x
            self.y += self.new_y

            if (self.x, self.y) in snake_list and length_of_snake >= 2:
                displayGame()

                run = False
                return run

            snake_list.append((self.x, self.y))
            positions = []
            if self.x == x_width and self.y == y_width:
                x_width = random.randrange(0, 400, +20)
                y_width = random.randrange(0, 400, +20)
                length_of_snake += 1
                increase += 1
            else:
                del snake_list[0]
            screen.fill(FILL_COLOR)
            for (i, j) in snake_list:
                pg.draw.rect(screen, SNAKE_COLOR, [i, j, heigth, length])

            pg.draw.rect(screen, FOOD_COLOR, [x_width, y_width, 20, 20])

            if length_of_snake % 5 == 0 and increase % 2 != 0:
                TIMER += 1
                increase += 1
            clock.tick(TIMER)

            pg.display.update()

            if self.x > HEIGTH or self.x < 0 or self.y > WIDTH or self.y < 0:
                displayGame()

                run = False
                return run


run = True

while play:
    screen.fill(FILL_COLOR)
    initializeGame = RunGame(x, y, new_x, new_y)

    if start_button.draw() and initializeGame.gamePlay(run):
        initializeGame.gamePlay(run)

    elif start_button.draw() and not initializeGame.gamePlay(run):
        run = True
        initializeGame.gamePlay(run)

    if stop_button.draw():
        print("GoodBye!")
        play = False

    pg.display.update()

    for decisions in pg.event.get():
        if decisions.type == pg.QUIT:
            play = False

# class Options:
