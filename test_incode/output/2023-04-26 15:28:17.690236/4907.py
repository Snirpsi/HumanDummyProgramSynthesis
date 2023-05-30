#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a port or iterates over words. """    
    
    port = sys.argv[1]
    
    words = []
    
    # Iterate over all words in the given port
    for word in range(port):
        words.append(word)
        
    # Print all words in the given port
    for word in words:
        print(word)
    
    # Print all words in the given port in reverse order
    for word in reversed(words):
        print(word)
    
    # Print all words in the given port in reverse order and print the first word
    for word in reversed(words):
        print(words[0])
    
    # Print all words in the given port in reverse order and print the first word and print the last word
    for word in reversed(words):
        print(words[-1])
    
    # Print all words in the given port in reverse order and print the first word and print the last word and print the first and last word
    for word in reversed(words):
        print(words[0], words[-1])
    
    # Print all words in the given port in reverse order and print the first word and print the last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and print the first and last word and 