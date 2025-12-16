import random

def rhythm_offset(step, section):
    if section in ["verse", "intro"]:
        return step + random.choice([0.25, 0.5])
    if section in ["chorus", "final"]:
        return round(step)
    return step
