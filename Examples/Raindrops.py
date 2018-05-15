"""
Raindrops
Raindrop aesthetic for M00D
by Dylan Hamer
"""

from . import mood

"""Dictionary defining generator"""
raindrops = {"colours":["blue", "cyan", "white"],
            "text":["drip ", "drop ", "splash "],
            "title":"It\'s raining...",
            "exitMessage":"\n\nIt has stopped raining. The sun is shining. In the distance, a rainbow is forming.\n",
            "delay":0.1}

mood.clear()

mood.loop(**raindrops)  # Run loop with argument dictionary
