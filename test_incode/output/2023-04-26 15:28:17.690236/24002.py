#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words or prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'help':
            print('Usage: python wordlist.py <word>')
            sys.exit(0)
        
        if word == 'list':
            print('\n'.join(wordlist))
            sys.exit(0)
    
    else:
        print('Usage: python wordlist.py <word>')
        sys.exit(1)
    
