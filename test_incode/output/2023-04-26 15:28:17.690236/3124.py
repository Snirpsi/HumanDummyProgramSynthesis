#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers. """    
    
    while True:
        numbers = []
        for i in range(10):
            numbers.append(i)
        
        print("Adding numbers: ", numbers)
        
        numbers.append(