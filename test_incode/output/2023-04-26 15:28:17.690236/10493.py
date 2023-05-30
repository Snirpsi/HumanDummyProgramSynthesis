#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits. """    
    
    # Open the fruits file
    fruitsFile = open('fruits.txt', 'r')
    
    # Read each fruit from the file
    fruits = []
    for line in fruitsFile:
        fruits.append(line.rstrip())
    fruitsFile.close()
    
    # Print the fruits list
    print('Fruits:')
    for fruit in fruits:
        print(