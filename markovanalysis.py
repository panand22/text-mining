from concurrent.futures import process
from string import punctuation
from string import whitespace
from analysis_book import*
import numpy as np

import urllib.request

# GLOBAL VARIABLE of url to book
url = 'https://www.gutenberg.org/files/219/219-0.txt'

def gatherWords(url):
    '''
    Gathers all the words in the book
    '''
    with urllib.request.urlopen(url) as f:
        words = f.read().decode('utf-8').split('***')[2]
        words = words.split()
    return words


def cleanWord(word):
    '''
    Function "cleans" word by removing punctuation and whitepsace from input string: word
    '''
    cleanedWord = ''
    for char in word:
        if ((char in whitespace) or (char in punctuation)):
            pass
        else:
            cleanedWord += char.lower()
    return cleanedWord

def make_markov_dict(cleanedWords, n):
    '''
    Function creates dictionary of words with:
        Key: Prefixes (number of words defined by n)
        Value: lists of suffixes that follow prefixes

    Code inspired by Github function that used a similar markov dictionary for a different source. Adapted for Project Gutenberg book.
    '''
    preList = []
    for i in range(len(cleanedWords) - n):
        preList.append(cleanedWords[i:i+n+1])
    markovDict = {}
    for _ in preList:
        strings = _[0]
        for i in range (1,n):
            strings = strings + ' ' + _[i]
        if strings not in markovDict:
            markovDict[strings] = [_[n]]
        else:
            markovDict[strings].append(_[n])

    return markovDict

def generate_suffixes(markovDict, prefix):
    '''
    Generates "suffixes" by returning list of sorted tuples (suffix, count) that correspond to prefix input.

    Got logic from same github repo that used markov dictionary to analyze a book from another source. Adapted for this project.
    '''
    tupList = []
    seenList = []

    for _ in markovDict[prefix]:
        if _ not in seenList:
            seenList.append(_)
            tupList.append((_, markovDict[prefix].count(_)))
    sortedTups = sorted(tupList, key = lambda x: x[1], reverse = True)
    
    return sortedTups

def predictSentence(cleanedWords,prefix,n):
    '''
    Returns a predicted sentence with prefix string and n: number of words you want to generate after prefix
    '''
    sentenceDict = make_markov_dict(cleanedWords,len(prefix.split()))
    prefix = prefix.lower()

    sentence = prefix # initialize sentence

    for _ in range(n-1):
        sortedTups = generate_suffixes(sentenceDict, prefix)
        words, nums = list(zip(*sortedTups)) # produces list of frequncies for random choice
        denominator = sum(nums)
        probs = [_ / denominator for _ in nums]
        suffix = np.random.choice(words, p = probs) 

        sentence = sentence + ' ' +  suffix #add suffix
        
        prefix = sentence.split()[-len(prefix.split()):] 
        # this above line redefines prefix to input

        prefix = (' ').join(prefix)  
    return sentence

def markovMain():
    # url = https://www.gutenberg.org/files/219/219-0.txt'
    words = gatherWords(url)
    cleanedWords = [cleanWord(word) for word in words]

    print('MARKOV ANALYSIS:')
    print()

    print('This will predict a sentence using a chosen prefix. Here are some examples:')
    print()
    ## EXAMPLES:
    print(predictSentence(cleanedWords, 'One evening', 40))
    print()
    print(predictSentence(cleanedWords, 'The sky', 30))
    print()
    print(predictSentence(cleanedWords, 'He said', 20))
    print()
    
    prefixInput = input('Enter a prefix to predict a sentence.\n')

    numWordsInput = int(input('How many words do you want to predict?\n'))

    print(predictSentence(cleanedWords, prefixInput, numWordsInput))


# if __name__ == '__main__':
#     main()

