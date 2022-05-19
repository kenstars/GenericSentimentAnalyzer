from pattern.en import sentiment, positive
sentiment_threshold = 0.1

def get_sentiment_result(text):
    """
    Creates a sentiment value to the given dataset
    """
    sentiment_result = sentiment(text)
    is_sentiment_positive = positive(sentiment_result, threshold=sentiment_threshold)
    return ["negative", "positive"][is_sentiment_positive]


if __name__ == "__main__":
    import pandas as pd
    import os
    all_csv_files = [each_file for each_file in os.listdir("data/") if each_file.endswith("csv") and each_file.startswith("tweets")]
    for each_file in all_csv_files:
        df = pd.read_csv(f"data/{each_file}", index = False)
        df["sentiment"] = df["text"].apply(get_sentiment_result)
        df.to_csv(f"data/{each_file}", index = False)
