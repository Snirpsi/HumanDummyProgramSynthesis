#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words and returns a list of numbers. """    
    import sys
    
    wordlist = sys.argv[1]
    numberlist = list(map(int,wordlist.split()))
    
    print(numberlist)
    
    

<|/ file source=github |>