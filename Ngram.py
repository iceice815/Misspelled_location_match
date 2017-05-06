import re

queryFile = open('PreprocessedUS-loc-names.txt', 'r')
opFile=open('xieb1_dataForNgram3_60.txt','w')
# numresults = 0
n = 3  # value of n to form ngrams
numresults=1
threshold = 60  # threshold for similarity percentage
for query in queryFile:
    querylist = query.split()
    numNgramsPattern = len(zip(*[''.join(querylist)[i:] for i in range(n)]))  # list of ngrams in the pattern query
    lineCount = 0
    ipFile = open('PreprocessedTweets.txt', 'r')
    for line in ipFile:
        words = line.split()
        strings = zip(
            *[words[i:] for i in range(len(querylist))])  # list of strings with the same number of tokens as the query
        for token in strings:
            string = ''.join(token)
            ngrams = zip(*[string[i:] for i in range(n)])  # list of ngrams in the string
            numNgrams = len(ngrams)
            count = 0
            for ngram in ngrams:
                ng = ''.join(ngram)
                if re.search(ng, ''.join(querylist)):  # searching for the presence of ngram in the pattern
                    count = count + 1
            if (numNgrams != 0 and numNgramsPattern !=0 and (count * 100 / numNgramsPattern) > threshold):
                opFile.write("No.")
                opFile.write(str(numresults)+'\n')
                opFile.write("Query: ")
                opFile.write(' '.join(token) + '\n')
                opFile.write(query )
                opFile.write("Similarity:")
                opFile.write(str((count * 100 / numNgramsPattern))+'% \n')
                opFile.write("Approx. match: ")
                tweets = open('xieb1_tweets_small.txt', 'r')
                tweetCount = 0
                for tweet in tweets:
                    if (tweetCount == lineCount) and (len(tweet.split())>1):
                        opFile.write("Tweet ID: ")
                        opFile.write(str(tweet.split()[1]) + '\n')
                        break
                    tweetCount = tweetCount + 1
                opFile.write("Tweet: ")
                opFile.write(line + '\n\n')
                numresults = numresults + 1
                print query
                tweets.close()
        lineCount = lineCount + 1
    ipFile.close()

