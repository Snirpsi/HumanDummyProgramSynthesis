#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words or stores user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        wordlist = sys.argv[1:]
    else:
        wordlist = ['hello', 'world', '!']
    
    for word in wordlist:
        print(word)
    
