import re

inputFile1 = open ('xieb1_tweets_small.txt', 'r')
outputFile1 = open ('PreprocessedTweets.txt', 'w')
for line1 in inputFile1:
        pattern = re.compile('[^a-zA-Z ]*') #regular expression to identify all non-alphabetic characters except spaces
        line1 = re.sub (pattern,'',line1) #patterns which match the RE are replaced by a ' '
        line1 = line1.lower()
        outputFile1.write(line1 + '\n')

inputFile2 = open ('US-loc-names.txt', "r")
outputFile2 = open ('PreprocessedUS-loc-names.txt', 'w')
removeReplica=set()
for line2 in inputFile2:
        pattern = re.compile('[^a-zA-Z ]*') #regular expression to identify all non-alphabetic characters except spaces
        line2 = re.sub (pattern, '', line2) #patterns which match the RE are replaced by a ' '
        line2 = line2.lower()
        removeReplica.add(line2)


for element in removeReplica:
        outputFile2.write(element+'\n')

inputFile2.close()
outputFile2.close()