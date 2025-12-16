from music21 import stream, note, chord

def build_song(melody_degrees, scale_notes, chords_prog):
    s = stream.Score()

    melody = stream.Part()
    harmony = stream.Part()
    bass = stream.Part()
    pad = stream.Part()

    # 🎵 Melody
    for d in melody_degrees:
        melody.append(note.Note(scale_notes[d-1], quarterLength=1))

    # 🎹 Chords
    for c in chords_prog:
        harmony.append(chord.Chord(c, quarterLength=4))
        pad.append(chord.Chord(c, quarterLength=4))

    # 🎸 Bass
    for c in chords_prog:
        bass.append(note.Note(c[0] - 12, quarterLength=4))

    s.insert(0, melody)
    s.insert(0, harmony)
    s.insert(0, bass)
    s.insert(0, pad)

    return s
