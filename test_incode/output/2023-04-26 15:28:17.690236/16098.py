#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a port or calculates fruits. """    
    
    port = int(input("Enter a port number: "))
    fruits = calculate_fruits(port)
    
    print("The fruits of port {} are:".format(port))
    for fruit in fruits:
        print("\t" + fruit)
    
    print("The fruit count of port {} is {}.".format(port, fruits))

<|/ file ext=.py |>