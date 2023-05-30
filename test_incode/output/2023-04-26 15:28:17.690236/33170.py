#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers or returns user input. """    
    
    import sys
    
    number = int(sys.argv[1])
    
    if number > 0 and number < 10:
        print(number)
    elif number > 10 and number < 20:
        print(number * 2)
    elif number > 20 and number < 30:
        print(number * 3)
    elif number > 30 and number < 40:
        print(number * 4)
    elif number > 40 and number < 50:
        print(number * 5)
    elif number > 50 and number < 60:
        print(number * 6)
    elif number > 60 and number < 70:
        print(number * 7)
    elif number > 70 and number < 80:
        print(number * 8)
    elif number > 80 and number < 90:
        print(number * 9)
    elif number > 90:
        print(number)
    else:
        print('Invalid input')
