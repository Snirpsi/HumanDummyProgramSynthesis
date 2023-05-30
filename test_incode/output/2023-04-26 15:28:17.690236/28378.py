#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a port or removes fruits. """    
    
    # read a file
    fruits = open('fruits.txt', 'r')
    
    # read a line
    line = fruits.readline()
    
    # remove fruit
    fruits.close()
    
    # print result
    print(line)
    
    # close file
    fruits.close()
    
    # close terminal
    