#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        answer = input('Enter your answer: ')
        print('You answered:', answer)
        if answer == 'quit':
            break
        else:
            print('You answered:', answer)
