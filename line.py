from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


class MidpointLine:
    
    def __init__(self):
        self.__midpoint_points = []

    def find_zone(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            if dx >= 0 and dy >= 0:
                return 0
            elif dx <= 0 and dy >= 0:
                return 3
            elif dx <= 0 and dy <= 0:
                return 4
            elif dx >= 0 and dy <= 0:
                return 7
        else:
            if dx >= 0 and dy >= 0:
                return 1
            elif dx <= 0 and dy >= 0:
                return 2
            elif dx <= 0 and dy <= 0:
                return 5
            elif dx >= 0 and dy <= 0:
                return 6

    def convert_to_zone0(self, x1, y1, zone):
        """
        Converting to Zone 0 from any zone.

        \nFrom Zone 0 -> x = x, y = y
        \nFrom Zone 1 -> x = y, y = x
        \nFrom Zone 2 -> x = y, y = -x
        \nFrom Zone 3 -> x = -x, y = y
        \nFrom Zone 4 -> x = -x, y = -y
        \nFrom Zone 5 -> x = -y, y = -x
        \nFrom Zone 6 -> x = -y, y = x
        \nFrom Zone 7 -> x = x, y = -y

        :return: x1, y1, x2, y2
        """

        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return y1, -x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return -y1, x1
        elif zone == 7:
            return x1, -y1

    def convert_to_original_zone(self, x1, y1, zone):
        """
        Converting to original zone from zone 0.
        The method is as same as converting to Zone 0 from any zone except for zone 2 and zone 6

        \nFrom Zone 2 -> x = -y, y = x
        \nFrom Zone 6 -> x = y, y = -x

        :return: x1, y1, x2, y2
        """

        if zone == 0:
            return x1, y1
        elif zone == 1:
            return y1, x1
        elif zone == 2:
            return -y1, x1
        elif zone == 3:
            return -x1, y1
        elif zone == 4:
            return -x1, -y1
        elif zone == 5:
            return -y1, -x1
        elif zone == 6:
            return y1, -x1
        elif zone == 7:
            return x1, -y1

    def midpoint(self, x1, y1, x2, y2):
        glBegin(GL_POINTS)

        zone = self.find_zone(x1, y1, x2, y2)

        x1_to_z0, y1_to_z0 = self.convert_to_zone0(x1, y1, zone)
        x2_to_z0, y2_to_z0 = self.convert_to_zone0(x2, y2, zone)

        dy = y2_to_z0 - y1_to_z0
        dx = x2_to_z0 - x1_to_z0
        d = 2 * dy - dx
        d_E = 2 * dy
        d_NE = 2 * (dy - dx)

        x = x1_to_z0
        y = y1_to_z0

        original_x, original_y = self.convert_to_original_zone(x, y, zone)
        glVertex2f(original_x, original_y)

        while x <= x2_to_z0:
            self.__midpoint_points.append((original_x, original_y))

            if d < 0:
                x = x + 1
                d = d + d_E
            else:
                x = x + 1
                y = y + 1
                d = d + d_NE

            original_x, original_y = self.convert_to_original_zone(x, y, zone)
            glVertex2f(original_x, original_y)

        glEnd()
