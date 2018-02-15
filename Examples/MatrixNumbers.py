"""
Matrix.py
Matrix aesthetic for M00D
by Dylan Hamer
"""

from M00D import loop, clear


class matrix:
    colours = ["green", "white"]
    text = list(range(9))
    delay = 0.001
    title = "F0110W TH3 WH1T3 R@881T"
    exitMessage = "\n\nIgnorance is bliss.\n"

clear()

loop(colours = matrix.colours,
     text = matrix.text,
     delay = matrix.delay,
     title = matrix.title,
     exitMessage = matrix.exitMessage)
