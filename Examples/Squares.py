"""
Squarws.py
Squares aesthetic for M00D
by Dylan Hamer
"""

from M00D import loop, clear

class squares:
    colours = ["red", "green", "blue", "yellow", "cyan", "magenta", "white"]
    text = ["#"]
    delay = 0.001
    title = "Squares!"

clear()

loop(colours = squares.colours,
     text = squares.text,
     delay = squares.delay,
     title = squares.title)
