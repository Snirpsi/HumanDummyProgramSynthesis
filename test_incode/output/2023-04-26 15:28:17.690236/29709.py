#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words and stores words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        words.append(line.strip())
    
    # Convert words to lowercase
    words = [word.lower() for word in words]
    
    # Print the converted words
    for word in words:
        print(word)
        
