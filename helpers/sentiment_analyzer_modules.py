from pattern.en import sentiment, positive

def get_sentiment_result(text):
    sentiment_result = sentiment(text)
    is_sentiment_positive = positive(sentiment_result, threshold=sentiment_threshold)
    return ["negative", "positive"][is_sentiment_positive]
