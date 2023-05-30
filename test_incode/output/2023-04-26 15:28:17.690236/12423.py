#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: %s <word>' % sys.argv[0])
        sys.exit(1)
    
    word = sys.argv[1]
    
    words = word.split()
    
    for word in words:
        if word not in stopwords:
            