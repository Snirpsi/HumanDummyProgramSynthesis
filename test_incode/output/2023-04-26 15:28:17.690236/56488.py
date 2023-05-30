#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits. """    
    
    # Open the fruit file
    fruit = open('fruits.txt', 'r')
    
    # Read all fruit lines and print them
    for line in fruit:
        print(line)
        
    # Close the fruit file
    fruit.close()
    
    # Close the program
    