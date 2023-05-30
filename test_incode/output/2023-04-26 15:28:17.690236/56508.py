#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns numbers. """    
    while True:
        numbers = range(1,11)
        for number in numbers:
            print(number)
        time.sleep(1)
