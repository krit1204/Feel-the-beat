from transformers import pipeline

emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def predict_emotion(text_line):
    """
    Predicts the dominant emotion and confidence for a given English line.
    """
    result = emotion_pipeline(text_line)[0]
    top_emotion = max(result, key=lambda x: x['score'])
    return top_emotion['label'], top_emotion['score']
