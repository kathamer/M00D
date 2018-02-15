"""
Custom.py
Custom user aesthetic for M00D
by Dylan Hamer
"""

from M00D import mood

class settings:
    colours = input("Enter colours seperated by a colon. (Available: red, green, blue, cyan, magenta, black, white): ").split(":")
    text = input("Enter the different text values you want to be displayed seperated by a colon: ").split(":")
    delay = int(input("Enter the amount of time in seconds you would like to wait between each print: "))
    title = input("Enter the title of the terminal that you would like: ")
    exitMessage = input("Enter the message you would like to be displayed when the program is exited cleanly: ")

mood(colours = settings.colours,
     text = settings.text,
     delay = settings.delay,
     title = settings.title,
     exitMessage = settings.exitMessage)
