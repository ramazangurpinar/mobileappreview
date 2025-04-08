# 📊 Dataset Overview: Google Play Store Reviews

## 🎯 Project Context

This project is part of the thesis:  
**"AI App to Automatically Classify and Analyse Mobile App Reviews"**  
The goal is to **design and implement an AI-based system** that can **automatically classify** app store reviews and **analyze user feedback** using Natural Language Processing (NLP).

---

## 📁 Dataset Source

- **Platform:** Google Play Store
- **Collected via:** Google Play Store Scraper Library
- **Data Format:** CSV
- **Total Records:** ~12,495 rows
- **License:** Public domain (CC0)

This dataset includes **real user reviews** from mobile apps available on Google Play. It contains text reviews, ratings (1–5 stars), review dates, and developer replies, making it ideal for **supervised learning and sentiment analysis** tasks.

---

## ✅ Why This Dataset is Suitable for the Thesis

| Thesis Objective              | Dataset Match |
|------------------------------|----------------|
| Automatic classification     | ⭐ Yes – Ratings and text can be used as labels |
| Review analysis              | ⭐ Yes – NLP-based insights possible |
| AI application design        | ⭐ Yes – ML/NLP models can be trained |
| Performance evaluation       | ⭐ Yes – Use metrics like Accuracy, F1-Score |
| Real-world data              | ⭐ Yes – Authentic user reviews from app store |

---

## 🧠 Potential Use Cases in Thesis

| Section             | Application                                                             |
|---------------------|--------------------------------------------------------------------------|
| **Data Source**     | Google Play Store Reviews (via Kaggle or scraping library)              |
| **Preprocessing**   | Cleaning, tokenization, stop word removal                               |
| **Feature Extraction** | TF-IDF, Word2Vec, BERT embeddings                                  |
| **Classification**  | Logistic Regression, Naive Bayes, SVM, or Transformer-based models      |
| **Evaluation**      | Accuracy, Precision, Recall, F1-score                                   |
| **Extra Analysis**  | Word clouds, time-based trends, most common complaints                  |

---

## 🧾 Column Descriptions

| Column Name          | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `reviewId`           | Unique ID of the review                                                     |
| `userName`           | Username of the reviewer                                                    |
| `userImage`          | Profile image URL of the reviewer                                           |
| `content`            | Text of the review – 🌟 **Main text for sentiment analysis**               |
| `score`              | Rating score (1 to 5) – 🌟 **Can be used as label for classification**     |
| `thumbsUpCount`      | Number of users who found the review helpful                                |
| `reviewCreatedVersion` | App version at the time of review                                        |
| `at`                 | Review timestamp                                                            |
| `replyContent`       | Developer’s reply (if any)                                                  |
| `repliedAt`          | Timestamp of developer’s reply                                              |
| `sortOrder`          | Review order (e.g., "newest")                                               |
| `appId`              | App identifier (e.g., com.anydo)                                            |

---

## 🌟 Key Columns for AI Analysis

| Objective                      | Recommended Columns            |
|-------------------------------|--------------------------------|
| **Sentiment Analysis**        | `content`, `score` (labeling: 1-2 = negative, 4-5 = positive) |
| **Review Content Analysis**   | `content`                      |
| **Time Series Insights**      | `at`                           |
| **Developer Interaction**     | `replyContent`, `repliedAt`   |
| **App-Level Comparison**      | `appId`                        |

---

## ✍️ Notes

- The dataset contains **no personally identifiable information**, making it **ethically safe** for academic use.
- Data volume (~12k reviews) is sufficient for training, validation, and testing of machine learning models.
- Developer replies provide additional context that could be used for **response analysis** or **customer support effectiveness** studies.

---

> 📌 This markdown file serves as a structured overview of the dataset and how it aligns with the thesis goals. You can include this in the `/notebooks/` or `/docs/` directory in your GitHub repo.
