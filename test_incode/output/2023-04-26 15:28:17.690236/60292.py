#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or multiplyes user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
        
        if word == 'word':
            word = input('Enter a word: ')
            
            print(word*3)
        elif word == 'multiply':
            word = input('Enter a word: ')
            
            print(word*3)
        else:
            print('Invalid input')
    else:
        print('Invalid input')
