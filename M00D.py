"""
M00D.py
Neat litte aesthetic generator
by Dylan Hamer
"""

import random, click, time, sys

"""Variables that modify the behaviour of the display"""
class variables:
    colours = ["blue", "cyan", "white"]
    text = ["drip ", "drop ", "splash "]
    delay = 1
    title = "It\'s raining..."

"""Aesthetic generator"""
def mood(**kwargs):
    colours = kwargs.get("colours", ["blue"])
    text = kwargs.get("text", ["m00d"])
    delay = kwargs.get("delay", 1)
    title = kwargs.get("title", "M00D")

    click.clear()

    sys.stdout.write("\x1b]2;{}\x07".format(title))

    while True:
        currentColour = random.choice(colours)
        currentText = random.choice(text)

        click.secho(currentText, fg=currentColour, nl=False)
        time.sleep(delay)

mood(colours = variables.colours,
     text = variables.text,
     delay = variables.delay,
     title = variables.title)
