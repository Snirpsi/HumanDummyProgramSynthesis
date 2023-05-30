#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or converts fruits. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s <fruits>" % sys.argv[0])
        sys.exit()
    
    fruits = sys.argv[1:]
    
    words = []
    for fruit in fruits:
        words.extend(get_words(fruit))
    
    words.sort()
    
    for word in words:
        print(word)
    
