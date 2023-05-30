#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or enumerates user input. """    
    while True:
        choice = input('Choose a number or type "quit" to quit: ')
        if choice == 'quit':
            break
        else:
            choice = int(choice)
            print(choice)
            
