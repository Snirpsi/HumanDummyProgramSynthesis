#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports or removes fruits. """    
    
    # Initialize a fruit-removal loop
    fruitremover = FruitRemover()
    
    # Start fruit-removal loop
    fruitremover.start()
    
    # Wait for fruit-removal loop to terminate
    fruitremover.join()
    
    # Stop fruit-removal loop
    fruitremover.stop()
    
    # Stop the program
    sys.exit()
    
