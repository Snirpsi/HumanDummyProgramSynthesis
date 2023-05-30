#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens user input or prints words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'quit':
            sys.exit()
        else:
            print(word)
    else:
        print('Usage: python words.py')
        
