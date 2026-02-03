import numpy as np
from scipy.io.wavfile import write

# Define frequencies for SA = 164.81 (E Base)
SA = 164.81
R  = SA * 9/8
G  = SA * 5/4
Gs = SA * 6/5
M  = SA * 4/3
Ms = SA * 45/32
P  = SA * 3/2
D  = SA * 5/3
N  = SA * 15/8

raag_notes = {
    "yaman": [N, R, G, Ms, P, D, N, SA*2],
    "des":   [SA, R, Gs, M, P, D, N, SA*2],
    "nand":  [SA, R, G, M, P, D, N, SA*2]
}

def gen_swarmandal(raag, dur=0.25):
    sr = 44100
    tone = np.array([])

    notes = raag_notes[raag]

    # Ascending
    for f in notes:
        t = np.linspace(0, dur, int(sr*dur))
        wave = 0.4*np.sin(2*np.pi*f*t)
        tone = np.concatenate((tone, wave))

    # Descending
    for f in reversed(notes):
        t = np.linspace(0, dur, int(sr*dur))
        wave = 0.4*np.sin(2*np.pi*f*t)
        tone = np.concatenate((tone, wave))

    write(f"{raag}.wav", sr, tone.astype(np.float32))
    print(f"\nGenerated → {raag}.wav")

raag = input("Enter raag (yaman/des/nand): ").strip().lower()

gen_swarmandal(raag)
