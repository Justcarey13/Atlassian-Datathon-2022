import csv
import regex
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from operator import itemgetter
import json

nltk.download('vader_lexicon')

confluence = r'(confluence)'
fuzzy_confluence = f'({confluence}){{e<=1}}'

sia = SentimentIntensityAnalyzer()
confluence_negative_tweet = []
with open('atlassian_twitter_dataset.csv', encoding="utf8") as twitter_data:
    reader = csv.reader(twitter_data, delimiter=',')
    for row in reader:
        confluence_matches = regex.search(fuzzy_confluence, row[2], regex.BESTMATCH)
        sent = sia.polarity_scores(row[2])
        if confluence_matches:
            if (sent['neg'] > 0): confluence_negative_tweet.append(row)
            
most_favorites = sorted(confluence_negative_tweet, key=itemgetter(3)) 
print(json.dumps(most_favorites[-10:], indent=4)) # Get top ten