import pandas as pd
import datetime

def save_emotion_to_tracker(emotion_data, user_id="user"):
    """ Save the emotion data to a CSV file. """
    filename = f"{user_id}_emotion_tracker.csv"
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["timestamp", "emotion"])
    
    new_data = pd.DataFrame({"timestamp": [datetime.datetime.now()], "emotion": [emotion_data]})
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(filename, index=False)
    print(f"Emotion saved to {filename}.")

def get_emotion_history(user_id="user"):
    """ Retrieve emotion history from the CSV file. """
    filename = f"{user_id}_emotion_tracker.csv"
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["timestamp", "emotion"])
