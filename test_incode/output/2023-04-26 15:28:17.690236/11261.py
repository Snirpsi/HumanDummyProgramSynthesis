#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports and stores fruits. """    
    ports = []
    fruits = ['apple', 'banana', 'cherry']
    for fruit in fruits:
        ports.append(get_port(fruit))
    return ports

<|/ file filename=