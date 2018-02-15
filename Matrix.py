"""
Matrix.py
Matrix aesthetic for M00D
by Dylan Hamer
"""

from M00D import mood

class matrix:
    colours = ["green", "white"]
    text = ["0", "1"]
    delay = 0.01
    title = "F0110W TH3 WH1T3 R@881T"
    exitMessage = "\n\nIgnorance is bliss.\n"

mood(colours = matrix.colours,
     text = matrix.text,
     delay = matrix.delay,
     title = matrix.title,
     exitMessage = matrix.exitMessage)
