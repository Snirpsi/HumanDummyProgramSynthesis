#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    
    # Read words from file
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    # Remove punctuation
    words = [word.translate(None, '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') for word in words]
    
    # Remove duplicates
    words = list(set(words))
    
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    
    # Remove numbers
    words = [word for word in words if word not in numbers]
    
    # Remove punctuation
    words = [word.translate(None, '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') for word in words]
    
    # Remove duplicates
    words = list(set(words))
    
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    
    # Remove numbers
    words = [word for word in words if word not in numbers]
    
    # Remove punctuation
    words = [word.translate(None, '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') for word in words]
    
    # Remove duplicates
    words = list(set(words))
    
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    
    # Remove numbers
    words = [word for word in words if word not in numbers]
    
    # Remove punctuation
    words = [word.translate(None, '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') for word in words]
    
    # Remove duplicates
    words = list(set(words))
    
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    
    # Remove numbers
    words = [word for word in words if word not in numbers]
    
    # Remove punctuation
    words = [word.translate(None, '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~') for word in words]
    
    # Remove duplicates
    words = list(set(words))
    
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    
    # Remove numbers
    words = [word for word in words if word not in numbers]
    
    # Remove punctu