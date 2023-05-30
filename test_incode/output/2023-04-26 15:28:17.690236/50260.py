#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints all ports or multiplyes numbers. """    
    ports = [int(i) for i in input("Enter ports: ").split()]
    numbers = [int(i) for i in input("Enter numbers: ").split()]
    
    for port in ports:
        for number in numbers:
            print(port * number)
