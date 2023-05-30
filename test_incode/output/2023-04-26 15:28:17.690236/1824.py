#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words or calculates a list of words. """    
    words = []
    
    words = words + get_words()
    
    words = sorted(words)
    
    words = [w for w in words if w not in stopwords]
    
    words = [w for w in words if w not in punctuation]
    
    words = [w for w in words if w not in numbers]
    
    words = [w for w in words if w not in stopwords and w not in punctuation]
    
    words = [w for w in words if w not in numbers]
    
    words = [w for w in words if w not in stopwords and w not in punctuation and w not in numbers]
    
    words = [w for w in words if w not in stopwords and w not in punctuation and w not in numbers]
    
    words = [w for w in words if w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords]
    
    words = [w for w in words if w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers]
    
    words = [w for w in words if w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers]
    
    words = [w for w in words if w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in numbers and w not in stopwords and w not in punctuation and w not in number