def editDistance(str1,str2,weight=1):
    len1 = len(str1)
    len2 = len(str2)
    matrix=[[0]*(len2+1) for j in range(len1+1)]
    for i in xrange(len1+1):
        for j in xrange(len2+1):
            if min(i,j)==0:
                matrix[i][j]=max(i,j)
            else:
                addValue=0 if str1[i-1]==str2[j-1] else weight
                matrix[i][j] = min(matrix[i-1][j-1]+addValue,matrix[i-1][j]+1,matrix[i][j-1]+1)
    return matrix[len1][len2]

queryFile = open('PreprocessedUS-loc-names.txt', 'r')
opFile=open('xieb1_dataForGlobalEditDistance40.txt','w')
numresults = 1
threshold = 40#threshold for dissimilarity percentage

for query in queryFile:
    count = 0
    querylist = query.split()
    ipFile =  open('PreprocessedTweets.txt', 'r')

    for line in ipFile:
        names = line.split()


        tokens = zip(*[names[i:] for i in range(len(querylist))])  # list of strings with the same number of tokens as the query
        for i in range(0, len(tokens)):
            dissimilarity = []
            for j in range(0, len(querylist)):
                dissimilarity.append(((editDistance(querylist[j], tokens[i][j])) * 100) / len(querylist[j]))
            overallDissimilarity = sum(dissimilarity) / len(dissimilarity)
            if (overallDissimilarity < threshold):
                opFile.write("No.")
                opFile.write(str(numresults)+'\n')
                opFile.write("Query: ")
                opFile.write(query)
                opFile.write("Similarity:")
                opFile.write(str((100-overallDissimilarity))+'% \n')
                opFile.write("Approx. match: ")
                opFile.write(' '.join(tokens[i]) + '\n')
                tweets = open('xieb1_tweets_small.txt', 'r')
                tweetCount = 0
                for tweet in tweets:
                    if (tweetCount == count) and (len(tweet.split())>1):
                        opFile.write("Tweet ID: ")
                        opFile.write(str(tweet.split()[1]) + '\n')
                        break
                    tweetCount = tweetCount + 1
                opFile.write("Tweet: ")
                opFile.write(line + '\n\n')
                numresults = numresults + 1
                print query
                tweets.close()

        count = count + 1
    ipFile.close()



