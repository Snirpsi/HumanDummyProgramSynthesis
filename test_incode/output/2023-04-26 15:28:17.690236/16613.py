#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores words. """    
    words = []
    with open('words.txt', 'r') as f:
        words = f.readlines()
    words = [word.strip() for word in words]
    words = [word.lower() for word in words]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
    words = [word for word in words if word not in stopwords]
    words = [word for word in words if len(word) > 2]
    words = [word for word in words if len(word) > 1]
    words = [word for word in words if len(word) > 0]
