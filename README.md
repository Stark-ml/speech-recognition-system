# Speech Recognition System

## Overview
This project implements a basic speech recognition pipeline using classical signal
processing and machine learning techniques. The system processes raw audio signals,
extracts Mel-Frequency Cepstral Coefficients (MFCC), trains an acoustic model using
Gaussian Mixture Models (GMM), and performs speech decoding using the Vosk toolkit.

The project is developed for academic and educational purposes and demonstrates the
core components of a traditional Automatic Speech Recognition (ASR) system.

---

## System Pipeline
The speech recognition system follows these main steps:

1. Audio loading and normalization
2. Power spectrum analysis
3. MFCC feature extraction
4. Acoustic modeling using Gaussian Mixture Models (GMM)
5. Simple bigram language modeling
6. Speech decoding using Vosk
7. Performance evaluation using Word Error Rate (WER)

---

## Technologies Used
- Python
- NumPy
- SciPy
- Matplotlib
- python_speech_features
- scikit-learn
- Vosk Speech Recognition Toolkit
