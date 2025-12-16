from python_speech_features import mfcc

def extract_mfcc(signal, rate):
    return mfcc(signal, samplerate=rate, numcep=13)
