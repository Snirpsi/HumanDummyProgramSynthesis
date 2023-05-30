#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and multiplyes a port. """    
    port = int(sys.argv[1])
    words = []
    
    for word in sys.argv[2:]:
        words.append(word.lower())
    
    words.sort()
    
    for word in words:
        