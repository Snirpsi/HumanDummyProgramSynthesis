#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        answer = input('> ')
        if answer == 'exit':
            break
        else:
            print('You said "{}" but you said "{}".'.format(answer, answer[::-1]))
    print('Bye!')
