#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        choice = input('> ')
        if choice == 'exit':
            break
        else:
            print(choice)
