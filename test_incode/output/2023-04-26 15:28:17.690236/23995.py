#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    
    # Get the command line arguments
    args = sys.argv[1:]
    
    # Get the list of numbers
    numbers = [int(x) for x in args]
    
    # Get the product of the numbers
    product = reduce(lambda x, y: x * y, numbers)
    
    # Print the result
    print("The product is", product)
    
    # Close the connection
    connection.close()
    
