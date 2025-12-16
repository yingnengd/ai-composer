import random
from config.jay_rules import SCALE_WEIGHT, MOTIFS
from melody.melody_constraints import valid_interval, valid_degree

def weighted_sample():
    degrees = list(SCALE_WEIGHT.keys())
    weights = list(SCALE_WEIGHT.values())
    return random.choices(degrees, weights)[0]


def generate_section(model, section, emotion, bars):
    melody = []
    last_degree = None
    last_interval = 0
    step = 0

    motif = random.choice(MOTIFS)

    for bar in range(bars):
        for deg in motif:
            candidate = model.predict_next_degree()
            candidate = candidate if random.random() < 0.6 else weighted_sample()

            interval = 0 if last_degree is None else candidate - last_degree
            strong_beat = (step % 1 == 0)

            if not valid_interval(last_interval, interval):
                continue
            if not valid_degree(candidate, strong_beat):
                continue

            melody.append((candidate, step))
            last_interval = interval
            last_degree = candidate
            step += 0.5

    return melody
