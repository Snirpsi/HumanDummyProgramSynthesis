#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and opens words. """    
    
    words = []
    with open('words.txt', 'r') as file:
        words = file.read().splitlines()
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) > 0]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]
    
    words = [word for word in words if word not in stopwords]