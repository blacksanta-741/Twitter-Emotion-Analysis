#For using it as a feature
from sklearn.feature_extraction.text import TfidfVectorizer

#Classifier
from sklearn.cluster import KMeans

from sklearn.metrics import adjusted_rand_score

#Handling csv files
import csv

import pandas as pd
from sklearn.model_selection import train_test_split

tweets_train = []
tweets_test = []
with open('Happy_out.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count > 500:
            break
        else:
            tweets_train.append(str(row))
            line_count += 1
print(tweets_train) 
with open('Sad_out.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count > 500:
            break
        else:
            tweets_train.append(str(row))
            line_count += 1


###################################
# START TRAINING
###################################   
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(tweets_train)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=1000, n_init=1)
model.fit(X)

##################################
# END TRAINING
##################################

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),

###################################
# START TESTING
###################################

#with open('Happy_out.csv') as csv_file:
#    csv_reader = csv.reader(csv_file,delimiter = ',')
#    line_count = 0
#            continue
#        elif line_count > 500 and line_count <1000:
#            tweets_test.append(str(row))
#            line_count += 1
#print(tweets_test)
#with open('Sad_out.csv') as csv_file:
#    csv_reader = csv.reader(csv_file,delimiter = ',')
#    for row in csv_reader:
#        if line_count < 500:
#            line_count += 1
#    line_count = 0
#    for row in csv_reader:
#        if line_count < 500:
#            line_count += 1
#            continue
#        elif line_count > 500 and line_count <1000:
#            print(tweets_test)
#            tweets_test.append(str(row))
#            line_count += 1
#print(tweets_test)

#for str1 in tweets_test:
#    print(str1)
#    Y = vectorizer.transform(str1)
#    prediction = model.predict(Y)
#    print(prediction)

Y = vectorizer.transform(["I am very not happy today...."])
prediction = model.predict(Y)
print(prediction)