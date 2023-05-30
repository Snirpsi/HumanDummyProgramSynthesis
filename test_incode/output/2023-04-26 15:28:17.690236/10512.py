#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or adds words. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        if word == 'help':
            print('''
            word.py
            
            Calculates the number of words in a text file.
            
            Adds words to a text file.
            
            Quits the program.
            
            ''')
            
        elif word == 'add':
            print('''
            word.py
            
            Adds words to a text file.
            
            Quits the program.
            
            ''')
            
        else:
            print('''
            word.py
            
            Calculates the number of words in a text file.
            
            Adds words to a text file.
            
            Quits the program.
            
            ''')
            
