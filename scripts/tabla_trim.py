import librosa
import soundfile as sf

path = input("Enter tabla WAV/MP3 to trim: ")

audio, sr = librosa.load(path)

trimmed, indices = librosa.effects.trim(audio, top_db=25)

sf.write(path, trimmed, sr)
print("Trimmed and saved:", path)
