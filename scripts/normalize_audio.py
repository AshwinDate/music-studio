import librosa
import soundfile as sf
import os
import numpy as np

folder = input("Enter folder path to normalize: ")

for file in os.listdir(folder):
    if file.endswith(".mp3") or file.endswith(".wav"):
        path = os.path.join(folder, file)
        audio, sr = librosa.load(path)
        audio = audio / np.max(np.abs(audio))  # Normalize
        sf.write(path, audio, sr)
        print("Normalized:", file)
