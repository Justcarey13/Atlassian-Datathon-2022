import csv
import regex
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

jira = r'(jira)'
confluence = r'(confluence)'
trello = r'(trello)'
bitbucket = r'(bitbucket)'
security = r'(bitbucket)'
fuzzy_jira = f'({jira}){{e<=1}}'
fuzzy_confluence = f'({confluence}){{e<=1}}'
fuzzy_trello = f'({trello}){{e<=1}}'
fuzzy_bitbucket = f'({bitbucket}){{e<=1}}'
fuzzy_security = f'({security}){{e<=1}}'

jira = {'count': 0, 'pos': 0, 'neg': 0, 'neu': 0}
confluence = {'count': 0, 'pos': 0, 'neg': 0, 'neu': 0}
trello = {'count': 0, 'pos': 0, 'neg': 0, 'neu': 0}
bitbucket = {'count': 0, 'pos': 0, 'neg': 0, 'neu': 0}
security = {'count': 0, 'pos': 0, 'neg': 0, 'neu': 0}
total = {'count': 0, 'pos': 0, 'neg': 0, 'neu': 0}

sia = SentimentIntensityAnalyzer()

with open('atlassian_twitter_dataset.csv', encoding="utf8") as twitter_data:
    reader = csv.reader(twitter_data, delimiter=',')
    for row in reader:
        jira_matches = regex.search(fuzzy_jira, row[2], regex.BESTMATCH)
        confluence_matches = regex.search(fuzzy_confluence, row[2], regex.BESTMATCH)
        trello_matches = regex.search(fuzzy_trello, row[2], regex.BESTMATCH)
        bitbucket_matches = regex.search(fuzzy_bitbucket, row[2], regex.BESTMATCH)
        security_matches = regex.search(fuzzy_security, row[2], regex.BESTMATCH)

        sent = sia.polarity_scores(row[2])
        total['count']+=1
        total['pos']+=sent['pos']
        total['neg']+=sent['neg']
        total['neu']+=sent['neu']

        if jira_matches:
            jira['count']+=1
            jira['pos']+=sent['pos']
            jira['neg']+=sent['neg']
            jira['neu']+=sent['neu']
        if confluence_matches:
            confluence['count']+=1
            confluence['pos']+=sent['pos']
            confluence['neg']+=sent['neg']
            confluence['neu']+=sent['neu']
        if trello_matches:
            trello['count']+=1
            trello['pos']+=sent['pos']
            trello['neg']+=sent['neg']
            trello['neu']+=sent['neu']
        if bitbucket_matches:
            bitbucket['count']+=1
            bitbucket['pos']+=sent['pos']
            bitbucket['neg']+=sent['neg']
            bitbucket['neu']+=sent['neu']
        if security_matches:
            security['count']+=1
            security['pos']+=sent['pos']
            security['neg']+=sent['neg']
            security['neu']+=sent['neu']

print(f'Total: {round((total["count"]/total["count"])*1000)/10}%', f'Pos: {round((total["pos"]/total["count"])*100)/100}', f'Neu: {round((total["neu"]/total["count"])*100)/100}', f'Neg: {round((total["neg"]/total["count"])*100)/100}')
print(f'Jira: {round((jira["count"]/total["count"])*1000)/10}%', f'Pos: {round((jira["pos"]/jira["count"])*100)/100}', f'Neu: {round((jira["neu"]/jira["count"])*100)/100}', f'Neg: {round((jira["neg"]/jira["count"])*100)/100}')
print(f'Confluence: {round((confluence["count"]/total["count"])*1000)/10}%', f'Pos: {round((confluence["pos"]/confluence["count"])*100)/100}', f'Neu: {round((confluence["neu"]/confluence["count"])*100)/100}', f'Neg: {round((confluence["neg"]/confluence["count"])*100)/100}')
print(f'Trello: {round((trello["count"]/total["count"])*1000)/10}%', f'Pos: {round((trello["pos"]/trello["count"])*100)/100}', f'Neu: {round((trello["neu"]/trello["count"])*100)/100}', f'Neg: {round((trello["neg"]/trello["count"])*100)/100}')
print(f'Bitbucket: {round((bitbucket["count"]/total["count"])*1000)/10}%', f'Pos: {round((bitbucket["pos"]/bitbucket["count"])*100)/100}', f'Neu: {round((bitbucket["neu"]/bitbucket["count"])*100)/100}', f'Neg: {round((bitbucket["neg"]/bitbucket["count"])*100)/100}')
print(f'Security: {round((security["count"]/total["count"])*1000)/10}%', f'Pos: {round((security["pos"]/security["count"])*100)/100}', f'Neu: {round((security["neu"]/security["count"])*100)/100}', f'Neg: {round((security["neg"]/security["count"])*100)/100}')
