"""
stanCode SC101 Assignment 5 Problem 2
File: sierpinski.py
Name: Tiffany Lin
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Sierpinski triangles to be recursively printed on canvas;
	while the constant, ORDER, controlling the level of iterations.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: The constant controlling the order of Sierpinski Triangle
	:param length: The length of order 1 Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of order 1 Sierpinski Triangle
	:return: Sierpinski triangles on the canvas
	"""
	if order == 0:
		return
	else:
		pause(10)

		# Original triangle
		horizontal_line = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		left_line = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		right_line = GLine(upper_left_x+length, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		window.add(horizontal_line)
		window.add(left_line)
		window.add(right_line)

		# Hypotenuse on the left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)

		# Hypotenuse on the right
		sierpinski_triangle(order-1, length / 2, upper_left_x+length/2, upper_left_y)

		# Base of triangle
		sierpinski_triangle(order-1, length / 2, upper_left_x+length/4, upper_left_y+length*0.866/2)


if __name__ == '__main__':
	main()
