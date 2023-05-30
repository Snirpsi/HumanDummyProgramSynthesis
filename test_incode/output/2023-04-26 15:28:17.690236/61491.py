#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and converts numbers. """    
    words = []
    for word in wordlist:
        words.append(word.lower())
    
    words = [word for word in words if word.isalpha()]
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word not in stopwords]
    
    return words

<|/ file filename=wordlist.py source=github |>