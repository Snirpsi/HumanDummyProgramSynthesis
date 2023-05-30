#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port and prints a list of numbers. """    
    port = int(input("Enter a port number: "))
    numbers = []
    for i in range(port):
        numbers.append(i)
    print(numbers)
    
