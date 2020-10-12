import pygame
from pygame.draw import *
from random import randint
pygame.init()

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FPS = 30
MAX_VEL = 7
WAIT_BALL = FPS*5
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

font = pygame.font.Font(None, 25)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Running_Ball(object):
    def __init__(self):
        self.x = randint(51, 449)
        self.y = randint(51, 449)
        self.r = randint(30, 50)

    def move(self):
        self.vx = 1/(self.x - pygame.mouse.get_pos())
        self.vy = 1/(self.y - pygame.mouse.get_pos())

        self.x += self.vx
        self.y += self.vy

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


class Ball(object):
    def __init__(self):
        self.x = randint(51, 449)
        self.y = randint(51, 449)
        self.r = randint(30, 50)
        self.vx = randint(-MAX_VEL, MAX_VEL)
        self.vy = randint(-MAX_VEL, MAX_VEL)
        self.color = COLORS[randint(0, 5)]

    def move(self):
        if self.vx == 0:
            self.vx = 1
        if self.vy == 0:
            self.vy = 1

        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= CANVAS_WIDTH or self.x - self.r <= 0:
            self.vx = -self.vx
            self.vy = randint(-MAX_VEL, MAX_VEL)
        if self.y + self.r >= CANVAS_HEIGHT or self.y - self.r <= 0:
            self.vy = -self.vy
            self.vx = randint(-MAX_VEL, MAX_VEL)

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


def dashboard_activity():
    done = False
    dat = []
    text_height = 5
    with open("scores.txt", "r") as f:
        data = f.readlines()
        f.close()
    print(data)
    while not done:
        for i in range(len(data)):
            text = font.render(data[i], True, BLUE)

        screen.blit(text, [5, text_height])

def escape_activity(score):
    input_box = rect(screen, WHITE, (5, 40, 140, 32))

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text_in_input = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        f =  open('scores.txt', 'a')
                        f.write(text_in_input + " " + str(score) + "\n")
                        f.close()
                        print(text_in_input)
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text_in_input = text_in_input[:-1]
                    else:
                        text_in_input += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        greeting_text = font.render("GREAT! YOUR SCORE IS {}".format(score), True, BLUE)
        nickname_text = font.render("Please, write your nickname", True, BLUE)
        txt_surface = font.render(text_in_input, True, color)
        # Resize the box if thetext_in_inputis too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(greeting_text, [5, 5])
        screen.blit(nickname_text, [5, 20])
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(FPS)
    dashboard_activity()


def check_click(event, balls):

    for ball in balls:
        if (ball.x - event.pos[0])**2 + (ball.y - event.pos[1])**2 <= ball.r**2:
            return ball

    return False

pygame.display.update()
clock = pygame.time.Clock()
finished = False

N = randint(3, 6)
running_ball = Ball()
balls = []
for i in range(N):
    balls.append(Ball())
counter = 0
text = font.render("SCORE: {}".format(counter),True,BLACK)
already_waited = 0
while not finished:
    clock.tick(FPS)
    finished =True
    already_waited += 1
    text = font.render("SCORE: {}".format(counter), True, RED)
    screen.blit(text, [5, 5])
    if WAIT_BALL <= already_waited:
        balls.append(Ball())
        already_waited = 0

    '''running_ball.move()
    running_ball.draw()'''

    for ball in balls:
        ball.move()
        ball.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            response = check_click(event, balls)
            if response != False:
                balls.remove(response)
                counter += 1
                if len(balls) == 0:
                    finished = True

    pygame.display.update()
    screen.fill(BLACK)

escape_activity(counter)


pygame.quit()