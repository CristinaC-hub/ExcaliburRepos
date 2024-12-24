Sentiment Analysis_TextFiles_Script

This script uses the TextBlob library to perform sentiment analysis on text files. 
Sentiment analysis identifies whether the sentiment of the text is positive, neutral, or negative.

Features
* Reads text data from a specified file.
* Calculates the sentiment polarity of the text using TextBlob.
  
Outputs a sentiment score:
-1 : Most negative
 0 : Neutral
 1 : Most positive
 
Requirements
1. Python: Version 3.7 or higher.
2. Install TextBlob:
   (Run the following command to install the required library: pip install textblob)
   
Usage
1. Clone this repository:
   git clone https://github.com/CristinaC-hub/ExcaliburRepos.git 
   cd Project/Sentiment Analysis_TextFiles.py
2. Prepare a text file with the content you want to analyze
   Example files:
   PositiveFeedback.txt
   NegativeFeedback.txt
3. Update the script to specify your input file.
   //with open('PositiveFeedback.txt', 'r') as f://
4. Run the script: Sentiment Analysis_TextFiles.py
5. View the sentiment score:
   * Positive score: Positive sentiment;
   * Negative score: Negative sentiment;
   * Score near 0: Neutral sentiment;
