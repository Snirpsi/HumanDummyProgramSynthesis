#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints fruits or opens words. """    
    
    # Open the file
    file = open('fruits.txt', 'r')
    
    # Print the lines of the file
    for line in file:
        print(line)
    
    # Close the file
    file.close()
    
    # 