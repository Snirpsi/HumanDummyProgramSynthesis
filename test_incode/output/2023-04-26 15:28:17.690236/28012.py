#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        answer = input('Enter your choice: ')
        if answer == 'quit':
            break
        print('You chose:', answer)
