EMOTION_INTERVAL = {
    "low":  [-1, 1],
    "mid":  [-2, 2, 3],
    "high": [4, 5, 7]
}

def choose_interval(emotion):
    return EMOTION_INTERVAL[emotion]
