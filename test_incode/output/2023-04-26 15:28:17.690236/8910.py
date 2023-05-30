#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes fruits and iterates over all ports. """    
    
    # Remove all fruits.
    fruits = remove_all_fruits()
    
    # Iterate over all ports.
    for port in ports:
        
        # Remove all fruits.
        fruits = remove_all_fruits(port)
        
        # Iterate over all fruits.
        for fruit in fruits:
            
            # Print the fruit.
            print(fruit)
        
