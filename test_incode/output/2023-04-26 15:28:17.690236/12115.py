#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input and removes a list of words. """    
    while True:
        word = input('Enter a word: ')
        words = word.split()
        
        removed = [word for word in words if word not in words]
        
        print('Removed words:', removed)
        
        print('Press enter to continue or type "quit" to quit.')
        
        choice = input('> ')
        
        if choice == 'quit':
            break
        
        else:
            print('Invalid input. Try again.')
            
    print('Goodbye!')
    
