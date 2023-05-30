#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input or enumerates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        
        for word in sys.argv[1:]:
            words.append(word)
            
        print(', '.join(words))
    else:
        print('Usage: python wordlist.py <words>')
    
