#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a list of words or prints user input. """    
    
    words = []
    
    # Read words from stdin and add to list
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    # Print user input
    for word in words:
        print(word)
        
    # Print list of words
    for word in words:
        print(word)
        
    # Print list of words in reverse order
    for word in reversed(words):
        print(word)
        
    # Print list of words in reverse order and print 