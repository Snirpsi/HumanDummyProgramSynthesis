#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes user input and stores numbers. """    
    while True:
        try:
            number = int(input('Enter a number: '))
            number *= number
            print(number)
        except ValueError:
            print('Invalid input')
        else:
            break
