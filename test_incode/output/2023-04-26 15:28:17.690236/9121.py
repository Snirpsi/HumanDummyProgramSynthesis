#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and opens words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        exit(1)
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    webserver.run(words)
    
