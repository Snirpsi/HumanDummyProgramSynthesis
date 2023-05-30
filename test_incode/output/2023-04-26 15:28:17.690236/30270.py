#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        word = word.split()
        word = [word for word in word if word.isalpha()]
        word = [word for word in word if word.isdigit()]
        word = [word for word in word if word.islower()]
        word = [word for word in word if word.isupper()]
        word = [word for word in word if word.isalnum()]
        word = [word for word in word if word not in stopwords]
        word = [word for word in word if word not in punctuations]
        word = [word for word in word if word not in stopwords and word not in punctuations]
        word = [word for word in word if word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations]
        word = [word for word in word if word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations]
        word = [word for word in word if word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations]
        word = [word for word in word if word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations]
        word = [word for word in word if word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations]
        word = [word for word in word if word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopwords and word not in punctuations and word not in stopword