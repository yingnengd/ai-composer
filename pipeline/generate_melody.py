def generate_melody(model, section, bars=8):
    melody = [5, 6, 5]  # motif seed

    while len(melody) < bars * 4:
        next_degree = model.predict_next_degree(melody)
        melody.append(next_degree)

    return melody
