import streamlit as st
import pickle
import numpy as np
from utils import clean_text
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load model
with open("model/fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

# App UI
st.set_page_config(page_title="Fake News Detector", layout="wide")
st.title("📰 Advanced Fake News Detection App")

st.markdown("Enter a news article, and the model will predict if it is **Fake** or **Real**, and show confidence scores.")

text_input = st.text_area("Enter News Article")

if st.button("Classify"):
    if text_input:
        cleaned = clean_text(text_input)
        prediction = model.predict([cleaned])[0]
        proba = model.predict_proba([cleaned])[0]

        label = "🟢 Real" if prediction == 1 else "🔴 Fake"
        st.markdown(f"### Prediction: **{label}**")
        st.progress(int(proba[prediction]*100))
        st.text(f"Confidence: {proba[prediction]*100:.2f}%")

        # WordCloud
        wc = WordCloud(background_color="white", max_words=100)
        wc.generate(cleaned)
        st.image(wc.to_array(), caption="WordCloud of Input Text")
    else:
        st.warning("Please enter text to analyze.")
