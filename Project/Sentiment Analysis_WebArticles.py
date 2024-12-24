import nltk
nltk.download('punkt_tab')

from textblob import TextBlob
from newspaper import Article

# url = 'https://www.cnbc.com/2024/12/23/meta-went-all-in-on-ai-in-2024-the-pressure-builds-in-2025.html' # 0.375 positive
url = 'https://moldovalive.md/electricity-imports-from-romania-are-higher-in-december-as-two-units-of-mgres-are-operating/' #-0.029 negative
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity #score: -1 most negative, 0 neutral, to 1 positive
print(sentiment)