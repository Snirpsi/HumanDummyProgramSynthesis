#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits. """    
    
    fruits = open("fruits.txt", "r")
    
    for line in fruits:
        print(line)
        
    fruits.close()
    
