```markdown
# 📰 Fake News Detection

A Streamlit-powered web application that detects **fake news** using machine learning (Logistic Regression) and advanced NLP preprocessing. Built using Python, scikit-learn, and Streamlit.

---

## 🚀 Features

- ✅ Detect fake vs real news articles.
- 📊 Show confidence scores for predictions.
- ☁️ Generate word clouds from input news.
- 🔍 Clean, preprocess, and classify news text.
- 🎛️ Hyperparameter tuning with GridSearchCV.

---

## 📁 Project Structure

```

fake\_news\_detection/
├── app.py                   # Streamlit application
├── train\_model.py           # Model training script
├── utils.py                 # Text cleaning utility
├── model/
│   ├── fake\_news\_model.pkl  # Trained ML model
│   └── vectorizer.pkl       # Saved TF-IDF vectorizer
├── data/
│   ├── fake.csv             # Fake news samples
│   └── true.csv             # Real news samples
├── visuals/
│   └── wordcloud.png        # Optional saved visuals
└── requirements.txt         # Python dependencies

````

---

## 📦 Installation

### 🧱 Requirements

- Python 3.7+
- pip

### 🔧 Setup

```bash
# Clone the repository
git clone [https://github.com/iamdpsingh/Fake-News-Detection.git]
cd Fake-News-Detection

# Install dependencies
pip install -r requirements.txt
````

---

## 📊 Model Training

Make sure your datasets (`fake.csv`, `true.csv`) are in the `data/` directory.

Then run:

```bash
python train_model.py
```

This will:

* Combine and clean the dataset
* Train a Logistic Regression model using GridSearchCV
* Save the model and vectorizer in `model/`

---

## 🖥️ Run the Web App

After training, start the Streamlit app:

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📌 Example

Paste any news article into the app, click **Classify**, and get:

* Prediction (`Fake` or `Real`)
* Confidence score
* WordCloud of input

---

## 🧠 Technologies Used

* Python 🐍
* Streamlit ⚡
* Scikit-learn 🤖
* WordCloud ☁️
* Matplotlib 📊
* Pandas 🐼

---

## 🔮 Future Improvements

* Use transformer models (BERT, RoBERTa) for better accuracy
* Add PDF/newsfeed ingestion
* Provide SHAP model interpretability
* Deploy to Hugging Face/Streamlit Cloud

---

## 🙌 Acknowledgements

* [Kaggle Fake News Dataset](https://www.kaggle.com/datasets/bhavikjikadara/fake-news-detection)
* Streamlit & scikit-learn communities

```
