#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        for word in words:
            print(word)
    else:
        print('usage: python3 addword