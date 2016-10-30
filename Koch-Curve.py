# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:15:17 2016

@author: Dom
"""

from graphics import *
from math import *
win = GraphWin("test", 1080, 720)
win.setCoords(-100,-100,100,100)
win.setBackground('white')

def C(turtle, length, degree):
    if degree == 0:
        turtle.draw(length)
    else:
        degree -= 1
        length = length/sqrt(2)
        turtle.turn(45)
        C(turtle,length, degree)
        turtle.turn(-90)
        C(turtle,length,degree)
        turtle.turn(45)
      
        
class Turtle:
    def __init__(self, location, direction,win):
        self.location = location
        self.direction = radians(direction)
        self.x = location.getX()
        self.y = location.getY()
        self.win = win
    def moveTo(self, point):
        self.location = point
    def draw(self, length):
        self.dx = length * cos(self.direction)
        self.dy = length * sin(self.direction)
        self.x += self.dx
        self.y += self.dy
        line = Line(self.location, Point(self.x, self.y))
        line.draw(self.win)
        self.moveTo(Point(self.x, self.y))
    def turn(self, degree):
        self.direction += radians(degree)
    
turtle = Turtle(Point(0,0), 90, win)
c = C(turtle, 50,12)