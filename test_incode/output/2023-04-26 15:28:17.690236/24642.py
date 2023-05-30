#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or calculates user input. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'word':
            word = input('Enter a word: ')
            
            print('The word is:', word)
            
        elif word == 'cal':
            word = input('Enter a word: ')
            
            print('The word is:', word)
            
        else:
            print('Invalid input.')
            
    else:
        print('Usage: python word