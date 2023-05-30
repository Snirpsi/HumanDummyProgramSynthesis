#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        answer = input('> ')
        if answer == 'q':
            break
        elif answer == 'n':
            print('Thank you!')
            break
        else:
            print('Sorry, I did not understand your input.')
