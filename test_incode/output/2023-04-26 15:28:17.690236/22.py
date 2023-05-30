#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input. """    
    while True:
        answer = input('Enter your choice: ')
        if answer == 'quit':
            break
        elif answer == 'quit\n':
            break
        else:
            print('You chose', answer)
    print('Thanks for playing!')
