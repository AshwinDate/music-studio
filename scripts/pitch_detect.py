import numpy as np
from scipy.io import wavfile
import librosa

def detect_pitch(audio_path):
    y, sr = librosa.load(audio_path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    pitch_values = pitches[magnitudes > np.median(magnitudes)]
    if len(pitch_values) == 0:
        return None

    return np.median(pitch_values)

file = input("Enter audio file path (wav/mp3): ")

pitch = detect_pitch(file)
print("\nDetected Frequency:", pitch, "Hz")
