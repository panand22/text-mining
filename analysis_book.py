
from concurrent.futures import process
import random
import string
import sys
from unicodedata import category

## Part 1: Harvesting text

import urllib.request

## Part 2: Analyzing Your Text

### Characterizing by Word Frequencies

## File exported as text file

def processText(filename,skip_header):
    '''
    Make histogram of words from book
    '''
    hist = {}
    text = open(filename, encoding='UTF8')

    if skip_header:
        skip_gutenberg_header(text)    

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in text:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()

            # update the histogram
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break

def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    total = 0
    for freq in hist.values():
        total+=freq
    return total

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

'''
### Computing Summary Statistics
Beyond simply calculating word frequencies there are some other ways to summarize the words in a text. For instance, what are the top 10 words in each text? What are the words that appear the most in each text that don't appear in other texts? 
'''
def mostCommon(hist, excludingBasicWords = True):
    '''
    Evaluates the 10 most common words using a historgram dictionary. Excludes basic words that are stored in stopwords.txt
    '''
    commonWords = []

    stopWords = processText('data/stopwords.txt',False) # from https://algs4.cs.princeton.edu/35applications/stopwords.txt
    stopWords = list(stopWords.keys())

    for word, freq in hist.items():
        if excludingBasicWords:
            if word in stopWords:
                continue

        commonWords.append((freq,word))
    
    commonWords.sort(reverse=True)
    return commonWords

def printCommonWords(hist,num):
    temp = mostCommon(hist)
    print('The most common words in this book are:')
    for freq, word in temp[:num]:
        print(word,'\t', freq)


### Natural Language Processing

from nltk.sentiment.vader import SentimentIntensityAnalyzer
'''
[NLTK](https://www.nltk.org/) - the Natural Language Toolkit - is a leading platform for building Python programs to work with human language data. It provides some really cool natural language processing capabilities. Some examples include: part of speech tagging, sentiment analysis, and full sentence parsing. 

To use NLTK, you need to install nltk by running the following command in **Command Prompt**:

pip install nltk
Here is an example of doing [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis):
'''

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def cleanText(skip_header):
    url = 'https://www.gutenberg.org/files/219/219-0.txt'
    with urllib.request.urlopen(url) as f:
        response = urllib.request.urlopen(url)
        data = response.read()  # a `bytes` object
        text = data.decode('utf-8')
        if skip_header:
            skip_gutenberg_header(text)
        strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in text:
        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()
        if line.startswith('*** END OF THIS PROJECT'):
            break
    return text

def nlpAnalysis():
    cleanText(skip_header=True)
    processedText = cleanText(skip_header=True)
    score = SentimentIntensityAnalyzer().polarity_scores(processedText)

    print("Sentiment Score: ", score)

def main():
    frequencyDict = processText('data/Heart of Darkness.txt',skip_header=True)
    print(frequencyDict)
        
    print('Total number of words:', total_words(frequencyDict))

    print()

    print('Number of different words:', different_words(frequencyDict))
    print()

    #prints the 10 most common words (excluding stop words)
    printCommonWords(frequencyDict,10)
    print()

    print('NATURAL LANGUAGE PROCESSING ANALYSIS:')
    nlpAnalysis()

if __name__ == '__main__':
    main()
