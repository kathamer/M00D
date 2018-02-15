"""
Police.py
Police aesthetic for M00D
by Dylan Hamer
"""

from M00D import loop, clear

class police:
    colours = ["red", "white", "blue"]
    text = ["WEE", "WOO"]
    delay = 0.001
    title = "It\'s the cops!"
    exitMessage = "\n\nWoop Woop, that\'s the sound of the police!\n"

clear()

loop(colours = police.colours,
     text = police.text,
     delay = police.delay,
     title = police.title,
     exitMessage = police.exitMessage)
