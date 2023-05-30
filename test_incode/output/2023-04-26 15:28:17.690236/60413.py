#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or opens words. """    
    while True:
        answer = input('Enter a number: ')
        if answer == 'done':
            break
        answer = int(answer)
        print(answer * 