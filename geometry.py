"""Module contains basic geometry objects"""

import logging

logger = logging.getLogger(__name__)


class Point:
    """Two dimensional point"""

    def __init__(self, xcoord, ycoord):
        """Initializes point with x and y coordinates

        Args:
            xcoord(int): X coordinate
            ycoord(int): Y coordinate
        """
        self.xcoord = xcoord
        self.ycoord = ycoord

        logger.debug('Point created; ({},{})'.format(xcoord, ycoord))

    def move_x(self, amount):
        """Changes x coordinate by given amount

        Args:
            amount(int): Number of units to move by
        """
        logger.debug('Point {} moved by {} in the x direction'.format(self.to_repr(), amount))

        self.xcoord += amount

    def move_y(self, amount):
        """Changes y coordinate by given amount

        Args:
            amount(int): Number of units to move by
        """
        logger.debug('Point {} moved by {} in the y direction'.format(self.to_repr(), amount))

        self.ycoord += amount

    def to_repr(self):
        """Returns representation of Point for logging"""
        return '({},{})'.format(self.xcoord, self.ycoord)


class Line:
    """Connection between two points"""

    def __init__(self, point1, point2):
        """Initializes a line given two points

        Args:
            point1(Point): The point at one end of the line
            point2(Point): The point at the other end of the line
        """
        self.point1 = point1
        self.point2 = point2

        logger.debug('Line created with points {} and {}'.format(point1.to_repr(), point2.to_repr()))

    def to_repr(self):
        """Returns representation of Line for logging"""
        return '[{}, {}]'.format(self.point1.to_repr(), self.point2.to_repr())

    @property
    def points(self):
        """Returns list of two points"""
        return [self.point1, self.point2]
