import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st

def plot_emotion_distribution(df):
    emotion_counts = df['Emotion'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=emotion_counts.index, y=emotion_counts.values, palette="Set2", ax=ax)
    ax.set_title("Overall Emotion Distribution")
    ax.set_ylabel("Frequency")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

def plot_emotion_timeline(df):
    emotion_map = {'joy': 0, 'sadness': 1, 'anger': 2, 'fear': 3, 'love': 4, 'surprise': 5}
    df['EmotionNum'] = df['Emotion'].map(emotion_map)
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.lineplot(x=df.index, y=df['EmotionNum'], marker='o', ax=ax)
    ax.set_title("Emotion Timeline Over Lyrics")
    ax.set_xlabel("Line Number")
    ax.set_ylabel("Emotion")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

def generate_word_cloud(df):
    all_text = ' '.join(df['Line'].tolist())
    wc = WordCloud(width=800, height=400, background_color='white').generate(all_text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    ax.set_title("Word Cloud from Lyrics")
    st.pyplot(fig)

def emoji_summary(df):
    emoji_dict = {
        'joy': '😊', 'sadness': '😢', 'anger': '😠',
        'fear': '😨', 'love': '❤️', 'surprise': '😲'
    }
    top_emotion = df['Emotion'].value_counts().idxmax()
    return emoji_dict.get(top_emotion.lower(), '🎵')
