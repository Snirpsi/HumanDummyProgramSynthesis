#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a list of words. """    
    import sys
    words = sys.argv[1:]
    
    for word in words:
        words = words.split()
        
        for word in words:
            if word.lower() not in stopwords and len(word) > 2:
                