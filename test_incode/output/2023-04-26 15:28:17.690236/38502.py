#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes a port or multiplyes fruits. """    
    
    ports = input("Enter the ports separated by commas: ").split(',')
    fruits = input("Enter the fruits separated by commas: ").split(',')
    
    ports = [int(p) for p in ports]
    fruits = [int(f) for f in fruits]
    
    fruits_sum = sum(