#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    for fruit in fruits:
        print("Adding " + fruit + "...")
        
        fruits.append(fruit)
        
    print("Done!")
    
