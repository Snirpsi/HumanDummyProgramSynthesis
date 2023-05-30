#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or opens user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = input("Enter a word: ")
        
    print("Opening word: {}".format(word))
    
    