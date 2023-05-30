#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or converts fruits. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    words = list(set(words))
    
    words.sort()
    
    print(words)
    
    if len(words) == 1:
        print("No words found")
    else:
        print("\n".join(words))
    
