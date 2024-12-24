Sentiment Analysis_WebArticles_Script

This script extracts and analyzes the sentiment of online news articles. 
It utilizes the TextBlob library for sentiment analysis and the Newspaper3k library for article scraping and summarization.

Features
* Scrapes online news articles using their URL.
* Extracts and summarizes the content of the article.
* Analyzes the sentiment of the summary using TextBlob.
  
Requirements

1. Python: Version 3.7 or higher.
2. Install the required libraries:
   pip install textblob / newspaper3k / nltk
3. Download NLTK resources:
   import nltk ->
   nltk.download('punkt_tab')

Usage
1. Clone this repository: git clone https://github.com/CristinaC-hub/ExcaliburRepos.git cd Project/Sentiment Analysis_TextFiles.py
2. Update the script to specify your desired article URL:
   url = 'https://example.com/your-article-link'
3. Run the script:
  Sentiment Analysis_WebArticles.py
4. View the output:
   - Article Summary: A concise overview of the article.
   - Sentiment Score:
       Positive score: Positive sentiment
       Negative score: Negative sentiment
       Score near 0: Neutral sentiment
   
Notes:

Ensure the URL points to a valid article.
If encountering issues with the newspaper3k library, ensure the lxml library is installed: pip install lxml.
