#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        for word in words:
            print(word*2)
    else:
        print('Usage: python wordlist.py word1 word2 word3 ...')
    
