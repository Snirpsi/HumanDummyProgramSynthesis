#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words or prints a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'word':
            word = input('Enter a word: ')
            
            print('The word is:', word)
        else:
            print('Usage: python word.py word')
    else:
        print('Usage: python word.py word')
    
