#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words or prints user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = input("Enter words: ")
    
    for word in words:
        print(word)
        
