#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port and multiplyes a list of numbers. """    
    
    port = int(input("Enter a port number: "))
    numbers = list(map(int, input("Enter a list of numbers: ").split()))
    
    numbers.remove(port)
    numbers = numbers * port
    
    print(numbers)
    
