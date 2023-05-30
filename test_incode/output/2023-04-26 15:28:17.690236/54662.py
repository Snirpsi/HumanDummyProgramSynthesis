#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes all ports and removes fruits. """    
    ports = range(1,6)
    fruits = ["apple", "orange", "banana", "cherry"]
    
    for port in ports:
        fruits.remove(fruits[port-1])
        
    for fruit in fruits:
        print(fruit)
    
