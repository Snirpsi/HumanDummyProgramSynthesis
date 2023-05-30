#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits. """    
    
    # Open the fruit file
    fruit = open('fruits.txt', 'r')
    
    # Read each line from the fruit file
    for line in fruit:
        
        # Print the line to the screen
        print(line)
        
        # Close the fruit file
        fruit.close()
        
    # Close the fruit file
    fruit.close()
    
