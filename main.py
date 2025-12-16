from src.audio_processing import load_audio
from src.feature_extraction import extract_mfcc
from src.acoustic_model import train_acoustic_model
from src.decoder import decode_with_vosk
from src.evaluation import word_error_rate

if __name__ == "__main__":
    filename = "data/sample_audio.wav"
    rate, signal = load_audio(filename)
    features = extract_mfcc(signal, rate)
    model = train_acoustic_model(features)
    decoded = decode_with_vosk(filename)
    wer = word_error_rate("hello how are you", decoded)
    print("Decoded:", decoded)
    print("WER:", wer)
