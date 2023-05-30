#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers and removes user input. """    
    
    numbers = [int(i) for i in input().split()]
    
    for number in numbers:
        if number % 2 == 0:
            print(number)
        else:
            print("