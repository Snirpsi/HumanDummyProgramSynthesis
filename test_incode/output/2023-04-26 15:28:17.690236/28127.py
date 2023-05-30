#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['cat', 'dog', 'bird', 'snake', 'mouse']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('Press enter to continue or type "quit" to quit: ')
        if choice == 'quit':
            break
        else:
            print('Please type "quit" to quit.')
            
