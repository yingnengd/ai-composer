from music21 import stream, chord, key

def harmonize(melody_degrees, key_name="C"):
    score = stream.Score()
    k = key.Key(key_name)
    score.insert(0, k)

    for deg, step in melody_degrees:
        pitch = k.pitchFromDegree(deg)
        c = chord.Chord([pitch])
        c.quarterLength = 0.5
        score.append(c)

    return score
