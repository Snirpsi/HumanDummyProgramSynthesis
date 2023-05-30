#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    
    while True:
        for word in words:
            print(word)
            
        choice = input('\nDo you want to play again? [y/N] ')
        if choice.lower() == 'y':
            break
        else:
            print('Exiting program.')
            sys.exit()
    
