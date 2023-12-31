from circle import MidpointCircle
from line import MidpointLine
from digits import Digits
from cube import CUBE
from uiTexts import UI_Text


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
from random import randint
from threading import Thread
from time import sleep
from pynput.keyboard import Key, Controller

y = 900
auto_key_press = Controller()
scale_radius = 0
SCORE = 0
HEALTH = 100

line = MidpointLine()
circle = MidpointCircle()
ui_text = UI_Text()
colors = 0, 0, 0

PLAYER_CURRENT_X_POSITION = 0
PLAYER_CURRENT_Y_POSITION = - 600
PLAYER_RADIUS = 40

OBJECT1_CURRENT_X_POSITION = randint(-600, 600)  # - 600 => 600
OBJECT1_CURRENT_Y_POSITION = 900
OBJECT1_SPEED = 10

OBJECT2_CURRENT_X_POSITION = randint(-600, 600)
OBJECT2_CURRENT_Y_POSITION = 900
OBJECT2_SPEED = 12

OBJECT3_CURRENT_X_POSITION = randint(-600, 600)
OBJECT3_CURRENT_Y_POSITION = 900
OBJECT3_SPEED = 20

OBJECT4_CURRENT_X_POSITION = randint(-600, 600)
OBJECT4_CURRENT_Y_POSITION = 900
OBJECT4_SPEED = 14

OBJECT5_CURRENT_X_POSITION = randint(-600, 600)
OBJECT5_CURRENT_Y_POSITION = 900
OBJECT5_SPEED = 22

OBJECT6_CURRENT_X_POSITION = randint(-600, 600)
OBJECT6_CURRENT_Y_POSITION = 900
OBJECT6_SPEED = 10

OBJECT7_CURRENT_X_POSITION = randint(-600, 600)
OBJECT7_CURRENT_Y_POSITION = 900
OBJECT7_SPEED = 8

OBJECT8_CURRENT_X_POSITION = randint(-600, 600)
OBJECT8_CURRENT_Y_POSITION = 900
OBJECT8_SPEED = 14

OBJECT9_CURRENT_X_POSITION = randint(-600, 600)
OBJECT9_CURRENT_Y_POSITION = 900
OBJECT9_SPEED = 20

OBJECT10_CURRENT_X_POSITION = randint(-600, 600)
OBJECT10_CURRENT_Y_POSITION = 900
OBJECT10_SPEED = 12


OBSTACLE_RADIUS = 40

SPEED_MULTIPLIER = 4

JIGGLE_X = 0

BULLET_X_POSITION = 900
BULLET_POSITION_Y = PLAYER_CURRENT_Y_POSITION
FIRE = False

# This boolean will decide should the update function run or not. Update function is responsible for drawing
# frames in every 0.1 seconds. If GAME_OVER is True, the update function will be stopped and the game will stop.
GAME_OVER = False


def environment_stars_and_air(value=10):
    # Stars animation
    glBegin(GL_POINTS)

    # Left stars
    for i in range(value):
        stars_x, stars_y = randint(-1920, -700), randint(-900, 900)
        glVertex2f(stars_x, stars_y)
    # Right stars
    for i in range(value):
        stars_x, stars_y = randint(700, 1920), randint(-900, 900)
        glVertex2f(stars_x, stars_y)
    glEnd()

    # Air animation
    # Left air
    for i in range(value - 4,):
        line_x, line_y = randint(-1920, -700), randint(-900, 900)
        line1_y = randint(-900, 900)
        line.midpoint(line_x, line_y, line_x, line1_y)
    # Right air
    for i in range(value - 4,):
        line_x, line_y = randint(700, 1920), randint(-900, 900)
        line1_y = randint(-900, 900)
        line.midpoint(line_x, line_y, line_x, line1_y)


def fire():
    global FIRE
    CUBE(-800)


def player_health_system():
    """
    This function will decrease the health of the player when the player is hit by the enemy drone.
    :return: None
    """
    global PLAYER_RADIUS, \
        HEALTH, \
        GAME_OVER

    PLAYER_RADIUS += 4
    HEALTH -= 1
    if HEALTH <= 0:
        HEALTH = 0
        PLAYER_RADIUS = - 100
        GAME_OVER = True


def update():
    """
    This update function is a mimic like Unity update. This update function is triggered in every 0.1 second.
    :return: None
    """
    global y, scale_radius, colors, \
        OBJECT1_CURRENT_Y_POSITION, \
        OBJECT1_CURRENT_X_POSITION, \
        OBJECT2_CURRENT_Y_POSITION, \
        OBJECT2_CURRENT_X_POSITION, \
        OBJECT3_CURRENT_Y_POSITION, \
        OBJECT3_CURRENT_X_POSITION, \
        OBJECT4_CURRENT_Y_POSITION, \
        OBJECT4_CURRENT_X_POSITION, \
        OBJECT5_CURRENT_Y_POSITION, \
        OBJECT5_CURRENT_X_POSITION, \
        OBJECT1_SPEED, \
        OBJECT2_SPEED, \
        OBJECT3_SPEED, \
        OBJECT4_SPEED, \
        OBJECT5_SPEED, \
        OBJECT6_CURRENT_Y_POSITION, \
        OBJECT6_CURRENT_X_POSITION, \
        OBJECT7_CURRENT_Y_POSITION, \
        OBJECT7_CURRENT_X_POSITION, \
        OBJECT8_CURRENT_Y_POSITION, \
        OBJECT8_CURRENT_X_POSITION, \
        OBJECT9_CURRENT_Y_POSITION, \
        OBJECT9_CURRENT_X_POSITION, \
        OBJECT10_CURRENT_Y_POSITION, \
        OBJECT10_CURRENT_X_POSITION, \
        OBJECT6_SPEED, \
        OBJECT7_SPEED, \
        OBJECT8_SPEED, \
        OBJECT9_SPEED, \
        OBJECT10_SPEED, \
        OBSTACLE_RADIUS, \
        PLAYER_CURRENT_Y_POSITION, \
        PLAYER_CURRENT_X_POSITION, \
        SPEED_MULTIPLIER, \
        JIGGLE_X, \
        BULLET_POSITION_Y, \
        FIRE, \
        GAME_OVER

    # Colors for score and health system
    red = True
    green = False
    blue = False

    while True:
        # Fire
        SPEED_MULTIPLIER += 0.001
        BULLET_POSITION_Y += 40
        if BULLET_POSITION_Y >= 900:
            BULLET_POSITION_Y = PLAYER_CURRENT_Y_POSITION
            FIRE = False

        scale_radius += 1
        auto_key_press.press(",")
        sleep(0.1)

        if GAME_OVER:
            break

        y -= 20
        if y <= -900:
            y = 900
            scale_radius = 0

        if red:
            red = False
            green = True
            blue = True
            colors = 1, 0, 0
        elif blue:
            red = False
            green = True
            blue = False
            colors = 0, 0, 1
        elif green:
            red = True
            green = False
            blue = True
            colors = 0, 1, 0

        JIGGLE_X += 1
        if JIGGLE_X > 20:
            JIGGLE_X = - 20

        # Enemy drones
        OBJECT1_CURRENT_Y_POSITION += - OBJECT1_SPEED * SPEED_MULTIPLIER
        if OBJECT1_CURRENT_Y_POSITION < - 900:
            OBJECT1_CURRENT_Y_POSITION = 900
            OBJECT1_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT2_CURRENT_Y_POSITION += - OBJECT2_SPEED * SPEED_MULTIPLIER
        if OBJECT2_CURRENT_Y_POSITION < - 900:
            OBJECT2_CURRENT_Y_POSITION = 900
            OBJECT2_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT3_CURRENT_Y_POSITION += - OBJECT3_SPEED * SPEED_MULTIPLIER
        if OBJECT3_CURRENT_Y_POSITION < - 900:
            OBJECT3_CURRENT_Y_POSITION = 900
            OBJECT3_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT4_CURRENT_Y_POSITION += - OBJECT4_SPEED * SPEED_MULTIPLIER
        if OBJECT4_CURRENT_Y_POSITION < - 900:
            OBJECT4_CURRENT_Y_POSITION = 900
            OBJECT4_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT5_CURRENT_Y_POSITION += - OBJECT5_SPEED * SPEED_MULTIPLIER
        if OBJECT5_CURRENT_Y_POSITION < - 900:
            OBJECT5_CURRENT_Y_POSITION = 900
            OBJECT5_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT6_CURRENT_Y_POSITION += - OBJECT6_SPEED * SPEED_MULTIPLIER
        if OBJECT6_CURRENT_Y_POSITION < - 900:
            OBJECT6_CURRENT_Y_POSITION = 900
            OBJECT6_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT7_CURRENT_Y_POSITION += - OBJECT7_SPEED * SPEED_MULTIPLIER
        if OBJECT7_CURRENT_Y_POSITION < - 900:
            OBJECT7_CURRENT_Y_POSITION = 900
            OBJECT7_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT8_CURRENT_Y_POSITION += - OBJECT8_SPEED * SPEED_MULTIPLIER
        if OBJECT8_CURRENT_Y_POSITION < - 900:
            OBJECT8_CURRENT_Y_POSITION = 900
            OBJECT8_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT9_CURRENT_Y_POSITION += - OBJECT9_SPEED * SPEED_MULTIPLIER
        if OBJECT9_CURRENT_Y_POSITION < - 900:
            OBJECT9_CURRENT_Y_POSITION = 900
            OBJECT9_CURRENT_X_POSITION = randint(-600, 600)

        OBJECT10_CURRENT_Y_POSITION += - OBJECT5_SPEED * SPEED_MULTIPLIER
        if OBJECT10_CURRENT_Y_POSITION < - 900:
            OBJECT10_CURRENT_Y_POSITION = 900
            OBJECT10_CURRENT_X_POSITION = randint(-600, 600)

        # Re-render the display
        glutPostRedisplay()


def score_increment():
    """
    This function is calculating the player score based on total survival time.
    :return: None
    """
    global SCORE
    while True:
        sleep(1)
        glutPostRedisplay()
        SCORE += 1
        if GAME_OVER:
            break


def RESTART():
    global y, scale_radius, colors, \
        OBJECT1_CURRENT_Y_POSITION, \
        OBJECT1_CURRENT_X_POSITION, \
        OBJECT2_CURRENT_Y_POSITION, \
        OBJECT2_CURRENT_X_POSITION, \
        OBJECT3_CURRENT_Y_POSITION, \
        OBJECT3_CURRENT_X_POSITION, \
        OBJECT4_CURRENT_Y_POSITION, \
        OBJECT4_CURRENT_X_POSITION, \
        OBJECT5_CURRENT_Y_POSITION, \
        OBJECT5_CURRENT_X_POSITION, \
        OBJECT1_SPEED, OBJECT2_SPEED, \
        OBJECT3_SPEED, OBJECT4_SPEED, \
        OBJECT5_SPEED, SPEED_MULTIPLIER, \
        PLAYER_CURRENT_X_POSITION, \
        PLAYER_CURRENT_Y_POSITION, \
        PLAYER_RADIUS, \
        SCORE, \
        OBSTACLE_RADIUS, \
        OBJECT6_CURRENT_Y_POSITION, \
        OBJECT6_CURRENT_X_POSITION, \
        OBJECT7_CURRENT_Y_POSITION, \
        OBJECT7_CURRENT_X_POSITION, \
        OBJECT8_CURRENT_Y_POSITION, \
        OBJECT8_CURRENT_X_POSITION, \
        OBJECT9_CURRENT_Y_POSITION, \
        OBJECT9_CURRENT_X_POSITION, \
        OBJECT10_CURRENT_Y_POSITION, \
        OBJECT10_CURRENT_X_POSITION, \
        OBJECT6_SPEED, \
        OBJECT7_SPEED, \
        OBJECT8_SPEED, \
        OBJECT9_SPEED, \
        OBJECT10_SPEED

    PLAYER_CURRENT_X_POSITION = 0
    PLAYER_CURRENT_Y_POSITION = - 600
    PLAYER_RADIUS = 40

    SCORE = 0
    OBSTACLE_RADIUS = 40

    OBJECT1_CURRENT_X_POSITION = randint(-600, 600)  # - 600 => 600
    OBJECT1_CURRENT_Y_POSITION = 900
    OBJECT1_SPEED = 10

    OBJECT2_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT2_CURRENT_Y_POSITION = 900
    OBJECT2_SPEED = 12

    OBJECT3_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT3_CURRENT_Y_POSITION = 900
    OBJECT3_SPEED = 20

    OBJECT4_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT4_CURRENT_Y_POSITION = 900
    OBJECT4_SPEED = 14

    OBJECT5_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT5_CURRENT_Y_POSITION = 900
    OBJECT5_SPEED = 22

    OBJECT6_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT6_CURRENT_Y_POSITION = 900
    OBJECT6_SPEED = 10

    OBJECT7_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT7_CURRENT_Y_POSITION = 900
    OBJECT7_SPEED = 8

    OBJECT8_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT8_CURRENT_Y_POSITION = 900
    OBJECT8_SPEED = 14

    OBJECT9_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT9_CURRENT_Y_POSITION = 900
    OBJECT9_SPEED = 20

    OBJECT10_CURRENT_X_POSITION = randint(-600, 600)
    OBJECT10_CURRENT_Y_POSITION = 900
    OBJECT10_SPEED = 12

    SPEED_MULTIPLIER = 4


class Survive_In_Space:
    
    def __init__(self, win_size_x=500, win_size_y=500, win_pos_x=0, win_pos_y=0, title="Priom OpenGL Class",
                 pixel_size=1):
        self.win_size_x = win_size_x
        self.win_size_y = win_size_y
        self.win_pos_x = win_pos_x
        self.win_pos_y = win_pos_y
        self.title = title
        self.pixel_size = pixel_size

        self.__midpoint_points = []
        self.__radius = 450
        self.__center_x = 0
        self.__center_y = 0

        self.player1_radius = 40
        self.player1_move_x = 0
        self.player1_move_y = 0
        self.score = 10

        self.player2_radius = 20
        self.player_move_x = 0
        self.player_move_y = 0

    def set_circle_values(self, radius, center_x=0, center_y=0):
        self.__radius = radius
        self.__center_x = center_x
        self.__center_y = center_y

    def initialize(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.win_size_x, self.win_size_y)
        glutInitWindowPosition(self.win_size_x // 2 - self.win_size_x, 0)
        glutCreateWindow(self.title)
        # glClearColor(0.3, 0.3, 0.3, 0)
        glClearColor(0, 0, 0, 0),
        glutDisplayFunc(self.show_screen)

        glutKeyboardFunc(self.buttons)
        glutMotionFunc(self.mouse)

        animation_thread = Thread(target=update)
        animation_thread.start()

        global score_thread
        score_thread = Thread(target=score_increment)
        score_thread.start()

        glViewport(0, 0, self.win_size_x, self.win_size_y)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-self.win_size_x, self.win_size_x, -self.win_size_y, self.win_size_y, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glPointSize(self.pixel_size)
        glLoadIdentity()

    def mouse(self, x, y):
        print(x, y)

        self.player1_move_x = x - 450
        self.player1_move_y = y - 450
        glutPostRedisplay()

    def buttons(self, key, x, y):
        global PLAYER_CURRENT_Y_POSITION, \
            PLAYER_CURRENT_X_POSITION, \
            PLAYER_RADIUS, \
            FIRE, \
            BULLET_X_POSITION, \
            GAME_OVER, \
            HEALTH, \
            SCORE

        move = 50

        # Movement inputs
        if key == b"w":
            PLAYER_CURRENT_Y_POSITION += move
        if key == b"a" and PLAYER_CURRENT_X_POSITION > - 600:
            PLAYER_CURRENT_X_POSITION -= move
        if key == b"s":
            PLAYER_CURRENT_Y_POSITION -= move
        if key == b"d" and PLAYER_CURRENT_X_POSITION < 600:
            PLAYER_CURRENT_X_POSITION += move

        # Restart game when "r" button is pressed
        if key == b"r":
            GAME_OVER = False
            PLAYER_RADIUS = 40
            HEALTH = 100

            restart = Thread(target=update)
            restart.start()

            SCORE = 0
            restart_score = Thread(target=score_increment)
            restart_score.start()

        if self.player1_radius > 0:
            if key == b"m":
                PLAYER_RADIUS += move
            if key == b"n":
                PLAYER_RADIUS -= move
        else:
            self.player1_radius += 10

        if PLAYER_CURRENT_Y_POSITION < - self.win_size_y:
            PLAYER_CURRENT_Y_POSITION = self.win_size_y

        if PLAYER_CURRENT_X_POSITION < - self.win_size_x:
            PLAYER_CURRENT_X_POSITION = self.win_size_x

        if PLAYER_CURRENT_Y_POSITION > self.win_size_y:
            PLAYER_CURRENT_Y_POSITION = - self.win_size_y

        if PLAYER_CURRENT_X_POSITION > self.win_size_x:
            PLAYER_CURRENT_X_POSITION = - self.win_size_x

        if key == b"f":
            BULLET_X_POSITION = PLAYER_CURRENT_X_POSITION
            FIRE = True

        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT1_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 1")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT2_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT2_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 2")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT3_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT3_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 3")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT4_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT4_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 4")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT5_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT5_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 5")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT6_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT6_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 6")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT7_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT7_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 7")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT8_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT8_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 8")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT9_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT9_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 9")
            player_health_system()
            # RESTART()
        if PLAYER_CURRENT_Y_POSITION - PLAYER_RADIUS <= OBJECT10_CURRENT_Y_POSITION <= PLAYER_CURRENT_Y_POSITION + PLAYER_RADIUS and PLAYER_CURRENT_X_POSITION - PLAYER_RADIUS <= OBJECT10_CURRENT_X_POSITION <= PLAYER_CURRENT_X_POSITION + PLAYER_RADIUS:
            print("Collision with Object 10")
            player_health_system()
            # RESTART()

        glutPostRedisplay()

    def another_circle(self, radius):
        circle1 = MidpointCircle()
        circle1.midpoint_circle_algorithm(500)

    # Glut Display
    def show_screen(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glColor(1,1,1)
        CUBE(y=OBJECT1_CURRENT_Y_POSITION)
        glColor3f(1, 1, 0)

        # Drawing methods
        self.road()
        self.road_decorators(-10)
        self.road_decorators(1400, 0)
        ui_text.health_text(-1900, 200)
        ui_text.score_text(950, 200)

        # Stars
        glColor3f(1, 1, 1)
        environment_stars_and_air(value=10)

        # Obstacles
        glColor3f(1, 1, 0)
        glPointSize(1)
        self.obstacle(OBJECT1_CURRENT_X_POSITION, OBJECT1_CURRENT_Y_POSITION)
        self.obstacle(OBJECT2_CURRENT_X_POSITION, OBJECT2_CURRENT_Y_POSITION)
        self.obstacle(OBJECT3_CURRENT_X_POSITION, OBJECT3_CURRENT_Y_POSITION)
        self.obstacle(OBJECT4_CURRENT_X_POSITION, OBJECT4_CURRENT_Y_POSITION)
        self.obstacle(OBJECT5_CURRENT_X_POSITION, OBJECT5_CURRENT_Y_POSITION)
        self.obstacle(OBJECT6_CURRENT_X_POSITION, OBJECT6_CURRENT_Y_POSITION)
        self.obstacle(OBJECT7_CURRENT_X_POSITION, OBJECT7_CURRENT_Y_POSITION)
        self.obstacle(OBJECT8_CURRENT_X_POSITION, OBJECT8_CURRENT_Y_POSITION)
        self.obstacle(OBJECT9_CURRENT_X_POSITION, OBJECT9_CURRENT_Y_POSITION)
        self.obstacle(OBJECT10_CURRENT_X_POSITION, OBJECT10_CURRENT_Y_POSITION)

        # Player
        glColor3f(0, 1, 0)
        # circle.filled_circle(self.player2_radius, self.player2_move_x, self.player2_move_y)
        circle.midpoint_circle_algorithm(PLAYER_RADIUS, PLAYER_CURRENT_X_POSITION, PLAYER_CURRENT_Y_POSITION)
        circle.filled_circle(PLAYER_RADIUS // 2 - 4, PLAYER_CURRENT_X_POSITION, PLAYER_CURRENT_Y_POSITION + 10)

        glPointSize(1)

        # Score
        score_and_health_text = Digits()
        digit_position = 900
        glColor3f(colors[0], colors[1], colors[2])

        for i in range(10, 50, 4):
            score_and_health_text.draw_digit(f"{SCORE}", offset_x=i, offset_y=i, digit_position_x=digit_position)

        glColor3f(colors[2], colors[1], colors[0])
        for i in range(10, 50, 2):
            score_and_health_text.draw_digit(f"{HEALTH}", digit_position_x=-1920 + i, offset_x=i, offset_y=i)

        # Bullet object for fire
        if FIRE:
            circle.filled_circle(10, BULLET_X_POSITION, BULLET_POSITION_Y)
            fires = Thread(target=fire)
            fires.start()

        # Drawing cross marks when the game is over
        if GAME_OVER:
            glColor3f(0, 0, 1)

            for i in range(0, 10, 2):
                circle.midpoint_circle_algorithm(900 - i, 0, 0)

            for i in range(0, 100, 10):
                circle.midpoint_circle_algorithm(900 - i, 0, 0)

            glColor3f(1, 0, 0)
            ui_text.game_over_text(-650, 0)

        glutSwapBuffers()

    def start_main_loop(self):
        glutMainLoop()

    def road(self):
        left_x1, left_y1 = -700, -900
        offset = -50

        line.midpoint(left_x1 + offset, left_y1, left_x1 + offset, 900)
        line.midpoint(-left_x1 - offset, left_y1, -left_x1 - offset, 900)

        for i in range(10):
            line.midpoint(left_x1 + offset + i, left_y1, left_x1 + offset + i + i*10, 900)
            line.midpoint(-left_x1 - offset - i, left_y1, -left_x1 - offset - i - i*10, 900)

    def road_decorators(self, offset_x=0, offset_y=0):
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + offset_x, y + offset_y)
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + 20 + offset_x, y + offset_y)
        circle.midpoint_circle_algorithm(scale_radius + 10, -700 + 10 + offset_x, y + 10 + offset_y)

    def obstacle(self, obstacle_x_position, obstacle_y_position):
        circle.midpoint_circle_algorithm(OBSTACLE_RADIUS, obstacle_x_position, obstacle_y_position)
        circle.filled_circle(OBSTACLE_RADIUS // 2 - 4, obstacle_x_position + JIGGLE_X, obstacle_y_position - 10)


survive_in_space = Survive_In_Space(win_size_x=1920,
                                    win_size_y=900,
                                    pixel_size=1,
                                    title="BubbleEscape")

survive_in_space.initialize()
survive_in_space.start_main_loop()