"""
Matrix.py
Matrix aesthetic for M00D
by Dylan Hamer
"""

from M00D import loop, clear

class matrix:
    colours = ["red", "yellow"]
    text = ["PIZZA!", "pizza"]
    delay = 0.001
    title = "pizza time"


clear()

loop(colours = matrix.colours,
     text = matrix.text,
     delay = matrix.delay,
     title = matrix.title)
