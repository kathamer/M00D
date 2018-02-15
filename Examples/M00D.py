"""
M00D.py
Neat litte aesthetic generator
by Dylan Hamer
"""

import random  # Used for choosing random colours and text
import click   # Used for clearing terminal and setting text colours
import time    # Used for delays
import sys     # Used for setting terminal title and exiting

"""Clears terminal - Designed to be used by parent application to initialise environment"""
def clear():
    click.clear()  # Clear terminal

def mood(**kwargs):
    colours = kwargs.get("colours", ["blue", "red"])             # Allowed text colours
    text = kwargs.get("text", ["m00d "])                         # Allowed text
    delay = kwargs.get("delay", 1)                               # Delay between each print
    title = kwargs.get("title", "M00D")                          # Terminal title

    sys.stdout.write("\x1b]2;{}\x07".format(title))       # Set terminal title

    currentColour = random.choice(colours)                # Choose a random colour
    currentText = str(random.choice(text))                # Choose some random text

    click.secho(currentText, fg=currentColour, nl=False)  # Print the random text in the random colour
    time.sleep(delay)                                     # Wait for the defined delay

"""Loop aesthetic generator"""
def loop(**kwargs):
    exitMessage = kwargs.get("exitMessage", "\n\nGoodbye!\n")  # Message to be displayed when CTRL-C is pressed
    while True:  # Loop forever
        try:
            mood(**kwargs)             # Run aesthetic generator with arguments
        except KeyboardInterrupt:    # If CTRL-C is pressed
            click.echo(exitMessage)  # Display exit message
            exit()                   # Exit


if __name__ == "__main__":  # If running as a standalone application
    loop()  # Run with default settings as a loop
