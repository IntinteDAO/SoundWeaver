import aubio

# Load the audio file
filename = 'music.mp3'
hop_size = 1024
win_size = 1024

# Create aubio tempo object
samplerate = 0

# Open the audio file and read its samples
audio_file = aubio.source(filename, samplerate, hop_size)
samples, _ = audio_file()
tempo = aubio.tempo("default", win_size, hop_size, samplerate)

# Process the audio samples and detect beat notes
beat_notes = []
while True:
    samples, read = audio_file()
    if read < hop_size:
        break
    is_beat = tempo(samples)
    if is_beat:
        beat_notes.append(tempo.get_last_s())

# Print the detected beat notes
print("Beat notes (in seconds):", beat_notes)