from textblob import TextBlob

with open('PositiveFeedback.txt','r') as f:   # +0.344
#with open('NegativeFeedback.txt','r') as f:  # -0.159
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #score: -1 most negative, 0 neutral, to 1 positive
print(sentiment)