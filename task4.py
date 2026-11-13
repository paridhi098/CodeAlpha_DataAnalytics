import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download("vader_lexicon")


def perform_sentiment_analysis():
  reviews = [
      (
          "I absolutely love this product! It exceeded all my expectations and"
          " works wonderfully."
      ),
      (
          "Terrible quality. It broke after just two days of use. Complete"
          " waste of money."
      ),
      (
          "The item is okay. Nothing special, does the job but shipping took"
          " way too long."
      ),
      ("Amazing customer service and fast delivery! Highly recommended."),
      ("Awful experience. Will never buy from this company again."),
  ]

  df = pd.DataFrame(reviews, columns=["Review"])
  sia = SentimentIntensityAnalyzer()

  compound_scores = []
  sentiments = []

  for review in df["Review"]:
    score = sia.polarity_scores(review)["compound"]
    compound_scores.append(score)

    if score >= 0.05:
      sentiment = "Positive"
    elif score <= -0.05:
      sentiment = "Negative"
    else:
      sentiment = "Neutral"
    sentiments.append(sentiment)

  df["Compound_Score"] = compound_scores
  df["Sentiment"] = sentiments

  print("--- Sentiment Analysis Results ---")
  print(df)


if __name__ == "__main__":
  perform_sentiment_analysis()