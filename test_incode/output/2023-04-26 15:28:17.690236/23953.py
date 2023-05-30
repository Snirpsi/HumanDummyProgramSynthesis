#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens fruits or multiplyes fruits. """    
    
    # Open fruits
    fruits = open_fruits()
    
    # Multiply fruits
    fruits_multiply = multiply_fruits(fruits)
    
    # Print results
    print("\nMultiplication of fruits:")
    print(fruits_multiply)
    
    # Close fruits
    fruits.close()
    
    # Close program
    exit()
    
# End of program
