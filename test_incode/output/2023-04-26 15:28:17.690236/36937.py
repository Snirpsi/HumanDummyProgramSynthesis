#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    # Print the words in reverse order
    for word in reversed(words):
        print(word)
    
    # 