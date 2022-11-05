***Project Writeup and Reflection***

**1. Project Overview**

I used the Project Gutenberg data source to analyze the book: Heart of Darkness. This is one of my favorite novels and I love the introspective themes in it, therefore I wanted to run a sentiment analysis on this book and track the most commonly words used within it. I also wanted to conduct predictive analysis to see what algorithms I could generate to predict sentences or random words based on the text in this book. 

To conduct the sentiment analysis, I used the NLTK library to understand the overall sentiment mood of this text. I hope to be able to better understand how this book compares to other texts, in terms of number of words and common words, as well as its general sentimental analysis. My hypothesis is that the book generally has a neutral tone. 

As for the predictive analysis, I generated a function to predict random words from the book. I also improved this predictive functionality by using Markov analysis to generate predictive sentences based on user inputs, while also providing a few examples.

**2. Implementation**

The data for this book was originally stored in a text file from the Project Gutenberg link. However, I stored it in a dictionary to track the frequency of the words that appear in the book. In this function, I removed the header and cleaned up the data. I also tracked the total words and number of different words in a histogram dictionary. I chose to use a dictionary, as it would be easy to track the frequency of the words and also iterate through them. Moreover, dictionaries allow for easy readibility and are also fast in looking up a key. I also wrote separate functions to track the frequency of the most common words and to print it, to allow for customization of the print method, in terms of specifying how many common words could be printed (currently set to 10). I also excluded basic words from this function with the use of a separate file (stopwords.txt) that contains commonly used words in English novels. 

I also used natural language processing to calculate a sentiment score of this book. For this function, I used the NLTK Toolkit. While testing the initial code, I noticed that I had to create a separate function to clean the text and return it as a text file, as the original process function returns a dictionary. Therefore, I cleaned the data and returned it as a text. 

For the markov analysis, I was inspired by a github repo I saw that used a similar markov dictionary logic and adapted it for this project. First, I generated functions to gather all the words from the book and clean them. Then, I made a dictionary with the key being prefixes (defined by n length) with the value beign lists of those suffixes that follow the prefixes. Next, I generated suffixes based on the created markov dictionary and inputted prefix. The last function I created was the predictSentence function to append suffixes to the prefixes. I also added functionality for user input to customize prefixes and number of words to generate.

**3. Results**

The results indicate that there are 38,809 words, compared to an average of 60,000+ words for most novels. Therefore, this novel is relatively short. I also found it interesting that the most common words in this novel is "man," as it suits the overall theme of this book. The book revolves around the concept of introspection frequently and, therefore, the book commonly uses the words "man" and "men." I also found it interesting that the word "river" is frequently used, as the book mainly takes place on a river.

The next conclusion found was that the book is mainly neutral in terms of sentiment analysis, which supports its introspective theme, as I remember it using many neutral terms to allow the reader to form their own judgement. 

I also believe that the markov analysis was relatively successful in generating predictive sentences, as it matched the tone of the book.  

**4. Reflection**

I believe the organization of this book into a dictionary to track frequency of words went well, resulting in a successful basic analysis of the text. I also believe the NLP part of the text confirmed my hypothesis that the text is mainly neutral. That being said, I could have expanded the scope of this project by comparing it to other texts or analyzing specific parts within this text. I plan to my learning on this NLP aspect in my final project, where I aim to analyze data from a social media source. 

In hindsight, I wish I knew how data can be best structured in a NLP database, as I could have used abstraction to make my program more efficiently by establishing data cleaning functions.

I also believe that I could have expanded my Markov analysis by generating full sentences by calculating the average word length of sentences in the text.