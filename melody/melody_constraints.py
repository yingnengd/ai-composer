def valid_interval(last_interval, new_interval):
    if abs(last_interval) >= 5 and abs(new_interval) >= 5:
        return False
    return True


def valid_degree(degree, strong_beat):
    if degree == 7 and strong_beat:
        return False
    return True
