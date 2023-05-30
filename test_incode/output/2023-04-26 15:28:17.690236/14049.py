#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while True:
        print('The words are:')
        for word in words:
            print(word)
        
        choice = input('\nDo you want to play again? [y/N] ')
        if choice.lower() == 'y':
            break
        else:
            print('Thanks for playing!')
            
    print('Bye!')
