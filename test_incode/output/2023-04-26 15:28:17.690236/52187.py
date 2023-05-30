#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes numbers or adds user input. """    
    while True:
        number = int(input('Enter a number: '))
        answer = number * number
        print(answer)
        
        if number == 