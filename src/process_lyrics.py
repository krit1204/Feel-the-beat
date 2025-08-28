import pandas as pd
from langdetect import detect
from transformers import pipeline
from src.emotion_predictor import predict_emotion

translation_models = {
    'hi': pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en"),
    'mr': pipeline("translation", model="Helsinki-NLP/opus-mt-mr-en"),
    'bn': pipeline("translation", model="Helsinki-NLP/opus-mt-bn-en"),
}

def translate_if_needed(text):
    """
    Translates non-English text to English if model is available.
    """
    lang = detect(text)
    if lang != 'en' and lang in translation_models:
        return translation_models[lang](text, max_length=512)[0]['translation_text']
    return text

def analyze_lyrics(file_path):
    """
    Reads a lyrics file, translates each line if necessary, and returns emotion predictions.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines if line.strip()]
    emotions = []
    scores = []

    for line in lines:
        translated_line = translate_if_needed(line)
        emotion, score = predict_emotion(translated_line)
        emotions.append(emotion)
        scores.append(score)

    df = pd.DataFrame({
        'Line': lines,
        'Emotion': emotions,
        'Confidence': scores
    })

    return df
