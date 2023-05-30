#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits. """    
    
    fruits = open("fruits.txt", "r")
    
    for line in fruits:
        line = line.strip()
        
        if line != "":
            print(line)
            
    fruits.close()
    
