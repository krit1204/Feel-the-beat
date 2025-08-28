from src.process_lyrics import analyze_lyrics
from src.visualize_results import plot_emotion_distribution, plot_emotion_timeline, generate_word_cloud, emoji_summary

lyrics_file = 'sample_lyrics.txt'
df = analyze_lyrics(lyrics_file)
print(df)

plot_emotion_distribution(df)
plot_emotion_timeline(df)
generate_word_cloud(df)
print("\n🎵 Dominant Emotion Emoji:", emoji_summary(df))
