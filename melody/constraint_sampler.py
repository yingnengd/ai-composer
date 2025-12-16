import random
from melody.emotion_curve import EMOTION_INTERVAL

SCALE_WEIGHT = {
    1: 0.22, 2: 0.05, 3: 0.10,
    4: 0.06, 5: 0.28, 6: 0.20, 7: 0.01
}

def constrained_sample(candidates, last_degree, emotion, last_interval=0):
    allowed_intervals = EMOTION_INTERVAL[emotion]

    filtered = []
    for d in candidates:
        interval = abs(d - last_degree)
        if interval in allowed_intervals:
            if last_interval >= 5 and interval >= 5:
                continue
            filtered.append(d)

    if not filtered:
        filtered = candidates

    weights = [SCALE_WEIGHT.get(d, 0.01) for d in filtered]
    return random.choices(filtered, weights=weights)[0]
