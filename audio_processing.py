import numpy as np
import scipy.io.wavfile as wav

def load_audio(filename):
    rate, signal = wav.read(filename)
    signal = signal / np.power(2, 15)
    return rate, signal
