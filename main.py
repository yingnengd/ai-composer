from melody.transformer_stub import TransformerStub
from melody.transformer_sampler import generate_section
from config.song_structure import SONG_STRUCTURE
from midi.export import export_midi

model = TransformerStub()
song = []

for section, bars, emotion in SONG_STRUCTURE:
    song += generate_section(model, section, emotion, bars)

export_midi(song, "jay_style_song.mid")
print("🎵 MIDI generated: jay_style_song.mid")
