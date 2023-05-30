#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and returns a port. """    
    port = 0
    
    while True:
        port = port + 1
        
        # Remove all words and return the port.
        words = input("Enter a word: ")
        
        # Remove all spaces and return the port.
        words = words.split()
        
        # Remove all punctuation and return the port.
        words = filter(lambda x: x not in string.punctuation, words)
        
        # Remove all stopwords and return the port.
        words = filter(lambda x: x not in stopwords, words)
        
        # Remove all words that only contain letters and return the port.
        words = filter(lambda x: len(x) <= 3, words)
        
        # Remove all words that only contain numbers and return the port.
        words = filter(lambda x: len(x) <= 5, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 7, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 9, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 11, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 13, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 15, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 17, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 19, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 21, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 23, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 25, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 27, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 29, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 31, words)
        
        # Remove all words that only contain letters and numbers and return the port.
        words = filter(lambda x: len(x) <= 33, words)
        
        # Remove all words that only contain letter