"""
Raindrops.py
Raindrop aesthetic for M00D
by Dylan Hamer
"""

from M00D import mood

class raindrops:
    colours = ["blue", "cyan", "white"]
    text = ["drip ", "drop ", "splash "]
    title = "It\'s raining..."
    exitMessage = "\n\nIt has stopped raining. The sun is shining. In the distance, a rainbow is forming.\n"
    delay = 1

mood(colours = raindrops.colours,
     text = raindrops.text,
     delay = raindrops.delay,
     title = raindrops.title,
     exitMessage = raindrops.exitMessage)
