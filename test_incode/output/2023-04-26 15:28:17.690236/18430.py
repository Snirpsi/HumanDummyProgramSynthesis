#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints numbers and iterates over a list of words. """    
    words = ['cat', 'dog', 'mouse']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('\nDo you want to continue (y/n)?