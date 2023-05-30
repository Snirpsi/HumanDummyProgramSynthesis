#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts numbers or prints words. """    
    while True:
        number = input('Enter a number: ')
        if number.isdigit():
            print(int(number))
        else:
            print('Sorry, I don\'t understand that number')
