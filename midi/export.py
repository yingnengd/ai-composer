from music21 import stream, note, midi

def export_midi(melody, filename="output.mid"):
    s = stream.Stream()

    for deg, step in melody:
        n = note.Note()
        n.pitch.midi = 60 + deg
        n.quarterLength = 0.5
        s.append(n)

    mf = midi.translate.streamToMidiFile(s)
    mf.open(filename, 'wb')
    mf.write()
    mf.close()
