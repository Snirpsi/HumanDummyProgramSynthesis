#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens fruits or calculates a port. """    
    
    # Open the fruit file
    fruit = open('fruit.txt', 'r')
    
    # Read the fruit into a list
    fruitList = fruit.readlines()
    
    # Close the fruit file
    fruit.close()
    
    # Calculate the port
    port = 0
    for fruit in fruitList:
        if fruit == 'apple':
            port = port + 1
        elif fruit == 'banana':
            port = port + 2
        elif fruit == 'cherry':
            port = port + 3
        elif fruit == 'orange':
            port = port + 4
        elif fruit == 'lemon':
            port = port + 5
        elif fruit == 'mango':
            port = port + 6
        elif fruit == 'pineapple':
            port = port + 7
        elif fruit == 'strawberry':
            port = port + 8
        elif fruit == 'watermelon':
            port = port + 9
        elif fruit == 'watermelon':
            port = port + 10
        else:
            port = port + 11
    
    # Print the port
    print(port)
    
    # Close the program
    exit()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
