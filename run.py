from pipeline.generate_melody import generate_melody
from arrangement.full_song_generator import build_song

melody = generate_melody(model, section="chorus")

song = build_song(
    melody_degrees=melody,
    scale_notes=["C4","D4","E4","F4","G4","A4","B4"],
    chords_prog=[
        ["A3","C4","E4"],
        ["F3","A3","C4"],
        ["C4","E4","G4"],
        ["G3","B3","D4"]
    ]
)

song.write("midi", "jay_transformer.mid")
