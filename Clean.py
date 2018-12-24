from textblob import TextBlob  

#for working with csv files
import csv

# for regular expressions
import re   

#for sorting dictionaries
import operator
import 
# Intialize an empty list to hold all of our tweets
tweets = []
final = []

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    #stripped = string.decode("utf-8").encode("ascii", "ignore")
    return ''.join(stripped)

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', " ", tweet).split())


with open('Tweets.csv','r',encoding='ascii') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')

    for row in reader:
        tweet = dict()
        tweet["original"] = row 

        if re.match(r'^rt.*', tweet['original']):
            continue
        print('Original Tweet : ' + tweet["original"])
        tweet["clean"] = tweet["original"]


          # Remove all non-ascii characters
        tweet['clean'] = strip_non_ascii(tweet['clean'])

        # Normalize case
        tweet['clean'] = tweet['clean'].lower()
        tweet['clean'] = re.sub(r'([a-zA-Z0-9]*\\[a-zA-Z0-9]*)+', "", tweet['clean'])
        tweet['clean'] = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet['clean'])
        tweet['clean'] = re.sub(r'\b(rt)\b', '', tweet['clean'])
        tweet['clean'] = re.sub(r'\bthats\b', 'that is', tweet['clean'])
        tweet['clean'] = re.sub(r'\bthat\'s\b', 'that is', tweet['clean'])
        tweet['clean'] = re.sub(r'\bive\b', 'i have', tweet['clean'])
        tweet['clean'] = re.sub(r'\biv\'e\b', 'i have', tweet['clean'])
        tweet['clean'] = re.sub(r'\bim\b', 'i am', tweet['clean'])
        tweet['clean'] = re.sub(r'\bi\'m\b', 'i am', tweet['clean'])
        tweet['clean'] = re.sub(r'\bya\b', 'yeah', tweet['clean'])
        tweet['clean'] = re.sub(r'\byea\b', 'yeah', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcant\b', 'cannot', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcan\'t\b', 'cannot', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwont\b', 'will not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwon\'t\b', 'will not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bid\b', 'i would', tweet['clean'])
        tweet['clean'] = re.sub(r'wtf', 'what the fuck', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwth\b', 'what the hell', tweet['clean'])
        tweet['clean'] = re.sub(r'\br\b', 'are', tweet['clean'])
        tweet['clean'] = re.sub(r'\bu\b', 'you', tweet['clean'])
        tweet['clean'] = re.sub(r'\bk\b', 'OK', tweet['clean'])
        tweet['clean'] = re.sub(r'\bsux\b', 'sucks', tweet['clean'])
        tweet['clean'] = re.sub(r'\bno+\b', 'no', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcoo+\b', 'cool', tweet['clean'])
        tweet['clean'] = re.sub(r'\bn\b', 'in', tweet['clean'])
        tweet['clean'] = re.sub(r'[^o\x00-\x7F]+', '', tweet['clean']) 


        # Create textblob object
        tweet['TextBlob'] = TextBlob(tweet['clean'])
        tweet['clean2'] = clean_tweet(tweet['clean'])
        tweet['TextBlob2'] = TextBlob(tweet['clean2'])

        print(tweet['TextBlob2'])
        a = str(tweet['TextBlob2'])
        print("a: "+a)
        final.append(a)
        tweets.append(tweet)

print(final)

with open("Clean.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in final:
        writer.writerow([val])