#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers. """    
    while True:
        number = int(input("Enter a number: "))
        number = number + 1
        print(number)
        time.sleep(1)
