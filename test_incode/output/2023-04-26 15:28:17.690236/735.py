#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input or adds user input. """    
    while True:
        answer = input('Enter your choice: ')
        if answer == 'quit':
            break
        else:
            print('You chose:', answer)
