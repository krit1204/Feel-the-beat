import streamlit as st
import pandas as pd
import json
from src.process_lyrics import analyze_lyrics
from src.visualize_results import (
    plot_emotion_distribution,
    plot_emotion_timeline,
    generate_word_cloud,
    emoji_summary
)
from src.mood_tracker import save_emotion_to_tracker, get_emotion_history

st.set_page_config(page_title="Lyrics Emotion Analyzer", layout="wide")
st.title("🎶 Feel The Beat")
st.markdown("Upload a lyrics file to analyze the emotions and visualize the results interactively.")

uploaded_file = st.file_uploader("Upload Lyrics (.txt file)", type=["txt"])

if uploaded_file:
    file_path = f"temp_uploaded.txt"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    df = analyze_lyrics(file_path)
    st.subheader("Line-wise Emotion Analysis")
    st.dataframe(df, use_container_width=True)

    dominant_emotion = df['Emotion'].mode()[0]
    save_emotion_to_tracker(dominant_emotion)

    st.subheader("🌍 Emotion Distribution")
    plot_emotion_distribution(df)

    st.subheader("⏰ Time-Series Emotion Flow")
    plot_emotion_timeline(df)

    st.subheader(":cloud: Word Cloud")
    generate_word_cloud(df)

    st.subheader(":smile: Emoji Summary")
    st.write("Dominant Emotion Emoji:", emoji_summary(df))

    st.subheader("📈 Your Emotional Journey")
    emotion_counts = df["Emotion"].value_counts().sort_index()
    emotion_df = emotion_counts.reset_index()
    emotion_df.columns = ["Emotion", "Count"]
    emotion_df.set_index("Emotion", inplace=True)

    if not emotion_df.empty:
        st.write("This line graph shows the frequency of each emotion in the uploaded lyrics:")
        st.line_chart(emotion_df)
    else:
        st.write("No emotions detected in the uploaded lyrics.")

    st.subheader("📤 Export Your Emotional Data")
    export_button = st.button("Export Emotional Data")

    if export_button:
        emotion_history = get_emotion_history()
        emotion_data = {
            "dominant_emotion": dominant_emotion,
            "emotion_distribution": df['Emotion'].value_counts().to_dict(),
            "emotion_history": emotion_history.to_dict() if not emotion_history.empty else {}
        }

        st.write("Emotion Data to be exported:", emotion_data)
        export_filename = "emotional_data.json"
        with open(export_filename, "w") as f:
            json.dump(emotion_data, f) 

        st.success("Emotional data has been exported successfully!")
        st.download_button("Download Exported Data", export_filename, file_name=export_filename)

else:
    st.warning("Please upload a .txt file to get started.")
